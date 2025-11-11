# -*- coding: utf-8 -*-
import urllib.request
import re

# Download official page
headers = {'User-Agent': 'Mozilla/5.0'}
req = urllib.request.Request('https://gateman.kr/g_grab_touch', headers=headers)

with urllib.request.urlopen(req, timeout=30) as response:
    html = response.read().decode('utf-8')

# Find all CSS link tags
css_links = re.findall(r'<link[^>]+stylesheet[^>]*>', html, re.IGNORECASE)

print(f'Total CSS links: {len(css_links)}')
print('\nCSS Files:')
for i, link in enumerate(css_links):
    href_match = re.search(r'href=[\"\']([^\"\']+)', link)
    if href_match:
        href = href_match.group(1)
        if not href.startswith('http'):
            href = 'https://gateman.kr' + href
        print(f'  {i+1}. {href}')

# Find inline style blocks
style_blocks = re.findall(r'<style[^>]*>.*?</style>', html, re.DOTALL | re.IGNORECASE)
print(f'\nInline style blocks: {len(style_blocks)}')
for i, block in enumerate(style_blocks):
    size = len(block)
    print(f'  Block {i+1}: {size} characters')
