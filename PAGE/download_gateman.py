import urllib.request

# Download gateman.kr homepage
url = 'https://gateman.kr/'
response = urllib.request.urlopen(url)
html_content = response.read().decode('utf-8')

# Save to file
with open('gateman_original.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Downloaded successfully!")