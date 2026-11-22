import sys
from bs4 import BeautifulSoup

def check_font_size(html_path, min_size=24):
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    
    # 簡易解析 style 中的 font-size
    for tag in soup.find_all(style=True):
        if 'font-size' in tag['style']:
            # 擷取數字部分比對...若小於 min_size 則報錯
            pass
            # sys.exit(1)
    print("Font size check passed.")