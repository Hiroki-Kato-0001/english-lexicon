import re
import spacy
import collections
import matplotlib.pyplot as plt

def detect_region(text, data, uk_count, name_count, us_count, can_count, austral_count,
                             nz_count, scot_count, irish_count, ind_count, eafr_count, wafr_count, safr_count,
                             welsh_count, neng_count, easi_count, wasi_count, sasi_count, seasi_count):

    for entry in data:
        if entry['entry_type'] == "Inflection" or entry['entry_type'] == "Phrase":
            word = entry['word'].lower()
            region = entry['region']
            pattern = rf"\b{re.escape(word)}\b"
            matches = re.findall(pattern, text)

            count = len(matches)
            if count == 0:
                continue

            if region == "United Kingdom":
                uk_count += count
                print(f"DEBUG: matched inflection United Kingdom:, {word} x {count}")
            if region == "North America":
                name_count += count
                print(f"DEBUG: matched inflection North America:, {word} x {count}")
            if region == "United States":
                us_count += count
                print(f"DEBUG: matched inflection United States:, {word} x {count}")
            if region == "Canada":
                can_count += count
                print(f"DEBUG: matched inflection Canada:, {word} x {count}")
            if region == "Australia":
                print(f"DEBUG: matched inflection Australia:, {word} x {count}")
            if region == "New Zealand":
                nz_count += count
                print(f"DEBUG: matched inflection  NewZealand:, {word} x {count}")
            if region == "Scotland":
                scot_count += count
                print(f"DEBUG: matched inflection Scotland:, {word} x {count}")
            if region == "Ireland":
                irish_count += count
                print(f"DEBUG: matched inflection Ireland:, {word} x {count}")
            if region == "Wales":
                welsh_count += count
                print(f"DEBUG: matched inflection Wales:, {word} x {count}")
            if region == "India":
                ind_count += count
                print(f"DEBUG: matched inflection India:, {word} x {count}")
            if region == "East Africa":
                eafr_count += count
                print(f"DEBUG: matched inflection East Africa:, {word} x {count}")
            if region == "West Africa":
                wafr_count += count
                print(f"DEBUG: matched inflection West Africa:, {word} x {count}")
            if region == "South Africa":
                safr_count += count
                print(f"DEBUG: matched inflection South Africa:, {word} x {count}")
            if region == "New England":
                neng_count += count
                print(f"DEBUG: matched inflection New England:, {word} x {count}")
            if region == "East Asia":
                easi_count += count
                print(f"DEBUG: matched inflection East Asia:, {word} x {count}")
            if region == "West Asia":
                wasi_count += count
                print(f"DEBUG: matched inflection West Asia:, {word} x {count}")
            if region == "South Asia":
                sasi_count += count
                print(f"DEBUG: matched inflection South Asia:, {word} x {count}")
            if region == "South-East Asia":
                seasi_count += count
                print(f"DEBUG: matched inflection South-East Asia:, {word} x {count}")

    print(f"DEBUG: after inflection and phrase detection, uk_count={uk_count}, name_count={name_count}, us_count={us_count}, can_count={can_count}, austral_count={austral_count}, nz_count={nz_count}, scot_count={scot_count}, irish_count={irish_count}, welsh_count={welsh_count}, ind_count={ind_count}, eafr_count={eafr_count}, wafr_count={wafr_count}, safr_count={safr_count}, neng_count={neng_count}, easi_count={easi_count}, wasi_count={wasi_count}, sasi_count={sasi_count}, seasi_count={seasi_count}")
    return uk_count, name_count, us_count, can_count, austral_count, nz_count, scot_count, irish_count, ind_count, eafr_count, wafr_count, safr_count, welsh_count, neng_count, easi_count, wasi_count, sasi_count, seasi_count


# Load spaCy English model
nlp = spacy.load("en_core_web_sm")
nlp.max_length = 6000000  # Increase max length if needed

