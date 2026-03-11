import re
import spacy
import collections
import matplotlib.pyplot as plt

def detect_region_inflection(text, lexicon_inflection, uk_count, name_count, us_count, can_count, austral_count,
                             nz_count, scot_count, irish_count, ind_count, eafr_count, wafr_count, safr_count,
                             welsh_count, neng_count, easi_count, wasi_count, sasi_count, seasi_count):

    for entry in lexicon_inflection:

        word = entry['word'].lower()
        region_code = entry['region_code']
        pattern = rf"\b{re.escape(word)}\b"
        matches = re.findall(pattern, text)

        count = len(matches)
        if count == 0:
            continue

        if region_code == "uk":
            uk_count += count
            print(f"DEBUG: matched inflection United Kingdom:, {word} x {count}")
        if region_code == "name":
            name_count += count
            print(f"DEBUG: matched inflection North America:, {word} x {count}")
        if region_code == "us":
            us_count += count
            print(f"DEBUG: matched inflection United States:, {word} x {count}")
        if region_code == "can":
            can_count += count
            print(f"DEBUG: matched inflection Canada:, {word} x {count}")
        if region_code == "austral":
            austral_count += count
            print(f"DEBUG: matched inflection Australia:, {word} x {count}")
        if region_code == "nz":
            nz_count += count
            print(f"DEBUG: matched inflection  NewZealand:, {word} x {count}")
        if region_code == "scot":
            scot_count += count
            print(f"DEBUG: matched inflection Scotland:, {word} x {count}")
        if region_code == "irish":
            irish_count += count
            print(f"DEBUG: matched inflection Ireland:, {word} x {count}")
        if region_code == "ind":
            ind_count += count
            print(f"DEBUG: matched inflection India:, {word} x {count}")
        if region_code == "eafr":
            eafr_count += count
            print(f"DEBUG: matched inflection East Africa:, {word} x {count}")
        if region_code == "wafr":
            wafr_count += count
            print(f"DEBUG: matched inflection West Africa:, {word} x {count}")
        if region_code == "Ssafr":
            safr_count += count
            print(f"DEBUG: matched inflection South Africa:, {word} x {count}")
        if region_code == "welsh":
            welsh_count += count
            print(f"DEBUG: matched inflection Wales:, {word} x {count}")
        if region_code == "neng":
            neng_count += count
            print(f"DEBUG: matched inflection New England:, {word} x {count}")
        if region_code == "easi":
            easi_count += count
            print(f"DEBUG: matched inflection East Asia:, {word} x {count}")
        if region_code == "wasi":
            wasi_count += count
            print(f"DEBUG: matched inflection West Asia:, {word} x {count}")
        if region_code == "sasi":
            sasi_count += count
            print(f"DEBUG: matched inflection South Asia:, {word} x {count}")
        if region_code == "seasi":
            seasi_count += count
            print(f"DEBUG: matched inflection South-East Asia:, {word} x {count}")

    print(f"DEBUG: after inflection detection, uk_count={uk_count}, name_count={name_count}, us_count={us_count}, can_count={can_count}, austral_count={austral_count}, nz_count={nz_count}, scot_count={scot_count}, irish_count={irish_count}, ind_count={ind_count}, eafr_count={eafr_count}, wafr_count={wafr_count}, safr_count={safr_count}, welsh_count={welsh_count}, neng_count={neng_count}, easi_count={easi_count}, wasi_count={wasi_count}, sasi_count={sasi_count}, seasi_count={seasi_count}")
    return uk_count, name_count, us_count, can_count, austral_count, nz_count, scot_count, irish_count, ind_count, eafr_count, wafr_count, safr_count, welsh_count, neng_count, easi_count, wasi_count, sasi_count, seasi_count


