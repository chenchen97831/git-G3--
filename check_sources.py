import re, sys

def check_sources_exist(draft_path):
    with open(draft_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # 檢查每一段或每一頁是否有
    citations = re.findall(r'\', text)
    if not citations:
        print(f"Error: {draft_path} 缺乏出處標籤，涉嫌自行發明內容！")
        sys.exit(1)
    # (進階：可加入比對 cite 標籤是否真實存在於 cards/ 裡)
    print("Source check passed.")