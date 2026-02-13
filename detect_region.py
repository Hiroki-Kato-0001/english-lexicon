import re
import spacy
import collections
import matplotlib.pyplot as plt

def detect_region_inflection(text, lexicon_inflection, uk_count, name_count, us_count, can_count, austral_count,
                             nz_count, scot_count, irish_count, ind_count, eafr_count, wafr_count, safr_count,
                             welsh_count, neng_count, easi_count, wasi_count, sasi_count, seasi_count):

    for entry in lexicon_inflection:
        #uk = entry['United Kingdom'].lower() if entry['United Kingdom'] else None
        #name = entry['North America'].lower() if entry['North America'] else None
        #us = entry['United States'].lower() if entry['United States'] else None
        #can = entry['Canada'].lower() if entry['Canada'] else None
        #austral = entry['Australia'].lower() if entry['Australia'] else None
        #nz = entry['New Zealand'].lower() if entry['New Zealand'] else None
        #scot = entry['Scotland'].lower() if entry['Scotland'] else None
        #irish = entry['Ireland'].lower() if entry['Ireland'] else None
        #ind = entry['India'].lower() if entry['India'] else None
        #eafr = entry['East Africa'].lower() if entry['East Africa'] else None
        #wafr = entry['West Africa'].lower() if entry['West Africa'] else None
        #safr = entry['South Africa'].lower() if entry['South Africa'] else None
        #welsh = entry['Wales'].lower() if entry['Wales'] else None
        #neng = entry['New England'].lower() if entry['New England'] else None
        #easi = entry['East Asia'].lower() if entry['East Asia'] else None
        #wasi = entry['West Asia'].lower() if entry['West Asia'] else None
        #sasi = entry['South Asia'].lower() if entry['South Asia'] else None
        #seasi = entry['South-East Asia'].lower() if entry['South-East Asia'] else None

        if entry['region'] == "United Kingdom" and re.search(rf"\b{re.escape(entry['word'])}\b", text):
            uk_count += 1
            print("DEBUG: matched inflection United Kingdom:", entry['word'])
        if entry['region'] == "North America" and re.search(rf"\b{re.escape(entry['word'])}\b", text):
            name_count += 1
            print("DEBUG: matched inflection North America:", entry['word'])
        if entry['region'] == "United States" and re.search(rf"\b{re.escape(entry['word'])}\b", text):
            us_count += 1
            print("DEBUG: matched inflection US:", entry['word'])
        if entry['region'] == "Canada" and re.search(rf"\b{re.escape(entry['word'])}\b", text):
            can_count += 1
            print("DEBUG: matched inflection Canada:", entry['word'])
        if entry['region'] == "Australia" and re.search(rf"\b{re.escape(entry['word'])}\b", text):
            austral_count += 1
            print("DEBUG: matched inflection Australia:", entry['word'])
        if entry['region'] == "New Zealand" and re.search(rf"\b{re.escape(entry['word'])}\b", text):
            nz_count += 1
            print("DEBUG: matched inflection New Zealand:", entry['word'])
        if entry['region'] == "Scotland" and re.search(rf"\b{re.escape(entry['word'])}\b", text):
            scot_count += 1
            print("DEBUG: matched inflection Scotland:", entry['word'])
        if entry['region'] == "Ireland" and re.search(rf"\b{re.escape(entry['word'])}\b", text):
            irish_count += 1
            print("DEBUG: matched inflection Ireland:", entry['word'])
        if entry['region'] == "India" and re.search(rf"\b{re.escape(entry['word'])}\b", text):
            ind_count += 1
            print("DEBUG: matched inflection India:", entry['word'])
        if entry['region'] == "East Africa" and re.search(rf"\b{re.escape(entry['word'])}\b", text):
            eafr_count += 1
            print("DEBUG: matched inflection East Africa:", entry['word'])
        if entry['region'] == "West Africa" and re.search(rf"\b{re.escape(entry['word'])}\b", text):
            wafr_count += 1
            print("DEBUG: matched inflection West Africa:", entry['word'])
        if entry['region'] == "South Africa" and re.search(rf"\b{re.escape(entry['word'])}\b", text):
            safr_count += 1
            print("DEBUG: matched inflection South Africa:", entry['word'])
        if entry['region'] == "Wales" and re.search(rf"\b{re.escape(entry['word'])}\b", text):
            welsh_count += 1
            print("DEBUG: matched inflection Wales:", entry['word'])
        if entry['region'] == "New England" and re.search(rf"\b{re.escape(entry['word'])}\b", text):
            neng_count += 1
            print("DEBUG: matched inflection New England:", entry['word'])
        if entry['region'] == "East Asia" and re.search(rf"\b{re.escape(entry['word'])}\b", text):
            easi_count += 1
            print("DEBUG: matched inflection East Asia:", entry['word'])
        if entry['region'] == "West Asia" and re.search(rf"\b{re.escape(entry['word'])}\b", text):
            wasi_count += 1
            print("DEBUG: matched inflection West Asia:", entry['word'])
        if entry['region'] == "South Asia" and re.search(rf"\b{re.escape(entry['word'])}\b", text):
            sasi_count += 1
            print("DEBUG: matched inflection South Asia:", entry['word'])
        if entry['region'] == "South-East Asia" and re.search(rf"\b{re.escape(entry['word'])}\b", text):
            seasi_count += 1
            print("DEBUG: matched inflection South-East Asia:", entry['word'])

    print(f"DEBUG: after inflection detection, uk_count={uk_count}, name_count={name_count}, us_count={us_count}, can_count={can_count}, austral_count={austral_count}, nz_count={nz_count}, scot_count={scot_count}, irish_count={irish_count}, ind_count={ind_count}, eafr_count={eafr_count}, wafr_count={wafr_count}, safr_count={safr_count}, welsh_count={welsh_count}, neng_count={neng_count}, easi_count={easi_count}, wasi_count={wasi_count}, sasi_count={sasi_count}, seasi_count={seasi_count}")
    return uk_count, name_count, us_count, can_count, austral_count, nz_count, scot_count, irish_count, ind_count, eafr_count, wafr_count, safr_count, welsh_count, neng_count, easi_count, wasi_count, sasi_count, seasi_count