def detect_region_phrase(text, lexicon_phrase, uk_count, name_count, us_count, can_count, austral_count,
                             nz_count, scot_count, irish_count, ind_count, eafr_count, wafr_count, safr_count,
                             welsh_count, neng_count, easi_count, wasi_count, sasi_count, seasi_count):

    
    for entry in lexicon_phrase:
        word = entry['word'].lower()
        region_code = entry['region_code']
        pattern = rf"\b{re.escape(word)}\b"
        matches = re.findall(pattern, text)

        count = len(matches)
        if count == 0:
            continue

        if region_code == "uk":
            uk_count += count
            print(f"DEBUG: matched phrase United Kingdom:, {word} x {count}")
        if region_code == "name":
            name_count += count
            print(f"DEBUG: matched phrase North America:, {word} x {count}")
        if region_code == "us":
            us_count += count
            print(f"DEBUG: matched phrase United States:, {word} x {count}")
        if region_code == "can":
            can_count += count
            print(f"DEBUG: matched phrase Canada:, {word} x {count}")
        if region_code == "austral":
            austral_count += count
            print(f"DEBUG: matched phrase Australia:, {word} x {count}")
        if region_code == "nz":
            nz_count += count
            print(f"DEBUG: matched phrase New Zealand:, {word} x {count}")
        if region_code == "scot":
            scot_count += count
            print(f"DEBUG: matched phrase Scotland:, {word} x {count}")
        if region_code == "irish":
            irish_count += count
            print(f"DEBUG: matched phrase Ireland:, {word} x {count}")
        if region_code == "ind":
            ind_count += count
            print(f"DEBUG: matched phrase India:, {word} x {count}")
        if region_code == "eafr":
            eafr_count += count
            print(f"DEBUG: matched phrase East Africa:, {word} x {count}")
        if region_code == "wafr":
            wafr_count += count
            print(f"DEBUG: matched phrase West Africa:, {word} x {count}")
        if region_code == "safr":
            safr_count += count
            print(f"DEBUG: matched phrase South Africa:, {word} x {count}")
        if region_code == "welsh":
            welsh_count += count
            print(f"DEBUG: matched phrase Wales:, {word} x {count}")
        if region_code == "neng":
            neng_count += count
            print(f"DEBUG: matched phrase New England:, {word} x {count}")
        if region_code == "easi":
            easi_count += count
            print(f"DEBUG: matched phrase East Asia:, {word} x {count}")
        if region_code == "wasi":
            wasi_count += count
            print(f"DEBUG: matched phrase West Asia:, {word} x {count}")
        if region_code == "sasi":
            sasi_count += count
            print(f"DEBUG: matched phrase South Asia:, {word} x {count}")
        if region_code == "seasi":
            seasi_count += count
            print(f"DEBUG: matched phrase South-East Asia:, {word} x {count}")

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
        
        word = entry['word'].lower()
        region_code = entry['region_code']
        keys = dict_counter.keys()
        count = dict_counter[word]

        if region_code == "uk" and word in keys:
            uk_count += count
            print(f"DEBUG: matched root United Kingdom:{word} x {count}")
        if region_code == "name" and word in keys:
            name_count += count
            print(f"DEBUG: matched root North America:{word} x {count}")
        if region_code == "us" and word in keys:
            us_count += count
            print(f"DEBUG: matched root United States:{word} x {count}")
        if region_code == "can" and word in keys:
            can_count += count
            print(f"DEBUG: matched root Canada:{word} x {count}")
        if region_code == "austral" and word in keys:
            austral_count += count
            print(f"DEBUG: matched root Australia:{word} x {count}")
        if region_code == "nz" and word in keys:
            nz_count += count
            print(f"DEBUG: matched root New Zealand:{word} x {count}")
        if region_code == "scot" and word in keys:
            scot_count += count
            print(f"DEBUG: matched root Scotland:{word} x {count}")
        if region_code == "irish" and word in keys:
            irish_count += count
            print(f"DEBUG: matched root Ireland:{word} x {count}")
        if region_code == "ind" and word in keys:
            ind_count += count
            print(f"DEBUG: matched root India:{word} x {count}")
        if region_code == "eafr" and word in keys:
            eafr_count += count
            print(f"DEBUG: matched root East Africa:{word} x {count}")
        if region_code == "wafr" and word in keys:
            wafr_count += count
            print(f"DEBUG: matched root West Africa:{word} x {count}")
        if region_code == "safr" and word in keys:
            safr_count += count
            print(f"DEBUG: matched root South Africa:{word} x {count}")
        if region_code == "welsh" and word in keys:
            welsh_count += count
            print(f"DEBUG: matched root Wales:{word} x {count}")
        if region_code == "neng" and word in keys:
            neng_count += count
            print(f"DEBUG: matched root New England:{word} x {count}")
        if region_code == "easi" and word in keys:
            easi_count += count
            print(f"DEBUG: matched root East Asia:{word} x {count}")
        if region_code == "wasi" and word in keys:
            wasi_count += count
            print(f"DEBUG: matched root West Asia:{word} x {count}")
        if region_code == "sasi" and word in keys:
            sasi_count += count
            print(f"DEBUG: matched root South Asia:{word} x {count}")
        if region_code == "seasi" and word in keys:
            seasi_count += count
            print(f"DEBUG: matched root South-East Asia:{word} x {count}")
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


