import get_wikipedia_text
import json
import re
import spacy
import collections


def detect_region_inflection(text, lexicon_inflection, uk_count, us_count):

    for entry in lexicon_inflection:
        uk = entry['uk'].lower()
        us = entry['us'].lower()

        if uk and re.search(rf"\b{re.escape(uk)}\b", text):
            uk_count += 1
            print("DEBUG: matched inflection UK:", uk)
        if us and re.search(rf"\b{re.escape(us)}\b", text):
            us_count += 1
            print("DEBUG: matched inflection US:", us)

    print(f"DEBUG: after inflection detection, uk_count={uk_count}, us_count={us_count}")
    return uk_count, us_count


def detect_region_phrase(text, lexicon_phrase, uk_count, us_count):

    for entry in lexicon_phrase:
        uk = entry['uk'].lower()
        us = entry['us'].lower()

        if uk and re.search(rf"\b{re.escape(uk)}\b", text):
            uk_count += 1
            print("DEBUG: matched phrase UK:", uk)
        if us and re.search(rf"\b{re.escape(us)}\b", text):
            us_count += 1
            print("DEBUG: matched phrase US:", us)

    print(f"DEBUG: after phrase detection, uk_count={uk_count}, us_count={us_count}")
    return uk_count, us_count


# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

def detect_region_with_spacy(text, lexicon_root, uk_count, us_count):

    doc = nlp(text)
    lemmas = [token.lemma_ for token in doc]
    dict_counter = collections.Counter(lemmas)

    for entry in lexicon_root:
        uk_root = entry['uk'].lower() if entry['uk'] else None
        us_root = entry['us'].lower() if entry['us'] else None

        if uk_root and uk_root in dict_counter.keys():
            uk_count += dict_counter[uk_root]
            print(f"DEBUG: found UK root: {uk_root}")
        if us_root and us_root in dict_counter.keys():
            us_count += dict_counter[us_root]
            print(f"DEBUG: found US root: {us_root}")
    print(f"DEBUG: after root detection, uk_count={uk_count}, us_count={us_count}")
    total = uk_count + us_count

    return {
        "uk_count": uk_count,
        "us_count": us_count,
        "total": total,
        "uk_percentage": (uk_count / total * 100) if total > 0 else 0,
        "us_percentage": (us_count / total * 100) if total > 0 else 0
    }


if __name__ == "__main__":
    
    # Fetch a text from Wikipedia
    ariticle = get_wikipedia_text.fetch_wikipedia_article()
    text = ariticle['content']
    text = text.lower()
    print(f"DEBUG: fetched content: {text[:100]}...")
    
    uk_count = 0
    us_count = 0

    # Load lexicon for inflections from JSON file
    with open('lexicon_us_uk - inflection.json', 'r', encoding='utf-8') as f:
        lexicon_inflection = json.load(f)

    uk_count, us_count = detect_region_inflection(text, lexicon_inflection, uk_count, us_count)

    # Load lexicon for phrases from JSON file
    with open('lexicon_us_uk - phrase.json', 'r', encoding='utf-8') as f:
        lexicon_phrase = json.load(f)

    uk_count, us_count = detect_region_phrase(text, lexicon_phrase, uk_count, us_count)

    # Load lexicon for roots from JSON file
    with open('lexicon_us_uk - root.json', 'r', encoding='utf-8') as f:
        lexicon_root = json.load(f)

    result = detect_region_with_spacy(text, lexicon_root, uk_count, us_count)
    print("Final detection result:", result)