def detect_region_phrase(text, lexicon_phrase, uk_count, name_count, us_count, can_count, austral_count,
                             nz_count, scot_count, irish_count, ind_count, eafr_count, wafr_count, safr_count,
                             welsh_count, neng_count, easi_count, wasi_count, sasi_count, seasi_count):

    for entry in lexicon_phrase:
        #uk = entry['United Kingdom'].lower() if entry['United Kingdom'] else None
        #name = entry['North America'].lower() if entry['North America'] else None
        #us = entry['United States'].lower() if entry['United States'] else None
        #can = entry['Canada'].lower() if entry['Canada'] else None
        #austral = entry['Australia'].lower() if entry['Australia'] else None
        #nz = entry['New Zealand'].lower() if entry['New Zealand'] else None
        #scot = entry['Scotland'].lower() if entry['Scotland'] else None
        #irish = entry['Ireland'].lower() if entry['Ireland'] else None
        #ind = entry['India'].lower() if entry['India'] else None
        #eafr = entry['East Africa'].lower() if entry['East Africa'] else None
        #wafr = entry['West Africa'].lower() if entry['West Africa'] else None
        #safr = entry['South Africa'].lower() if entry['South Africa'] else None
        #welsh = entry['Wales'].lower() if entry['Wales'] else None
        #neng = entry['New England'].lower() if entry['New England'] else None
        #easi = entry['East Asia'].lower() if entry['East Asia'] else None
        #wasi = entry['West Asia'].lower() if entry['West Asia'] else None
        #sasi = entry['South Asia'].lower() if entry['South Asia'] else None
        #seasi = entry['South-East Asia'].lower() if entry['South-East Asia'] else None

        if entry['region'] == "United Kingdom" and re.search(rf"\b{re.escape(entry['word'])}\b", text):
            uk_count += 1
            print("DEBUG: matched phrase United Kingdom:", entry['word'])
        if entry['region'] == "North America" and re.search(rf"\b{re.escape(entry['word'])}\b", text):
            name_count += 1
            print("DEBUG: matched phrase North America:", entry['word'])
        if entry['region'] == "United States" and re.search(rf"\b{re.escape(entry['word'])}\b", text):
            us_count += 1
            print("DEBUG: matched phrase United States:", entry['word'])
        if entry['region'] == "Canada" and re.search(rf"\b{re.escape(entry['word'])}\b", text):
            can_count += 1
            print("DEBUG: matched phrase Canada:", entry['word'])
        if entry['region'] == "Australia" and re.search(rf"\b{re.escape(entry['word'])}\b", text):
            austral_count += 1
            print("DEBUG: matched phrase Australia:", entry['word'])
        if entry['region'] == "New Zealand" and re.search(rf"\b{re.escape(entry['word'])}\b", text):
            nz_count += 1
            print("DEBUG: matched phrase New Zealand:", entry['word'])
        if entry['region'] == "Scotland" and re.search(rf"\b{re.escape(entry['word'])}\b", text):
            scot_count += 1
            print("DEBUG: matched phrase Scotland:", entry['word'])
        if entry['region'] == "Ireland" and re.search(rf"\b{re.escape(entry['word'])}\b", text):
            irish_count += 1
            print("DEBUG: matched phrase Ireland:", entry['word'])
        if entry['region'] == "India" and re.search(rf"\b{re.escape(entry['word'])}\b", text):
            ind_count += 1
            print("DEBUG: matched phrase India:", entry['word'])
        if entry['region'] == "East Africa" and re.search(rf"\b{re.escape(entry['word'])}\b", text):
            eafr_count += 1
            print("DEBUG: matched phrase East Africa:", entry['word'])
        if entry['region'] == "West Africa" and re.search(rf"\b{re.escape(entry['word'])}\b", text):
            wafr_count += 1
            print("DEBUG: matched phrase West Africa:", entry['word'])
        if entry['region'] == "South Africa" and re.search(rf"\b{re.escape(entry['word'])}\b", text):
            safr_count += 1
            print("DEBUG: matched phrase South Africa:", entry['word'])
        if entry['region'] == "Wales" and re.search(rf"\b{re.escape(entry['word'])}\b", text):
            welsh_count += 1
            print("DEBUG: matched phrase Wales:", entry['word'])
        if entry['region'] == "New England" and re.search(rf"\b{re.escape(entry['word'])}\b", text):
            neng_count += 1
            print("DEBUG: matched phrase New England:", entry['word'])
        if entry['region'] == "East Asia" and re.search(rf"\b{re.escape(entry['word'])}\b", text):
            easi_count += 1
            print("DEBUG: matched phrase East Asia:", entry['word'])
        if entry['region'] == "West Asia" and re.search(rf"\b{re.escape(entry['word'])}\b", text):
            wasi_count += 1
            print("DEBUG: matched phrase West Asia:", entry['word'])
        if entry['region'] == "South Asia" and re.search(rf"\b{re.escape(entry['word'])}\b", text):
            sasi_count += 1
            print("DEBUG: matched phrase South Asia:", entry['word'])
        if entry['region'] == "South-East Asia" and re.search(rf"\b{re.escape(entry['word'])}\b", text):
            seasi_count += 1
            print("DEBUG: matched phrase South-East Asia:", entry['word'])

    print(f"DEBUG: after phrase detection, uk_count={uk_count}, name_count={name_count}, us_count={us_count}, can_count={can_count}, austral_count={austral_count}, nz_count={nz_count}, scot_count={scot_count}, irish_count={irish_count}, ind_count={ind_count}, eafr_count={eafr_count}, wafr_count={wafr_count}, safr_count={safr_count}, welsh_count={welsh_count}, neng_count={neng_count}, easi_count={easi_count}, wasi_count={wasi_count}, sasi_count={sasi_count}, seasi_count={seasi_count}")
    return uk_count, name_count, us_count, can_count, austral_count, nz_count, scot_count, irish_count, ind_count, eafr_count, wafr_count, safr_count, welsh_count, neng_count, easi_count, wasi_count, sasi_count, seasi_count


