# -*- coding: utf-8 -*-
import subprocess
import sys

# All 17 products
products = [
    # Pushhpull series (7)
    ('https://gateman.kr/gm_900s', 'gm-900s', 'GM-900S'),
    ('https://gateman.kr/gm_500s', 'gm-500s', 'GM-500S'),
    ('https://gateman.kr/gm_1000l', 'gm-1000l', 'GM-1000L'),
    ('https://gateman.kr/gp_900d', 'gp-900d', 'GP-900D'),
    ('https://gateman.kr/gp_700d', 'gp-700d', 'GP-700D'),
    ('https://gateman.kr/gp_500r', 'gp-500r', 'GP-500R'),
    ('https://gateman.kr/gp_300un', 'gp-300un', 'GP-300UN'),

    # Mortise series (10)
    ('https://gateman.kr/g_grab_touch', 'g-grab-touch', 'G-GRAB touch'),
    ('https://gateman.kr/grab100_fh', 'grab100-fh', 'G-GRAB scan+'),
    ('https://gateman.kr/gl_200h', 'gl-200h', 'GL-200H'),
    ('https://gateman.kr/gr_20', 'gr-20', 'GR-20'),
    ('https://gateman.kr/gr_sash', 'gr-sash', 'GR-SASH'),
    ('https://gateman.kr/gr_clip', 'gr-clip', 'GR-CLIP'),
    ('https://gateman.kr/gr_frame', 'gr-frame', 'GR-FRAME'),
    ('https://gateman.kr/g_touch', 'g-touch', 'G-TOUCH'),
    ('https://gateman.kr/g_suit_touch', 'g-suit-touch', 'G-SUIT touch'),
    ('https://gateman.kr/g_click_scan', 'g-click-scan', 'G-CLICK scan'),
]

print(f"Recreating {len(products)} products with custom header/footer...")
print("=" * 70)

success_count = 0
failed = []

for url, slug, name in products:
    print(f"\n[{success_count + 1}/{len(products)}] {name}")
    print(f"  URL: {url}")

    # Run create_product_with_custom_header.py
    result = subprocess.run(
        ['python', 'create_product_with_custom_header.py', url, slug, name],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"  SUCCESS")
        success_count += 1
    else:
        print(f"  FAILED: {result.stderr}")
        failed.append((name, result.stderr))

print("\n" + "=" * 70)
print(f"Summary: {success_count}/{len(products)} products created successfully")

if failed:
    print(f"\nFailed products ({len(failed)}):")
    for name, error in failed:
        print(f"  - {name}: {error[:100]}")
else:
    print("\nAll products created successfully!")
