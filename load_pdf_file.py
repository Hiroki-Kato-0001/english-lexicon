from pypdf import PdfReader
from pdf2image import convert_from_path
import pytesseract

def load_text_from_pdf(path):
    reader = PdfReader(path)
    text = ""
    
    for page in reader.pages:
        text += page.extract_text() + "\n"
    
    if text.strip():
        print("DEBUG: text extracted from PDF using pypdf")
        return text
    
    # Fallback to OCR if text extraction fails
    print("DEBUG: No text found, running OCR")

    images = convert_from_path(path)
    text = ""

    for image in images:
        text += pytesseract.image_to_string(image, lang="eng") + "\n"

    return text