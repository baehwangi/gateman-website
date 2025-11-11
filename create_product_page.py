import sys
import re
import os
import urllib.request

if len(sys.argv) < 3:
    print("Usage: python create_product_page.py <product_url_slug> <product_display_name>")
    print("Example: python create_product_page.py gm_500s GM-500S")
    sys.exit(1)

url_slug = sys.argv[1]
product_name = sys.argv[2]

source_file = f"{url_slug}_source.html"
output_file = f"products/{url_slug.replace('_', '-')}.html"
image_dir = f"images/products/{url_slug}"

print(f"Creating page for {product_name}...")
print(f"  Source: {source_file}")
print(f"  Output: {output_file}")
print(f"  Images: {image_dir}")

# Create image directory
os.makedirs(image_dir, exist_ok=True)

# Read source HTML
try:
    with open(source_file, 'r', encoding='utf-8') as f:
        source = f.read()
except FileNotFoundError:
    print(f"ERROR: Source file {source_file} not found!")
    sys.exit(1)

# Extract CSS (look for .gaWrap or similar pattern)
css_match = re.search(r'\.gaWrap.*?</style>', source, re.DOTALL)
if css_match:
    official_css = css_match.group(0).replace('</style>', '')
else:
    print("WARNING: Could not find CSS in source file")
    official_css = ""

# Extract HTML content (look for .gaWrap div)
html_match = re.search(r'<div class="gaWrap">.*?<!-- //gaWrap -->', source, re.DOTALL)
if html_match:
    official_html = html_match.group(0)
else:
    print("ERROR: Could not find gaWrap content!")
    sys.exit(1)

# Replace image URLs
base_url_pattern = f'https://gateman.kr/common/img/smartdoorlock/gateman/{url_slug}/'
local_img_path = f'../images/products/{url_slug}/'

official_html = official_html.replace(base_url_pattern, local_img_path)
official_html = official_html.replace('https://gateman.kr/common/img/access/', local_img_path)
official_css = official_css.replace(base_url_pattern, local_img_path)
official_css = official_css.replace('https://gateman.kr/common/img/access/', local_img_path)

# Replace phone numbers
official_html = official_html.replace('1577-1919', '010-6633-7732')
official_html = official_html.replace('1544-3232', '010-6633-7732')

# Fix YouTube iframes - replace with clickable thumbnails
youtube_pattern = r'<iframe[^>]+src="https://www\.youtube\.com/embed/([^"?]+)[^"]*"[^>]*></iframe>'

def youtube_replacer(match):
    video_id = match.group(1)
    return f'''<a href="https://www.youtube.com/watch?v={video_id}" target="_blank" style="display:block;position:relative;padding-bottom:56.25%;height:0;overflow:hidden;">
                                <img src="https://img.youtube.com/vi/{video_id}/maxresdefault.jpg" alt="YouTube video" style="position:absolute;top:0;left:0;width:100%;height:100%;object-fit:cover;">
                                <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:80px;height:56px;background:rgba(255,0,0,0.9);border-radius:12px;cursor:pointer;">
                                    <svg viewBox="0 0 68 48" style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:48px;height:48px;"><path d="M66.52,7.74c-0.78-2.93-2.49-5.41-5.42-6.19C55.79,.13,34,0,34,0S12.21,.13,6.9,1.55 C3.97,2.33,2.27,4.81,1.48,7.74C0.06,13.05,0,24,0,24s0.06,10.95,1.48,16.26c0.78,2.93,2.49,5.41,5.42,6.19 C12.21,47.87,34,48,34,48s21.79-0.13,27.1-1.55c2.93-0.78,4.64-3.26,5.42-6.19C67.94,34.95,68,24,68,24S67.94,13.05,66.52,7.74z" fill="#f00"></path><path d="M 45,24 27,14 27,34" fill="#fff"></path></svg>
                                </div>
                            </a>'''

official_html = re.sub(youtube_pattern, youtube_replacer, official_html)

