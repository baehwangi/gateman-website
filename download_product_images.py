import sys
import re
import os
import urllib.request

if len(sys.argv) < 2:
    print("Usage: python download_product_images.py <url_slug>")
    sys.exit(1)

url_slug = sys.argv[1]
source_file = f"{url_slug}_source.html"
image_dir = f"images/products/{url_slug}"

print(f"Downloading images for {url_slug}...")

# Create directory
os.makedirs(image_dir, exist_ok=True)

# Read source
try:
    with open(source_file, 'r', encoding='utf-8') as f:
        source = f.read()
except FileNotFoundError:
    print(f"ERROR: {source_file} not found!")
    sys.exit(1)

# Find all images
base_pattern = f'https://gateman.kr/common/img/smartdoorlock/gateman/{url_slug}/'
access_pattern = 'https://gateman.kr/common/img/access/'

img_urls = re.findall(rf'{base_pattern}([^"\'\s)]+\.(?:png|jpg|jpeg|gif))', source, re.IGNORECASE)
access_urls = re.findall(rf'{access_pattern}([^"\'\s)]+\.(?:png|jpg|jpeg|gif))', source, re.IGNORECASE)

all_images = set(img_urls + access_urls)
print(f"Found {len(all_images)} images")

headers = {'User-Agent': 'Mozilla/5.0'}
downloaded = 0

for filename in sorted(all_images):
    filepath = os.path.join(image_dir, filename)
    if os.path.exists(filepath):
        continue

    # Try product folder first
    url = f'{base_pattern}{filename}'
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

    # Try access folder
    url = f'{access_pattern}{filename}'
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            with open(filepath, 'wb') as f:
                f.write(response.read())
        downloaded += 1
        print(f"  OK: {filename} (access)")
    except Exception as e:
        print(f"  SKIP: {filename}")

print(f"Downloaded: {downloaded}")
