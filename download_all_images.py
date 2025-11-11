import subprocess

# Products with successful HTML generation
products = [
    "gm_500s",
    "gp_900d",
    "gp_700d",
    "gp_500r",
    "gm_1000l",
    "gp_300un"
]

print("Downloading images for all products...")
print("=" * 60)

for idx, url_slug in enumerate(products, 1):
    print(f"\n[{idx}/{len(products)}] {url_slug.upper()}")
    print("-" * 60)

    try:
        result = subprocess.run(
            ["python", "download_product_images.py", url_slug],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore',
            timeout=120
        )
        print(result.stdout)
    except Exception as e:
        print(f"ERROR: {e}")

print("\n" + "=" * 60)
print("All images downloaded!")
print("=" * 60)
