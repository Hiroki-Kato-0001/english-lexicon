from pypdf import PdfReader
from pdf2image import convert_from_path
import pytesseract

def load_text_from_pdf(path):
    reader = PdfReader(path)
    images = convert_from_path(path)

    text = ""

    for i, page in enumerate(reader.pages):
        page_text = page.extract_text()

        if page_text and len(page_text) > 50:
            print(f"DEBUG: page {i+1} extracted using pypdf")
            text += page_text
        else:
            print(f"DEBUG: page {i+1} using OCR")
            ocr_text = pytesseract.image_to_string(images[i], lang="eng")
            text += ocr_text

    text = text.replace('\n', ' ')
    
    print(f"Total extracted text length: {len(text)} characters")

    return text
