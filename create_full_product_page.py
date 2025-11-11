# -*- coding: utf-8 -*-
import re
import sys
import os
import urllib.request

def create_full_product_page(url_slug, product_name):
    """Create complete product page with all CSS and JS like GM-900S"""

    source_file = f'{url_slug}_source.html'
    output_file = f'products/{url_slug.replace("_", "-")}.html'
    image_dir = f'images/products/{url_slug}'

    print(f"Creating full page for {product_name}...")
    print(f"  Source: {source_file}")
    print(f"  Output: {output_file}")
    print(f"  Images: {image_dir}")

    # Read source HTML
    try:
        with open(source_file, 'r', encoding='utf-8') as f:
            source = f.read()
    except FileNotFoundError:
        print(f"ERROR: Source file {source_file} not found!")
        return False

    # Extract ALL <style> blocks
    style_blocks = []
    style_matches = re.finditer(r'<style[^>]*>(.*?)</style>', source, re.DOTALL | re.IGNORECASE)
    for match in style_matches:
        style_blocks.append(match.group(1))

    print(f"  Found {len(style_blocks)} style blocks")

    # Extract ALL <link rel="stylesheet"> tags
    link_tags = re.findall(r'<link[^>]+rel=["\']stylesheet["\'][^>]*>', source, re.IGNORECASE)
    print(f"  Found {len(link_tags)} stylesheet links")

    # Extract the main content section
    content_match = re.search(r'<section[^>]*id=["\']container["\'][^>]*style="[^"]*">(.*?)</section>', source, re.DOTALL)
    if not content_match:
        content_match = re.search(r'<section[^>]*id=["\']container["\'][^>]*>(.*?)</section>', source, re.DOTALL)

    if not content_match:
        print("ERROR: Could not find container section!")
        return False

    main_content = content_match.group(0)
    print(f"  Found container: {len(main_content)} characters")

    # Replace image URLs to use local paths
    base_url = 'https://gateman.kr/'
    local_img_prefix = '../images/products/' + url_slug + '/'

    # Replace image paths in main content
    main_content = re.sub(
        r'src="?/common/img/smartdoorlock/gateman/' + url_slug + r'/([^"\s]+)"?',
        r'src="' + local_img_prefix + r'\1"',
        main_content
    )

    # Replace phone numbers
    main_content = main_content.replace('1577-1919', '010-6633-7732')
    main_content = main_content.replace('1544-3232', '010-6633-7732')

    # Fix YouTube iframes to clickable thumbnails
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

    # Combine all styles into one big style block
    combined_styles = '\n\n'.join(style_blocks)

    # Create full HTML page
    html = f'''<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{product_name} - 게이트맨 김해 밀양 공식 대리점</title>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700&display=swap" rel="stylesheet">

    <!-- Original Stylesheets -->
    {chr(10).join(link_tags)}

    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Noto Sans KR', sans-serif; line-height: 1.6; color: #333; padding-top: 100px; }}

        /* Custom Header */
        .custom-header {{ position: fixed; top: 0; left: 0; right: 0; background: white; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); z-index: 10000; }}
        .container {{ max-width: 1400px; margin: 0 auto; padding: 0 20px; }}
        .header-content {{ display: flex; justify-content: space-between; align-items: center; padding: 15px 0; }}
        .logo {{ display: flex; align-items: center; gap: 10px; }}
        .logo img {{ height: 50px; width: auto; }}
        .logo a {{ text-decoration: none; display: flex; align-items: center; gap: 10px; }}
        .dealer-badge {{ background: #1a5490; color: white; padding: 10px 20px; border-radius: 25px; font-size: 1.1rem; font-weight: 600; }}
        .main-nav ul {{ display: flex; list-style: none; gap: 40px; }}
        .main-nav a {{ text-decoration: none; color: #333; font-weight: 500; font-size: 1rem; transition: color 0.3s; }}
        .main-nav a:hover, .main-nav a.active {{ color: #1a5490; }}
        .header-contact {{ display: flex; align-items: center; gap: 8px; color: #1a5490; font-weight: 600; font-size: 1.1rem; }}

        /* Custom Footer */
        .custom-footer {{ background: #2c3e50; color: white; padding: 60px 0 30px; margin-top: 100px; }}
        .footer-content {{ display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 60px; margin-bottom: 40px; }}
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
        @media (max-width: 1000px) {{
            .header-content {{ flex-wrap: wrap; }}
            .main-nav {{ display: none; }}
            .footer-content {{ grid-template-columns: 1fr; gap: 30px; }}
        }}
        @media (max-width: 768px) {{
            .mobile-bottom-buttons {{ position: fixed; bottom: 0; left: 0; right: 0; display: grid; grid-template-columns: 1fr 1fr; gap: 0; z-index: 999; box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.1); }}
            .mobile-btn {{ padding: 18px; text-align: center; color: white; text-decoration: none; font-weight: 600; font-size: 1rem; border: none; display: flex; align-items: center; justify-content: center; gap: 8px; }}
            .mobile-btn-call, .mobile-btn-contact {{ background: linear-gradient(135deg, #1a5490 0%, #2c3e50 100%); }}
            .mobile-btn:active {{ opacity: 0.8; }}
            body {{ padding-bottom: 70px; }}
        }}
        @media (min-width: 769px) {{ .mobile-bottom-buttons {{ display: none; }} }}

        /* Original Styles */
        {combined_styles}
    </style>
</head>
<body>
    <header class="custom-header">
        <div class="container">
            <div class="header-content">
                <div class="logo">
                    <a href="../index.html">
                        <img src="../images/gateman-logo.png" alt="게이트맨">
                        <span class="dealer-badge">김해 밀양 공식 대리점</span>
                    </a>
                </div>
                <nav class="main-nav">
                    <ul>
                        <li><a href="../index.html#about">브랜드 소개</a></li>
                        <li><a href="../smartdoorlock.html" class="active">스마트도어락</a></li>
                        <li><a href="../index.html#technology">기술력</a></li>
                        <li><a href="../index.html#contact">문의하기</a></li>
                    </ul>
                </nav>
                <div class="header-contact">
                    <i class="fas fa-phone"></i>
                    <span>010-6633-7732</span>
                </div>
            </div>
        </div>
    </header>

    {main_content}

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

    <script src="https://kit.fontawesome.com/your-kit-id.js" crossorigin="anonymous"></script>

    <!-- Original Scripts from source -->
    <script src="https://gateman.kr/common/js/jquery.min.js"></script>
    <script src="https://gateman.kr/common/js/x.min.js"></script>
    <script src="https://gateman.kr/common/js/xe.min.js"></script>
    <script src="https://gateman.kr/layouts/KSO_Infinity/js/bootstrap.min.js"></script>
    <script src="https://gateman.kr/layouts/KSO_Infinity/js/jquery.sticky.js"></script>
    <script src="https://gateman.kr/layouts/KSO_Infinity/js/waypoints.min.js"></script>
    <script src="https://gateman.kr/layouts/KSO_Infinity/js/owl.carousel.min.js"></script>
</body>
</html>'''

    # Write output file
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"SUCCESS: Created {output_file} ({len(html)} bytes)")
        return True
    except Exception as e:
        print(f"ERROR writing {output_file}: {e}")
        return False

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python create_full_product_page.py <url_slug> <product_name>")
        print("Example: python create_full_product_page.py g_suit_touch 'G-SUIT touch'")
        sys.exit(1)

    url_slug = sys.argv[1]
    product_name = sys.argv[2]

    success = create_full_product_page(url_slug, product_name)
    sys.exit(0 if success else 1)
