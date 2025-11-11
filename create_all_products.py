import urllib.request
import os
import re
import time

# 제품 목록 (GM-900S는 이미 완료)
products = [
    {"name": "GM-500S", "url": "gm_500s"},
    {"name": "GP-900D", "url": "gp_900d"},
    {"name": "GP-700D", "url": "gp_700d"},
    {"name": "GP-500R", "url": "gp_500r"},
    {"name": "G-GRAB touch", "url": "g_grab_touch"},
    {"name": "G-GRAB scan+", "url": "g_grab_scan_plus"},
    {"name": "GM-1000L", "url": "gm_1000l"},
    {"name": "GL-200H", "url": "gl_200h"},
    {"name": "GR-20", "url": "gr_20"},
    {"name": "GR-SASH", "url": "gr_sash"},
    {"name": "GR-CLIP", "url": "gr_clip"},
    {"name": "GR-FRAME", "url": "gr_frame"},
    {"name": "G-TOUCH", "url": "g_touch"},
    {"name": "G-SUIT touch+", "url": "g_suit_touch_plus"},
    {"name": "GP-300UN", "url": "gp_300un"},
    {"name": "G-CLICK scan+", "url": "g_click_scan_plus"}
]

print("=" * 60)
print("게이트맨 제품 상세 페이지 생성 스크립트")
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

    # 1. HTML 소스 다운로드
    print(f"  - 공식 페이지 다운로드: {official_url}")
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

    time.sleep(1)  # 서버 부하 방지

print("\n" + "=" * 60)
print("HTML 소스 다운로드 완료!")
print("=" * 60)
