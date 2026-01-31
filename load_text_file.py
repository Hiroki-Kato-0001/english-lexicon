def load_text_from_txt(path):
    with open(path, 'r', encoding='utf-8') as f:
        text =  f.read()
        text = text.replace('\n', ' ')
        return text