# Load spaCy English model
nlp = spacy.load("en_core_web_sm")
nlp.max_length = 6000000  # Increase max length if needed

def detect_region_with_spacy(text, lexicon_root, uk_count, name_count, us_count, can_count, austral_count,
                             nz_count, scot_count, irish_count, ind_count, eafr_count, wafr_count, safr_count,
                             welsh_count, neng_count, easi_count, wasi_count, sasi_count, seasi_count):

    doc = nlp(text)
    lemmas = [token.lemma_ for token in doc]
    dict_counter = collections.Counter(lemmas)

    for entry in lexicon_root:
    

        if entry['region'] == "United Kingdom" and entry['word'] in dict_counter.keys():
            uk_count += dict_counter[entry['word']]
            print(f"DEBUG: matched root United Kingdom: {entry['word']}")
        if entry['region'] == "North America" and entry['word'] in dict_counter.keys():
            name_count += dict_counter[entry['word']]
            print(f"DEBUG: matched root North America: {entry['word']}")
        if entry['region'] == "United States" and entry['word'] in dict_counter.keys():
            us_count += dict_counter[entry['word']]
            print(f"DEBUG: matched root United States: {entry['word']}")
        if entry['region'] == "Canada" and entry['word'] in dict_counter.keys():
            can_count += dict_counter[entry['word']]
            print(f"DEBUG: matched root Canada: {entry['word']}")
        if entry['region'] == "Australia" and entry['word'] in dict_counter.keys():
            austral_count += dict_counter[entry['word']]
            print(f"DEBUG: matched root Australia: {entry['word']}")
        if entry['region'] == "New Zealand" and entry['word'] in dict_counter.keys():
            nz_count += dict_counter[entry['word']]
            print(f"DEBUG: matched root New Zealand: {entry['word']}")
        if entry['region'] == "Scotland" and entry['word'] in dict_counter.keys():
            scot_count += dict_counter[entry['word']]
            print(f"DEBUG: matched root Scotland: {entry['word']}")
        if entry['region'] == "Ireland" and entry['word'] in dict_counter.keys():
            irish_count += dict_counter[entry['word']]
            print(f"DEBUG: matched root Ireland: {entry['word']}")
        if entry['region'] == "India" and entry['word'] in dict_counter.keys():
            ind_count += dict_counter[entry['word']]
            print(f"DEBUG: matched root India: {entry['word']}")
        if entry['region'] == "East Africa" and entry['word'] in dict_counter.keys():
            eafr_count += dict_counter[entry['word']]
            print(f"DEBUG: matched root East Africa: {entry['word']}")
        if entry['region'] == "West Africa" and entry['word'] in dict_counter.keys():
            wafr_count += dict_counter[entry['word']]
            print(f"DEBUG: matched root West Africa: {entry['word']}")
        if entry['region'] == "South Africa" and entry['word'] in dict_counter.keys():
            safr_count += dict_counter[entry['word']]
            print(f"DEBUG: matched root South Africa: {entry['word']}")
        if entry['region'] == "Wales" and entry['word'] in dict_counter.keys():
            welsh_count += dict_counter[entry['word']]
            print(f"DEBUG: matched root Wales: {entry['word']}")
        if entry['region'] == "New England" and entry['word'] in dict_counter.keys():
            neng_count += dict_counter[entry['word']]
            print(f"DEBUG: matched root New England: {entry['word']}")
        if entry['region'] == "East Asia" and entry['word'] in dict_counter.keys():
            easi_count += dict_counter[entry['word']]
            print(f"DEBUG: matched root East Asia: {entry['word']}")
        if entry['region'] == "West Asia" and entry['word'] in dict_counter.keys():
            wasi_count += dict_counter[entry['word']]
            print(f"DEBUG: matched root West Asia: {entry['word']}")
        if entry['region'] == "South Asia" and entry['word'] in dict_counter.keys():
            sasi_count += dict_counter[entry['word']]
            print(f"DEBUG: matched root South Asia: {entry['word']}")
        if entry['region'] == "South-East Asia" and entry['word'] in dict_counter.keys():
            seasi_count += dict_counter[entry['word']]
            print(f"DEBUG: matched root South-East Asia: {entry['word']}")
    print(f"DEBUG: after root detection, uk_count={uk_count}, name_count={name_count}, us_count={us_count}, can_count={can_count}, austral_count={austral_count}, nz_count={nz_count}, scot_count={scot_count}, irish_count={irish_count}, ind_count={ind_count}, eafr_count={eafr_count}, wafr_count={wafr_count}, safr_count={safr_count}, welsh_count={welsh_count}, neng_count={neng_count}, easi_count={easi_count}, wasi_count={wasi_count}, sasi_count={sasi_count}, seasi_count={seasi_count}")
    total = uk_count + name_count + us_count + can_count + austral_count + nz_count + scot_count + irish_count + ind_count + eafr_count + wafr_count + safr_count + welsh_count + neng_count + easi_count + wasi_count + sasi_count + seasi_count
    
    return {
        "uk_count": uk_count,
        "name_count": name_count,
        "us_count": us_count,
        "can_count": can_count,
        "austral_count": austral_count,
        "nz_count": nz_count,
        "scot_count": scot_count,
        "irish_count": irish_count,
        "ind_count": ind_count,
        "eafr_count": eafr_count,
        "wafr_count": wafr_count,
        "safr_count": safr_count,
        "welsh_count": welsh_count,
        "neng_count": neng_count,
        "easi_count": easi_count,
        "wasi_count": wasi_count,
        "sasi_count": sasi_count,
        "seasi_count": seasi_count,
        "total": total
    }


