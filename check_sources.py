import re
import sys

def check_sources(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if file_path.endswith('.md'):
        # 逐頁稿階段：檢查是否有標準 標籤
        citations = re.findall(r'\', content)
        if not citations:
            print(f"Failed: {file_path} 缺乏 出處標籤！")
            sys.exit(1)
        print(f"Passed: {file_path} 偵測到 {len(citations)} 處引用。")

    elif file_path.endswith('.html'):
        # 渲染階段：檢查每個 .slide 區塊內是否都有保留 <!-- cite: x --> 註解
        slides = re.findall(r'<div class="slide"[^>]*>(.*?)</div>\s*(?=<div class="slide"|</body>)', content, re.DOTALL)
        for idx, slide_html in enumerate(slides, 1):
            if not re.search(r'<!--\s*cite:\s*\d+.*?-->', slide_html):
                print(f"Failed: {file_path} 第 {idx} 頁遺失隱藏出處註解！")
                sys.exit(1)
        print(f"Passed: {file_path} 共 {len(slides)} 頁皆完整保留出處註解。")

if __name__ == "__main__":
    check_sources(sys.argv[1])
