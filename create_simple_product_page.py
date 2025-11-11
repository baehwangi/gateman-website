import sys
import re
import os
import urllib.request

if len(sys.argv) < 3:
    print("Usage: python create_simple_product_page.py <product_url_slug> <product_display_name>")
    sys.exit(1)

url_slug = sys.argv[1]
product_name = sys.argv[2]

source_file = f"{url_slug}_source.html"
output_file = f"products/{url_slug.replace('_', '-')}.html"
image_dir = f"images/products/{url_slug}"

print(f"Creating simple page for {product_name}...")
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

# Extract main content - look for section with product images
content_match = re.search(r'<section[^>]*id="container"[^>]*>.*?</section>', source, re.DOTALL)
if content_match:
    official_html = content_match.group(0)
else:
    # Try alternative pattern
    content_match = re.search(r'<div[^>]*data-element="main"[^>]*>.*?</div>', source, re.DOTALL)
    if content_match:
        official_html = f'<section id="container">{content_match.group(0)}</section>'
    else:
        print("ERROR: Could not find main content!")
        sys.exit(1)

# Replace image URLs
base_url_pattern = f'https://gateman.kr/common/img/smartdoorlock/gateman/{url_slug}/'
local_img_path = f'../images/products/{url_slug}/'

official_html = official_html.replace(base_url_pattern, local_img_path)
official_html = official_html.replace('/common/img/smartdoorlock/gateman/' + url_slug + '/', local_img_path)

# Replace phone numbers
official_html = official_html.replace('1577-1919', '010-6633-7732')
official_html = official_html.replace('1544-3232', '010-6633-7732')

# Generate complete HTML page
html_template = f'''<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{product_name} - 게이트맨 김해 밀양 공식 대리점</title>
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

        /* Product Content */
        #container {{ max-width: 100%; margin: 0 auto; }}
        #container img {{ max-width: 100%; height: auto; display: block; margin: 0 auto; }}
        .img_resizing {{ text-align: center; }}

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

    <script src="https://kit.fontawesome.com/your-kit-id.js" crossorigin="anonymous"></script>
</body>
</html>'''

# Write output file
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(html_template)

print(f"SUCCESS: Created {output_file} ({len(html_template)} bytes)")

# Download images
print("Downloading images...")

# Find all image references
img_urls = re.findall(r'src="([^"]+\.(?:jpg|jpeg|png|gif))"', official_html, re.IGNORECASE)

all_images = set()
for img_url in img_urls:
    if img_url.startswith('../images/products/'):
        filename = img_url.split('/')[-1]
        all_images.add(filename)
    elif img_url.startswith('/common/img/') or img_url.startswith('https://gateman.kr'):
        # Extract filename
        filename = img_url.split('/')[-1]
        all_images.add(filename)

print(f"Found {len(all_images)} unique images to download")

headers = {'User-Agent': 'Mozilla/5.0'}
downloaded = 0
failed = 0

for filename in sorted(all_images):
    filepath = os.path.join(image_dir, filename)
    if os.path.exists(filepath):
        continue

    # Try product folder first
    url = f'https://gateman.kr/common/img/smartdoorlock/gateman/{url_slug}/{filename}'
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            with open(filepath, 'wb') as f:
                f.write(response.read())
        downloaded += 1
        print(f"  OK: {filename}")
        continue
    except:
        pass

    # Try from files/attach folder
    try:
        # Search in source for the actual URL of this file
        file_pattern = re.search(rf'https://gateman\.kr/\./files/attach/[^"\']+/{re.escape(filename)}', source)
        if file_pattern:
            url = file_pattern.group(0)
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as response:
                with open(filepath, 'wb') as f:
                    f.write(response.read())
            downloaded += 1
            print(f"  OK: {filename} (from files)")
            continue
    except:
        pass

    failed += 1
    print(f"  SKIP: {filename}")

print(f"Downloaded: {downloaded}, Failed: {failed}")
print("DONE!")
