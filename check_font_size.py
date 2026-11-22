import re
import sys
from bs4 import BeautifulSoup

def check_font_size(html_path, min_size=24):
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    violations = []

    # 1. 解析 <style> 標籤內的 CSS 規則
    for style_tag in soup.find_all('style'):
        css_text = style_tag.string or ""
        # 尋找選擇器與對應的 font-size
        rules = re.findall(r'([^{]+)\{([^}]+)\}', css_text)
        for selector, body in rules:
            font_matches = re.findall(r'font-size\s*:\s*(\d+)px', body)
            for size_str in font_matches:
                size = int(size_str)
                if size < min_size:
                    violations.append(f"CSS 選擇器 '{selector.strip()}' 字體為 {size}px (低於 {min_size}px)")

    # 2. 檢查任何直接寫在標籤上的 inline style
    for tag in soup.find_all(style=True):
        font_matches = re.findall(r'font-size\s*:\s*(\d+)px', tag['style'])
        for size_str in font_matches:
            size = int(size_str)
            if size < min_size:
                violations.append(f"標籤 <{tag.name}> 行內字體為 {size}px (低於 {min_size}px)")

    if violations:
        print(f"Failed: {html_path} 發現 {len(violations)} 處字體過小：")
        for v in violations:
            print(f"  - {v}")
        sys.exit(1)

    print(f"Passed: {html_path} 所有定義字體皆 >= {min_size}px。")

if __name__ == "__main__":
    check_font_size(sys.argv[1])
