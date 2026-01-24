from make_json_file import make_json_file
from get_wikipedia_text import fetch_wikipedia_article
from detect_region import detect_region_inflection, detect_region_phrase, detect_region_with_spacy
import json

csv_file = "lexicon_us_uk - raw data.csv"

# Generate JSON files from CSV
result = make_json_file(csv_file)
print(result)

# Fetch a text from Wikipedia
article = fetch_wikipedia_article()
text = article['content']
text = text.lower()
print(f"DEBUG: fetched content: {text[:100]}...")

brit_count = 0
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
nafr_count = 0
neng_count = 0
easi_count = 0
wasi_count = 0
sasi_count = 0
nasi_count = 0

# Load lexicon for inflections from JSON file
with open('lexicon_us_uk - inflection.json', 'r', encoding='utf-8') as f:
    lexicon_inflection = json.load(f)

brit_count, name_count, us_count, can_count, austral_count, nz_count, scot_count, irish_count, ind_count, eafr_count, wafr_count, safr_count, nafr_count, neng_count, easi_count, wasi_count, sasi_count, nasi_count = detect_region_inflection(text, lexicon_inflection, brit_count, name_count, us_count, can_count, austral_count, nz_count, scot_count, irish_count, ind_count, eafr_count, wafr_count, safr_count, nafr_count, neng_count, easi_count, wasi_count, sasi_count, nasi_count)

# Load lexicon for phrases from JSON file
with open('lexicon_us_uk - phrase.json', 'r', encoding='utf-8') as f:
    lexicon_phrase = json.load(f)

brit_count, name_count, us_count, can_count, austral_count, nz_count, scot_count, irish_count, ind_count, eafr_count, wafr_count, safr_count, nafr_count, neng_count, easi_count, wasi_count, sasi_count, nasi_count = detect_region_phrase(text, lexicon_phrase, brit_count, name_count, us_count, can_count, austral_count, nz_count, scot_count, irish_count, ind_count, eafr_count, wafr_count, safr_count, nafr_count, neng_count, easi_count, wasi_count, sasi_count, nasi_count)

# Load lexicon for roots from JSON file
with open('lexicon_us_uk - root.json', 'r', encoding='utf-8') as f:
    lexicon_root = json.load(f)

result = detect_region_with_spacy(text, lexicon_root, brit_count, name_count, us_count, can_count, austral_count, nz_count, scot_count, irish_count, ind_count, eafr_count, wafr_count, safr_count, nafr_count, neng_count, easi_count, wasi_count, sasi_count, nasi_count)
print("Final detection result:", result)
