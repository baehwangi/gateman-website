# -*- coding: utf-8 -*-
import re
import urllib.request
import os

# All 17 products with their URL slugs
products = [
    ('gm_900s', 'gm-900s'),
    ('gm_500s', 'gm-500s'),
    ('gm_1000l', 'gm-1000l'),
    ('gp_900d', 'gp-900d'),
    ('gp_700d', 'gp-700d'),
    ('gp_500r', 'gp-500r'),
    ('gp_300un', 'gp-300un'),
    ('g_grab_touch', 'g-grab-touch'),
    ('grab100_fh', 'grab100-fh'),
    ('gl_200h', 'gl-200h'),
    ('gr_20', 'gr-20'),
    ('gr_sash', 'gr-sash'),
    ('gr_clip', 'gr-clip'),
    ('gr_frame', 'gr-frame'),
    ('g_touch', 'g-touch'),
    ('g_suit_touch', 'g-suit-touch'),
    ('g_click_scan', 'g-click-scan'),
]

print("Downloading images for all 17 products...")
print("=" * 70)

headers = {'User-Agent': 'Mozilla/5.0'}
total_downloaded = 0
total_images = 0

for url_slug, file_slug in products:
    print(f"\n{file_slug.upper()}")

    # Read HTML file
    html_path = f'products/{file_slug}.html'

    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            html = f.read()
    except FileNotFoundError:
        print(f"  ERROR: {html_path} not found")
        continue

    # Find all image references
    img_pattern = r'src=\"\.\./images/products/' + url_slug + r'/([^\"]+)\"'
    images = list(set(re.findall(img_pattern, html)))
    images.sort()

    if not images:
        print(f"  No images found")
        continue

    print(f"  Found {len(images)} images")
    total_images += len(images)

    # Create directory
    img_dir = f'images/products/{url_slug}'
    os.makedirs(img_dir, exist_ok=True)

    # Download images
    downloaded = 0
    base_url = f'https://gateman.kr/common/img/smartdoorlock/gateman/{url_slug}/'

    for img in images:
        filepath = f'{img_dir}/{img}'

        if os.path.exists(filepath):
            downloaded += 1
            continue

        url = base_url + img
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as response:
                with open(filepath, 'wb') as f:
                    f.write(response.read())
            print(f"    Downloaded: {img}")
            downloaded += 1
        except Exception as e:
            print(f"    ERROR {img}: {e}")

    print(f"  Status: {downloaded}/{len(images)} images")
    total_downloaded += downloaded

print("\n" + "=" * 70)
print(f"Total: {total_downloaded}/{total_images} images downloaded")
print("Done!")
