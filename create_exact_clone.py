# -*- coding: utf-8 -*-
import re
import sys
import urllib.request

def create_exact_clone(url, product_slug):
    """Create exact clone of official page with minimal changes"""

    output_file = f'products/{product_slug}.html'

    print(f"Cloning {url}...")
    print(f"  Output: {output_file}")

    # Download HTML
    headers = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            html = response.read().decode('utf-8')
        print(f"  Downloaded: {len(html)} bytes")
    except Exception as e:
        print(f"ERROR downloading: {e}")
        return False

    # Fix all relative URLs to absolute URLs
    # Fix CSS links
    html = re.sub(r'href="/', r'href="https://gateman.kr/', html)
    html = re.sub(r'href=\'/', r'href=\'https://gateman.kr/', html)

    # Fix script src
    html = re.sub(r'src="/', r'src="https://gateman.kr/', html)
    html = re.sub(r'src=\'/', r'src=\'https://gateman.kr/', html)

    # Fix background images in CSS
    html = re.sub(r'url\(/common/', r'url(https://gateman.kr/common/', html)
    html = re.sub(r'url\(/files/', r'url(https://gateman.kr/files/', html)

    # Replace phone numbers
    html = html.replace('1577-1919', '010-6633-7732')
    html = html.replace('1544-3232', '010-6633-7732')

    # Replace YouTube iframes with clickable thumbnails
    def youtube_replacer(match):
        video_id = match.group(1)
        return f'''<a href="https://www.youtube.com/watch?v={video_id}" target="_blank" style="display:block;position:relative;padding-bottom:56.25%;height:0;overflow:hidden;max-width:100%;">
    <img src="https://img.youtube.com/vi/{video_id}/maxresdefault.jpg" alt="YouTube video" style="position:absolute;top:0;left:0;width:100%;height:100%;object-fit:cover;">
    <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:80px;height:56px;background:rgba(255,0,0,0.9);border-radius:12px;cursor:pointer;">
        <svg viewBox="0 0 68 48" style="width:100%;height:100%;"><path d="M66.52 7.74c-.78-2.93-2.49-5.41-5.42-6.19C55.79.13 34 0 34 0S12.21.13 6.9 1.55c-2.93.78-4.63 3.26-5.42 6.19C.06 13.05 0 24 0 24s.06 10.95 1.48 16.26c.78 2.93 2.49 5.41 5.42 6.19C12.21 47.87 34 48 34 48s21.79-.13 27.1-1.55c2.93-.78 4.64-3.26 5.42-6.19C67.94 34.95 68 24 68 24s-.06-10.95-1.48-16.26z" fill="white"></path><path d="M45 24L27 14v20" fill="#FF0000"></path></svg>
    </div>
</a>'''

    html = re.sub(
        r'<iframe[^>]+src="https://www\.youtube\.com/embed/([^"?]+)[^"]*"[^>]*></iframe>',
        youtube_replacer,
        html,
        flags=re.IGNORECASE
    )

    # Replace image URLs to use local paths (only for product-specific images)
    # Extract product folder name from URL
    url_parts = url.rstrip('/').split('/')
    product_folder = url_parts[-1]

    # Replace product-specific image paths
    html = re.sub(
        r'src="?/common/img/smartdoorlock/gateman/' + product_folder + r'/([^"\s]+)"?',
        r'src="../images/products/' + product_folder.replace('_', '') + r'/\1"',
        html
    )

    # Keep common images pointing to gateman.kr
    # (They're already using absolute paths like /common/img/commonNew/ or https://gateman.kr/...)

    # No banner - keep it clean and identical to official site

    # Write output
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"SUCCESS: Created {output_file} ({len(html)} bytes)")
        return True
    except Exception as e:
        print(f"ERROR writing file: {e}")
        return False

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python create_exact_clone.py <url> <product_slug>")
        print("Example: python create_exact_clone.py https://gateman.kr/g_suit_touch g-suit-touch")
        sys.exit(1)

    url = sys.argv[1]
    product_slug = sys.argv[2]

    success = create_exact_clone(url, product_slug)
    sys.exit(0 if success else 1)
