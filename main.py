from make_json_file import make_json_file
from get_wikipedia_text import fetch_wikipedia_article
from load_text_file import load_text_from_txt
from load_pdf_file import load_text_from_pdf
from detect_region import detect_region_inflection, detect_region_phrase, detect_region_with_spacy
import visualise
import json

csv_file = "lexicon - raw data.csv"

# Generate JSON files from CSV
result = make_json_file(csv_file)
print(result)

# Fetch a text from Wikipedia/txt/pdf
print("DEBUG: asking for input now")

link_or_file = input("Enter a URL of an article on Wikipedia or a path to a local text or PDF file: ").strip()
print("DEBUG: user gave:", link_or_file)

if link_or_file.lower().endswith('.txt'):
    text = load_text_from_txt(link_or_file)
elif link_or_file.lower().endswith('.pdf'):
    text = load_text_from_pdf(link_or_file)
else:
    page_link = link_or_file
    article = fetch_wikipedia_article(page_link)
    text = article['content']

text = text.lower()
print(f"DEBUG: fetched content: {text[:100]}...")

uk_count = 0
name_count = 0
us_count = 0
can_count = 0
austral_count = 0
nz_count = 0
scot_count = 0
irish_count = 0
ind_count = 0
eafr_count = 0
wafr_count = 0
safr_count = 0
welsh_count = 0
neng_count = 0
easi_count = 0
wasi_count = 0
sasi_count = 0
seasi_count = 0

# Load lexicon for inflections from JSON file
with open('lexicon - inflection.json', 'r', encoding='utf-8') as f:
    lexicon_inflection = json.load(f)

uk_count, name_count, us_count, can_count, austral_count, nz_count, scot_count, irish_count, ind_count, eafr_count, wafr_count, safr_count, welsh_count, neng_count, easi_count, wasi_count, sasi_count, seasi_count = detect_region_inflection(text, lexicon_inflection, uk_count, name_count, us_count, can_count, austral_count, nz_count, scot_count, irish_count, ind_count, eafr_count, wafr_count, safr_count, welsh_count, neng_count, easi_count, wasi_count, sasi_count, seasi_count)

# Load lexicon for phrases from JSON file
with open('lexicon - phrase.json', 'r', encoding='utf-8') as f:
    lexicon_phrase = json.load(f)

uk_count, name_count, us_count, can_count, austral_count, nz_count, scot_count, irish_count, ind_count, eafr_count, wafr_count, safr_count, welsh_count, neng_count, easi_count, wasi_count, sasi_count, seasi_count = detect_region_phrase(text, lexicon_phrase, uk_count, name_count, us_count, can_count, austral_count, nz_count, scot_count, irish_count, ind_count, eafr_count, wafr_count, safr_count, welsh_count, neng_count, easi_count, wasi_count, sasi_count, seasi_count)

# Load lexicon for roots from JSON file
with open('lexicon - root.json', 'r', encoding='utf-8') as f:
    lexicon_root = json.load(f)

result = detect_region_with_spacy(text, lexicon_root, uk_count, name_count, us_count, can_count, austral_count, nz_count, scot_count, irish_count, ind_count, eafr_count, wafr_count, safr_count, welsh_count, neng_count, easi_count, wasi_count, sasi_count, seasi_count)

image_path = visualise.plot_region_bar(result)

print("Final detection result:", result)
print(f"Bar chart saved to: {image_path}")
