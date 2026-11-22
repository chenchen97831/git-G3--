import os, sys

def check_word_count(draft_path, max_words=100):
    with open(draft_path, 'r', encoding='utf-8') as f:
        text = f.read()
    word_count = len(text.replace(" ", "").replace("\n", ""))
    if word_count > max_words:
        print(f"Error: {draft_path} 字數超標 ({word_count}/{max_words})")
        sys.exit(1) # 報錯，觸發精準退回
    print("Word count check passed.")