import subprocess
import os

# Successfully downloaded products
products = [
    ("gm_500s", "GM-500S"),
    ("gp_900d", "GP-900D"),
    ("gp_700d", "GP-700D"),
    ("gp_500r", "GP-500R"),
    ("g_grab_touch", "G-GRAB touch"),
    ("gm_1000l", "GM-1000L"),
    ("gl_200h", "GL-200H"),
    ("gr_20", "GR-20"),
    ("gr_sash", "GR-SASH"),
    ("gr_clip", "GR-CLIP"),
    ("gr_frame", "GR-FRAME"),
    ("g_touch", "G-TOUCH"),
    ("gp_300un", "GP-300UN")
]

print("=" * 60)
print("Generating all product pages...")
print("=" * 60)

for idx, (url_slug, product_name) in enumerate(products, 1):
    print(f"\n[{idx}/{len(products)}] {product_name}")
    print("-" * 60)

    try:
        result = subprocess.run(
            ["python", "create_product_page.py", url_slug, product_name],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore'
        )

        print(result.stdout)
        if result.returncode != 0:
            print("ERROR:", result.stderr)

    except Exception as e:
        print(f"ERROR: {e}")

print("\n" + "=" * 60)
print("All pages generated!")
print("=" * 60)
