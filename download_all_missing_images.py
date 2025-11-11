# -*- coding: utf-8 -*-
import re
import urllib.request
import os
import time

# All products with their slugs (matching HTML filenames and image folders)
products = [
    ('gm-900s', 'gm_900s'),       # HTML: gm-900s.html, Images: gm_900s
    ('gm-500s', 'gm_500s'),
    ('gm-1000l', 'gm_1000l'),
    ('gp-900d', 'gp_900d'),
    ('gp-700d', 'gp_700d'),
    ('gp-500r', 'gp_500r'),
    ('gp-300un', 'gp_300un'),
    ('g-grab-touch', 'g_grab_touch'),
    ('grab100-fh', 'grab100_fh'),
    ('gl-200h', 'gl_200h'),
    ('gr-20', 'gr_20'),
    ('gr-sash', 'gr_sash'),
    ('gr-clip', 'gr_clip'),
    ('gr-frame', 'gr_frame'),
    ('g-touch', 'g_touch'),
    ('g-suit-touch', 'g_suit_touch'),
    ('g-click-scan', 'g_click_scan'),
]

print("Scanning all product pages for missing images...")
print("=" * 70)

total_images = 0
total_downloaded = 0
total_skipped = 0
total_errors = 0

headers = {'User-Agent': 'Mozilla/5.0'}

for html_slug, img_slug in products:
    # HTML file uses hyphen, image folder uses underscore
    html_file = f'products/{html_slug}.html'

    if not os.path.exists(html_file):
        print(f"\nSkipping {html_slug} (file not found)")
        continue

    print(f"\n{'='*70}")
    print(f"Processing: {html_slug} (images: {img_slug})")
    print(f"{'='*70}")

    # Read HTML
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find all local image references
    img_pattern = rf'src=\"\.\./images/products/{img_slug}/([^\"]+)\"'
    images = list(set(re.findall(img_pattern, html)))
    images.sort()

    if not images:
        print(f"  No images found")
        continue

    print(f"  Found {len(images)} unique images")

    # Create directory
    img_dir = f'images/products/{img_slug}'
    os.makedirs(img_dir, exist_ok=True)

    base_url = f'https://gateman.kr/common/img/smartdoorlock/gateman/{img_slug}/'

    downloaded = 0
    skipped = 0
    errors = 0

    for img in images:
        filepath = f'{img_dir}/{img}'

        if os.path.exists(filepath):
            print(f"  Skip {img} (exists)")
            skipped += 1
            continue

        url = base_url + img
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as response:
                with open(filepath, 'wb') as f:
                    f.write(response.read())
            print(f"  Downloaded {img}")
            downloaded += 1
            time.sleep(0.1)  # Be nice to the server
        except Exception as e:
            print(f"  ERROR {img}: {str(e)[:50]}")
            errors += 1

    total_images += len(images)
    total_downloaded += downloaded
    total_skipped += skipped
    total_errors += errors

    print(f"  Summary: {downloaded} downloaded, {skipped} skipped, {errors} errors")

print("\n" + "=" * 70)
print("FINAL SUMMARY")
print("=" * 70)
print(f"Total images: {total_images}")
print(f"Downloaded: {total_downloaded}")
print(f"Skipped (already exist): {total_skipped}")
print(f"Errors: {total_errors}")
print(f"Success rate: {((total_downloaded + total_skipped) / total_images * 100):.1f}%")
