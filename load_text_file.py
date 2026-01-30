def load_text_from_txt(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()