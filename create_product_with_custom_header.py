# -*- coding: utf-8 -*-
import re
import sys
import urllib.request

def create_product_with_custom_header(url, product_slug, product_name):
    """Extract product content and wrap with our custom header/footer like GM-900S"""

    output_file = f'products/{product_slug}.html'

    print(f"Creating {product_name} page...")
    print(f"  Source: {url}")
    print(f"  Output: {output_file}")

    # Download HTML
    headers = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            source = response.read().decode('utf-8')
        print(f"  Downloaded: {len(source)} bytes")
    except Exception as e:
        print(f"ERROR downloading: {e}")
        return False

    # Extract ALL <style> blocks from source
    style_blocks = []
    for match in re.finditer(r'<style[^>]*>(.*?)</style>', source, re.DOTALL | re.IGNORECASE):
        style_blocks.append(match.group(1))

    print(f"  Found {len(style_blocks)} style blocks")

    # Extract ALL CSS link tags
    css_links = []
    for match in re.finditer(r'<link[^>]+stylesheet[^>]*>', source, re.IGNORECASE):
        link_tag = match.group(0)
        href_match = re.search(r'href=[\"\']([^\"\']+)', link_tag)
        if href_match:
            href = href_match.group(1)
            if not href.startswith('http'):
                href = 'https://gateman.kr' + href
            css_links.append(href)

    print(f"  Found {len(css_links)} CSS links")

    # Extract the main content section (everything inside <section id="container">)
    content_match = re.search(r'<section[^>]*id=["\']container["\'][^>]*>(.*?)</section>', source, re.DOTALL)

    if not content_match:
        print("ERROR: Could not find container section!")
        return False

    main_content = content_match.group(0)
    print(f"  Found main content: {len(main_content)} characters")

    # Replace phone numbers
    main_content = main_content.replace('1577-1919', '010-6633-7732')
    main_content = main_content.replace('1544-3232', '010-6633-7732')

    # Replace YouTube iframes with clickable thumbnails
    def youtube_replacer(match):
        video_id = match.group(1)
        return f'''<a href="https://www.youtube.com/watch?v={video_id}" target="_blank" style="display:block;position:relative;padding-bottom:56.25%;height:0;overflow:hidden;max-width:100%;">
    <img src="https://img.youtube.com/vi/{video_id}/maxresdefault.jpg" alt="YouTube video" style="position:absolute;top:0;left:0;width:100%;height:100%;object-fit:cover;">
    <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:80px;height:56px;background:rgba(255,0,0,0.9);border-radius:12px;cursor:pointer;">
        <svg viewBox="0 0 68 48" style="width:100%;height:100%;"><path d="M66.52 7.74c-.78-2.93-2.49-5.41-5.42-6.19C55.79.13 34 0 34 0S12.21.13 6.9 1.55c-2.93.78-4.63 3.26-5.42 6.19C.06 13.05 0 24 0 24s.06 10.95 1.48 16.26c.78 2.93 2.49 5.41 5.42 6.19C12.21 47.87 34 48 34 48s21.79-.13 27.1-1.55c2.93-.78 4.64-3.26 5.42-6.19C67.94 34.95 68 24 68 24s-.06-10.95-1.48-16.26z" fill="white"></path><path d="M45 24L27 14v20" fill="#FF0000"></path></svg>
    </div>
</a>'''

    main_content = re.sub(
        r'<iframe[^>]+src="https://www\.youtube\.com/embed/([^"?]+)[^"]*"[^>]*></iframe>',
        youtube_replacer,
        main_content,
        flags=re.IGNORECASE
    )

    # Replace product image paths to local
    product_folder = url.rstrip('/').split('/')[-1]
    main_content = re.sub(
        r'src="?/common/img/smartdoorlock/gateman/' + product_folder + r'/([^"\s]+)"?',
        r'src="../images/products/' + product_folder + r'/\1"',
        main_content
    )

    # Fix other image paths in content to use gateman.kr
    main_content = re.sub(r'src="/common/img/', r'src="https://gateman.kr/common/img/', main_content)
    main_content = re.sub(r'src="/files/', r'src="https://gateman.kr/files/', main_content)

    # Combine all styles
    combined_styles = '\n\n'.join(style_blocks)

    # Fix background image URLs in CSS
    combined_styles = re.sub(r'url\(/common/', r'url(https://gateman.kr/common/', combined_styles)
    combined_styles = re.sub(r'url\(/files/', r'url(https://gateman.kr/files/', combined_styles)

    # Remove all .header related styles from original CSS to prevent conflicts
    combined_styles = re.sub(r'\.header[^{]*\{[^}]*\}', '', combined_styles, flags=re.MULTILINE)
    combined_styles = re.sub(r'\.header-[^{]*\{[^}]*\}', '', combined_styles, flags=re.MULTILINE)

    # Create complete HTML with our custom header/footer (GM-900S style)
    # Build CSS links HTML
    css_links_html = '\n    '.join([f'<link rel="stylesheet" href="{link}">' for link in css_links])

    html = f'''<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{product_name} - 게이트맨 김해 밀양 공식 대리점</title>

    <!-- Original CSS Files FIRST -->
    {css_links_html}

    <!-- Font Awesome AFTER original CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <!-- Custom Header Styles - LAST TO OVERRIDE -->
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Noto Sans KR', sans-serif; color: #231f20; line-height: 1.6; }}

        /* Header - Force override original Gateman CSS */
        .header {{
            position: fixed !important;
            top: 0 !important;
            left: 0 !important;
            right: 0 !important;
            background: white !important;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1) !important;
            z-index: 10000 !important;
            width: 100% !important;
        }}

        .header .container {{
            max-width: 1400px !important;
            margin: 0 auto !important;
            padding: 0 20px !important;
        }}

        .header-content {{
            display: flex !important;
            justify-content: space-between !important;
            align-items: center !important;
            padding: 15px 0 !important;
        }}

        .header .logo {{
            display: flex !important;
            align-items: center !important;
            gap: 10px !important;
        }}

        .header .logo img {{
            height: 50px !important;
            width: auto !important;
        }}

        .header .dealer-badge {{
            background: #1a5490 !important;
            color: white !important;
            padding: 10px 20px !important;
            border-radius: 25px !important;
            font-size: 1.1rem !important;
            font-weight: 600 !important;
        }}

        .header .main-nav ul {{
            display: flex !important;
            list-style: none !important;
            gap: 40px !important;
            margin: 0 !important;
            padding: 0 !important;
        }}

        .header .main-nav a {{
            text-decoration: none !important;
            color: #333 !important;
            font-weight: 500 !important;
            font-size: 1rem !important;
            transition: color 0.3s !important;
        }}

        .header .main-nav a:hover,
        .header .main-nav a.active {{
            color: #1a5490 !important;
        }}

        .header .header-contact {{
            display: flex !important;
            align-items: center !important;
            gap: 8px !important;
            color: #1a5490 !important;
            font-weight: 600 !important;
            font-size: 1.1rem !important;
        }}

        .header .header-contact span {{
            color: #1a5490 !important;
        }}

        .header .mobile-menu-btn {{
            display: none !important;
            background: none !important;
            border: none !important;
            font-size: 1.5rem !important;
            color: #333 !important;
            cursor: pointer !important;
        }}

        @media (max-width: 1000px) {{
            .header .main-nav {{
                display: none !important;
            }}
            .header .mobile-menu-btn {{
                display: block !important;
            }}
        }}

        /* Page content spacing */
        .page-content {{ margin-top: 80px; }}

        /* Custom Footer */
        .custom-footer {{ background: #2c3e50; color: white; padding: 60px 0 30px; margin-top: 100px; }}
        .footer-content {{ display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 60px; margin-bottom: 40px; max-width: 1400px; margin: 0 auto; padding: 0 20px; }}
        .footer-logo {{ font-size: 1.5rem; font-weight: 700; color: #fff; margin-bottom: 20px; }}
        .footer-info p {{ margin-bottom: 10px; color: #bdc3c7; }}
        .footer-links h4 {{ color: #fff; margin-bottom: 20px; font-size: 1.1rem; }}
        .footer-links ul {{ list-style: none; }}
        .footer-links a {{ color: #bdc3c7; text-decoration: none; display: block; margin-bottom: 10px; transition: color 0.3s; }}
        .footer-links a:hover {{ color: #fff; }}
        .footer-bottom {{ text-align: center; padding-top: 30px; border-top: 1px solid #34495e; color: #95a5a6; }}

        /* Mobile buttons */
        .mobile-bottom-buttons {{ display: none; }}

        /* Responsive */
        @media (max-width: 768px) {{
            .header .header-content {{
                flex-direction: row !important;
                justify-content: center !important;
                align-items: center !important;
                position: relative !important;
            }}

            .header .logo {{
                flex: 0 1 auto !important;
                justify-content: center !important;
            }}

            .header .logo a {{
                justify-content: center !important;
                gap: 8px !important;
            }}

            .header .logo img {{
                height: 40px !important;
            }}

            .header .dealer-badge {{
                font-size: 0.75rem !important;
                padding: 6px 12px !important;
            }}

            .header .header-contact {{
                display: none !important;
            }}

            .header .mobile-menu-btn {{
                display: block !important;
                position: absolute !important;
                right: -5px !important;
                top: 50% !important;
                transform: translateY(-50%) !important;
                font-size: 2rem !important;
                padding-right: 15px !important;
            }}

            .footer-content {{ grid-template-columns: 1fr; gap: 30px; }}
            .mobile-bottom-buttons {{ position: fixed; bottom: 0; left: 0; right: 0; display: grid; grid-template-columns: 1fr 1fr; gap: 0; z-index: 999; box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.1); }}
            .mobile-btn {{ padding: 18px; text-align: center; color: white; text-decoration: none; font-weight: 600; font-size: 1rem; border: none; display: flex; align-items: center; justify-content: center; gap: 8px; }}
            .mobile-btn-call, .mobile-btn-contact {{ background: linear-gradient(135deg, #1a5490 0%, #2c3e50 100%); }}
            .mobile-btn:active {{ opacity: 0.8; }}
            body {{ padding-bottom: 70px; }}
        }}

        /* Original Product Styles */
        {combined_styles}
    </style>
</head>
<body>
    <header class="header" style="position: fixed !important; top: 0 !important; left: 0 !important; right: 0 !important; background: white !important; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1) !important; z-index: 10000 !important; width: 100% !important;">
        <div class="container" style="max-width: 1400px !important; margin: 0 auto !important; padding: 0 20px !important;">
            <div class="header-content" style="display: flex !important; justify-content: space-between !important; align-items: center !important; padding: 15px 0 !important;">
                <div class="logo" style="display: flex !important; align-items: center !important; gap: 10px !important;">
                    <a href="../index.html" style="display: flex !important; align-items: center !important; gap: 15px !important; text-decoration: none !important;">
                        <img src="../logo/logo.png" alt="GATEMAN Logo" style="height: 50px !important; width: auto !important;">
                        <span class="dealer-badge" style="background: #1a5490 !important; color: white !important; padding: 10px 20px !important; border-radius: 25px !important; font-size: 1.1rem !important; font-weight: 600 !important;">김해 밀양 공식 대리점</span>
                    </a>
                </div>
                <nav class="main-nav" style="display: flex !important;">
                    <ul style="display: flex !important; list-style: none !important; gap: 40px !important; margin: 0 !important; padding: 0 !important;">
                        <li><a href="../smartdoorlock.html" style="text-decoration: none !important; color: #333 !important; font-weight: 500 !important; font-size: 1rem !important;">스마트도어락</a></li>
                        <li><a href="../technology.html" style="text-decoration: none !important; color: #333 !important; font-weight: 500 !important; font-size: 1rem !important;">테크놀로지</a></li>
                        <li><a href="../cs_support.html" style="text-decoration: none !important; color: #333 !important; font-weight: 500 !important; font-size: 1rem !important;">고객지원</a></li>
                        <li><a href="../purchase.html" style="text-decoration: none !important; color: #333 !important; font-weight: 500 !important; font-size: 1rem !important;">제품구매</a></li>
                        <li><a href="../gateman.html" style="text-decoration: none !important; color: #333 !important; font-weight: 500 !important; font-size: 1rem !important;">게이트맨</a></li>
                    </ul>
                </nav>
                <div class="header-contact" style="display: flex !important; align-items: center !important; gap: 8px !important; color: #1a5490 !important; font-weight: 600 !important; font-size: 1.1rem !important;">
                    <i class="fas fa-phone"></i>
                    <span style="color: #1a5490 !important;">010-6633-7732</span>
                </div>
                <button class="mobile-menu-btn" style="display: none !important; background: none !important; border: none !important; font-size: 1.5rem !important; color: #333 !important; cursor: pointer !important;">
                    <i class="fas fa-bars"></i>
                </button>
            </div>
        </div>
    </header>

    <div class="page-content">
        {main_content}
    </div>

    <footer class="custom-footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-about">
                    <div class="footer-logo">게이트맨 김해 밀양 공식 대리점</div>
                    <div class="footer-info">
                        <p><strong>대표:</strong> 대리점명</p>
                        <p><strong>주소:</strong> 경남 김해시/밀양시</p>
                        <p><strong>전화:</strong> 010-6633-7732</p>
                        <p><strong>영업시간:</strong> 평일 09:00 - 18:00</p>
                    </div>
                </div>
                <div class="footer-links">
                    <h4>제품 정보</h4>
                    <ul>
                        <li><a href="../smartdoorlock.html">스마트도어락</a></li>
                        <li><a href="../index.html#technology">기술력</a></li>
                        <li><a href="../index.html#contact">문의하기</a></li>
                    </ul>
                </div>
                <div class="footer-links">
                    <h4>고객 지원</h4>
                    <ul>
                        <li><a href="tel:010-6633-7732">전화 상담</a></li>
                        <li><a href="../index.html#contact">온라인 문의</a></li>
                        <li><a href="../index.html#about">오시는 길</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2024 게이트맨 김해 밀양 공식 대리점. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <div class="mobile-bottom-buttons">
        <a href="tel:010-6633-7732" class="mobile-btn mobile-btn-call">
            <i class="fas fa-phone"></i>
            <span>전화 상담</span>
        </a>
        <a href="../index.html#contact" class="mobile-btn mobile-btn-contact">
            <i class="fas fa-envelope"></i>
            <span>문의하기</span>
        </a>
    </div>

    <!-- Original Scripts -->
    <script src="https://gateman.kr/common/js/jquery.min.js"></script>
    <script src="https://gateman.kr/common/js/x.min.js"></script>
    <script src="https://gateman.kr/common/js/xe.min.js"></script>
</body>
</html>'''

    # Write output
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"SUCCESS: Created {output_file} ({len(html)} bytes)")
        return True
    except Exception as e:
        print(f"ERROR writing file: {e}")
        return False

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python create_product_with_custom_header.py <url> <product_slug> <product_name>")
        print("Example: python create_product_with_custom_header.py https://gateman.kr/g_suit_touch g-suit-touch 'G-SUIT touch'")
        sys.exit(1)

    url = sys.argv[1]
    product_slug = sys.argv[2]
    product_name = sys.argv[3]

    success = create_product_with_custom_header(url, product_slug, product_name)
    sys.exit(0 if success else 1)