def detect_region_with_spacy(text, data, uk_count, name_count, us_count, can_count, austral_count,
                             nz_count, scot_count, irish_count, ind_count, eafr_count, wafr_count, safr_count,
                             welsh_count, neng_count, easi_count, wasi_count, sasi_count, seasi_count):

    doc = nlp(text)
    lemmas = [token.lemma_ for token in doc]
    dict_counter = collections.Counter(lemmas)

    for entry in data:

        if entry['entry_type'] != "Root":
        
            word = entry['word'].lower()
            region = entry['region']
            keys = dict_counter.keys()
            count = dict_counter[word]

            if region == "United Kingdom" and word in keys:
                uk_count += count
                print(f"DEBUG: matched root United Kingdom:{word} x {count}")
            if region == "North America" and word in keys:
                name_count += count
                print(f"DEBUG: matched root North America:{word} x {count}")
            if region == "United States" and word in keys:
                us_count += count
                print(f"DEBUG: matched root United States:{word} x {count}")
            if region == "Canada" and word in keys:
                can_count += count
                print(f"DEBUG: matched root Canada:{word} x {count}")
            if region == "Australia" and word in keys:
                austral_count += count
                print(f"DEBUG: matched root Australia:{word} x {count}")
            if region == "New Zealand" and word in keys:
                nz_count += count
                print(f"DEBUG: matched root New Zealand:{word} x {count}")
            if region == "Scotland" and word in keys:
                scot_count += count
                print(f"DEBUG: matched root Scotland:{word} x {count}")
            if region == "Ireland" and word in keys:
                irish_count += count
                print(f"DEBUG: matched root Ireland:{word} x {count}")
            if region == "Wales" and word in keys:
                welsh_count += count
                print(f"DEBUG: matched root Wales:{word} x {count}")
            if region == "India" and word in keys:
                ind_count += count
                print(f"DEBUG: matched root India:{word} x {count}")
            if region == "East Africa" and word in keys:
                eafr_count += count
                print(f"DEBUG: matched root East Africa:{word} x {count}")
            if region == "West Africa" and word in keys:
                wafr_count += count
                print(f"DEBUG: matched root West Africa:{word} x {count}")
            if region == "South Africa" and word in keys:
                safr_count += count
                print(f"DEBUG: matched root South Africa:{word} x {count}")
            if region == "New England" and word in keys:
                neng_count += count
                print(f"DEBUG: matched root New England:{word} x {count}")
            if region == "East Asia" and word in keys:
                easi_count += count
                print(f"DEBUG: matched root East Asia:{word} x {count}")
            if region == "West Asia" and word in keys:
                wasi_count += count
                print(f"DEBUG: matched root West Asia:{word} x {count}")
            if region == "South Asia" and word in keys:
                sasi_count += count
                print(f"DEBUG: matched root South Asia:{word} x {count}")
            if region == "South-East Asia" and word in keys:
                seasi_count += count
                print(f"DEBUG: matched root South-East Asia:{word} x {count}")

    print(f"DEBUG: after root detection, uk_count={uk_count}, name_count={name_count}, us_count={us_count}, can_count={can_count}, austral_count={austral_count}, nz_count={nz_count}, scot_count={scot_count}, irish_count={irish_count}, welsh_count={welsh_count}, ind_count={ind_count}, eafr_count={eafr_count}, wafr_count={wafr_count}, safr_count={safr_count}, neng_count={neng_count}, easi_count={easi_count}, wasi_count={wasi_count}, sasi_count={sasi_count}, seasi_count={seasi_count}")
    total = uk_count + name_count + us_count + can_count + austral_count + nz_count + scot_count + irish_count + welsh_count + ind_count + eafr_count + wafr_count + safr_count + neng_count + easi_count + wasi_count + sasi_count + seasi_count
    
    return {
        "uk_count": uk_count,
        "name_count": name_count,
        "us_count": us_count,
        "can_count": can_count,
        "austral_count": austral_count,
        "nz_count": nz_count,
        "scot_count": scot_count,
        "irish_count": irish_count,
        "welsh_count": welsh_count,
        "ind_count": ind_count,
        "eafr_count": eafr_count,
        "wafr_count": wafr_count,
        "safr_count": safr_count,
        "neng_count": neng_count,
        "easi_count": easi_count,
        "wasi_count": wasi_count,
        "sasi_count": sasi_count,
        "seasi_count": seasi_count,
        "total": total
    }


