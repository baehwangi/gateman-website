import urllib.request
import os
import time

# Mortise 제품 목록 (우리가 필요한 제품들만)
products = [
    {"name": "GL-200H", "url": "gl_200H"},
    {"name": "G-GRAB scan+", "url": "grab100_fh"},
    {"name": "G-GRAB touch", "url": "g_grab_touch"},
    {"name": "GR-20", "url": "gr_20"},
    {"name": "GR-SASH", "url": "gr_sash"},
    {"name": "GR-CLIP", "url": "gr_clip"},
    {"name": "GR-FRAME", "url": "gr_frame"},
    {"name": "G-TOUCH", "url": "g_touch"}
]

print("=" * 60)
print("Mortise 제품 HTML 소스 다운로드")
print("=" * 60)
print(f"총 {len(products)}개 제품 처리 예정")
print("=" * 60)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

for idx, product in enumerate(products, 1):
    product_name = product['name']
    url_slug = product['url']

    print(f"\n[{idx}/{len(products)}] {product_name} 처리 중...")

    # 공식 사이트 URL
    official_url = f"https://gateman.kr/{url_slug}"
    source_file = f"{url_slug}_source.html"

    # HTML 소스 다운로드
    print(f"  - 공식 페이지 다운로드: {official_url}")

    # 이미 다운로드된 파일이 있으면 스킵
    if os.path.exists(source_file):
        print(f"    SKIP: {source_file} already exists")
        continue

    try:
        req = urllib.request.Request(official_url, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as response:
            html_content = response.read().decode('utf-8')

        with open(source_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"    OK: {source_file} ({len(html_content)} bytes)")

    except Exception as e:
        print(f"    ERROR: {e}")
        continue

    time.sleep(1)

print("\n" + "=" * 60)
print("다운로드 완료!")
print("=" * 60)
