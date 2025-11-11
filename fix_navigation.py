# -*- coding: utf-8 -*-
import re
import sys

def fix_navigation(filename):
    """Remove product navigation from HTML file"""

    print(f"Fixing {filename}...")

    # Read file
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Add CSS to hide navigation
    if '.prod-nav, .m-prod-nav { display: none !important; }' not in html:
        html = html.replace(
            '        /* Page content spacing */\n        .page-content { margin-top: 80px; }',
            '''        /* Page content spacing */
        .page-content { margin-top: 80px; }

        /* Hide product navigation */
        .prod-nav, .m-prod-nav { display: none !important; }'''
        )
        print(f"  Added CSS to hide navigation")

    # Remove navigation HTML (from prod-nav to before prod4-section1 or prod-curvy-sec1)
    pattern = r'(<div class="prod-section prod-view[^>]*>).*?(<div class="prod[^"]*-section1 prod-curvy-sec1">)'

    if re.search(pattern, html, re.DOTALL):
        html = re.sub(
            pattern,
            r'\1\n\2',
            html,
            flags=re.DOTALL
        )
        print(f"  Removed navigation HTML")
    else:
        print(f"  Navigation HTML not found or already removed")

    # Write file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"  SUCCESS: {filename} updated")

if __name__ == '__main__':
    files = [
        'products/g-grab-touch.html',
        'products/g-suit-touch.html',
        'products/g-click-scan.html'
    ]

    for filename in files:
        try:
            fix_navigation(filename)
        except Exception as e:
            print(f"  ERROR: {e}")
        print()

    print("All files processed!")
