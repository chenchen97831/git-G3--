import re, sys

WHITELIST_DOMAINS = ["wikimedia.org", "gov.tw"]

def check_links(html_path):
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    urls = re.findall(r'href="([^"]+)"|src="([^"]+)"', content)
    for url_tuple in urls:
        url = url_tuple[0] or url_tuple[1]
        if url.startswith('http') and not any(domain in url for domain in WHITELIST_DOMAINS):
            print(f"Error: 偵測到非白名單外部連結 {url}")
            sys.exit(1)
    print("External links check passed.")