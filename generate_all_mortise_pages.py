import subprocess

# Mortise products (simple layout)
products = [
    ("gl_200h", "GL-200H"),
    ("grab100_fh", "G-GRAB scan+"),
    ("g_grab_touch", "G-GRAB touch"),
    ("gr_20", "GR-20"),
    ("gr_sash", "GR-SASH"),
    ("gr_clip", "GR-CLIP"),
    ("gr_frame", "GR-FRAME"),
    ("g_touch", "G-TOUCH")
]

print("=" * 60)
print("Generating all mortise product pages...")
print("=" * 60)

for idx, (url_slug, product_name) in enumerate(products, 1):
    print(f"\n[{idx}/{len(products)}] {product_name}")
    print("-" * 60)

    try:
        result = subprocess.run(
            ["python", "create_simple_product_page.py", url_slug, product_name],
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
print("All mortise pages generated!")
print("=" * 60)
