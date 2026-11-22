import re
import sys

def check_word_count(draft_path, max_words=50, max_sentences=3):
    with open(draft_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. 移除出處標籤 與 Markdown 粗體符號 **
    clean_text = re.sub(r'\[cite:[^\]]+\]', '', text)
    clean_text = clean_text.replace('**', '').strip()

    # 2. 計算句子數量 (以句號、驚嘆號、問號切分)
    sentences = [s for s in re.split(r'[。！？]', clean_text) if s.strip()]
    if len(sentences) > max_sentences:
        print(f"Failed: {draft_path} 句數超標 ({len(sentences)}/{max_sentences} 句)")
        sys.exit(1)

    # 3. 計算純文字字數 (排除空白、換行與常見全形標點)
    pure_words = re.sub(r'[\s，。！？、「」『』（）—…：；]', '', clean_text)
    word_count = len(pure_words)

    if word_count > max_words:
        print(f"Failed: {draft_path} 字數超標 ({word_count}/{max_words} 字)")
        sys.exit(1)

    print(f"Passed: {draft_path} (字數: {word_count}/{max_words}, 句數: {len(sentences)}/{max_sentences})")

if __name__ == "__main__":
    check_word_count(sys.argv[1])