# Generate complete HTML page
html_template = f'''<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{product_name} - 게이트맨 김해 밀양 공식 대리점</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@10/swiper-bundle.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700&display=swap" rel="stylesheet">
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

        /* WOW.js animations */
        .fadeUpMotion, .slideLeftMotion, .slideRightMotion {{
            visibility: visible !important;
            animation-name: fadeInUp !important;
        }}
        @keyframes fadeInUp {{
            from {{ opacity: 0; transform: translate3d(0, 40px, 0); }}
            to {{ opacity: 1; transform: translate3d(0, 0, 0); }}
        }}

        /* Official CSS */
        {official_css}

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

    {official_html}

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

    <script src="https://cdn.jsdelivr.net/npm/swiper@10/swiper-bundle.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/wow/1.1.2/wow.min.js"></script>
    <script src="https://kit.fontawesome.com/your-kit-id.js" crossorigin="anonymous"></script>
    <script>
        new WOW().init();

        // Gateman Dot Slider
        if (document.querySelector('.gvSlider')) {{
            new Swiper('.gvSlider', {{
                slidesPerView: 1,
                effect: 'fade',
                fadeEffect: {{ crossFade: true }},
                speed: 1500,
                spaceBetween: 30,
                loop: true,
                autoplay: {{ delay: 2000, disableOnInteraction: false }}
            }});
        }}

        // Function Sliders (Safety & Convenience)
        var mySwipers = [];
        function initOrDestroySwipers() {{
            var windowWidth = window.innerWidth;
            var sliders = document.querySelectorAll('.gfSlider');
            if (windowWidth > 1000) {{
                if (!mySwipers.length && sliders.length) {{
                    sliders.forEach(function(slider){{
                        mySwipers.push(new Swiper(slider, {{
                            breakpoints: {{
                                1000: {{ slidesPerView: 2.2, spaceBetween: 40 }},
                                1400: {{ slidesPerView: 3.4, spaceBetween: 90 }}
                            }}
                        }}));
                    }});
                }}
            }} else {{
                if (mySwipers.length) {{
                    mySwipers.forEach(function(swiper){{ swiper.destroy(true, true); }});
                    mySwipers = [];
                }}
            }}
        }}

        if (document.querySelectorAll('.gfSlider').length) {{
            initOrDestroySwipers();
            window.addEventListener('resize', initOrDestroySwipers);
        }}
    </script>
</body>
</html>'''

# Write output file
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(html_template)

print(f"SUCCESS: Created {output_file} ({len(html_template)} bytes)")

# Download images
print("Downloading images...")
img_tags = re.findall(r'<img[^>]+src="([^"]+)"', official_html)
css_backgrounds = re.findall(r'url\(["\']?([^)"\' ]+\.(?:png|jpg|jpeg|gif))["\']?\)', official_css, re.IGNORECASE)

all_images = set()
for img in img_tags + css_backgrounds:
    if img.startswith('../images/products/'):
        filename = img.split('/')[-1]
        all_images.add(filename)

print(f"Found {len(all_images)} unique images to download")

headers = {'User-Agent': 'Mozilla/5.0'}
downloaded = 0
failed = 0

for filename in sorted(all_images):
    filepath = os.path.join(image_dir, filename)
    if os.path.exists(filepath):
        continue

    url = f'https://gateman.kr/common/img/smartdoorlock/gateman/{url_slug}/{filename}'

    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            with open(filepath, 'wb') as f:
                f.write(response.read())
        downloaded += 1
        print(f"  OK: {filename}")
    except Exception as e:
        # Try access folder
        try:
            url = f'https://gateman.kr/common/img/access/{filename}'
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as response:
                with open(filepath, 'wb') as f:
                    f.write(response.read())
            downloaded += 1
            print(f"  OK: {filename} (from access)")
        except:
            failed += 1
            print(f"  SKIP: {filename}")

print(f"Downloaded: {downloaded}, Failed: {failed}")
print("DONE!")
