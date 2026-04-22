import re

def load_text_from_txt(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
        text = re.sub('\n', ' ', text)
        text = re.sub('\s+', ' ', text)
        text = text.lower()
        text = text.strip()

        print(f"Total extracted text length: {len(text)} characters")

        return text