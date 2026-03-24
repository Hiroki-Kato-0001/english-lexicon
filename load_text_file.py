def load_text_from_txt(path):
    with open(path, 'r', encoding='utf-8') as f:
        text =  f.read()
        text = text.replace('\n', ' ')

        print(f"Total extracted text length: {len(text)} characters")

        return text