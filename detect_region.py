import get_wikipedia_text
import json
import re
import spacy
import collections


def detect_region_inflection(text, lexicon_inflection, brit_count, name_count, us_count, can_count, austral_count,
                             nz_count, scot_count, irish_count, ind_count, eafr_count, wafr_count, safr_count,
                             nafr_count, neng_count, easi_count, wasi_count, sasi_count, nasi_count):

    for entry in lexicon_inflection:
        brit = entry['Great Britain'].lower() if entry['Great Britain'] else None
        name = entry['North America'].lower() if entry['North America'] else None
        us = entry['United States'].lower() if entry['United States'] else None
        can = entry['Canada'].lower() if entry['Canada'] else None
        austral = entry['Australia'].lower() if entry['Australia'] else None
        nz = entry['New Zealand'].lower() if entry['New Zealand'] else None
        scot = entry['Scotland'].lower() if entry['Scotland'] else None
        irish = entry['Ireland'].lower() if entry['Ireland'] else None
        ind = entry['India'].lower() if entry['India'] else None
        eafr = entry['East Africa'].lower() if entry['East Africa'] else None
        wafr = entry['West Africa'].lower() if entry['West Africa'] else None
        safr = entry['South Africa'].lower() if entry['South Africa'] else None
        nafr = entry['North Africa'].lower() if entry['North Africa'] else None
        neng = entry['New England'].lower() if entry['New England'] else None
        easi = entry['East Asia'].lower() if entry['East Asia'] else None
        wasi = entry['West Asia'].lower() if entry['West Asia'] else None
        sasi = entry['South Asia'].lower() if entry['South Asia'] else None
        nasi = entry['North Asia'].lower() if entry['North Asia'] else None

        if brit and re.search(rf"\b{re.escape(brit)}\b", text):
            brit_count += 1
            print("DEBUG: matched inflection Great Britain:", brit)
        if name and re.search(rf"\b{re.escape(name)}\b", text):
            name_count += 1
            print("DEBUG: matched inflection North America:", name)
        if us and re.search(rf"\b{re.escape(us)}\b", text):
            us_count += 1
            print("DEBUG: matched inflection US:", us)
        if can and re.search(rf"\b{re.escape(can)}\b", text):
            can_count += 1
            print("DEBUG: matched inflection Canada:", can)
        if austral and re.search(rf"\b{re.escape(austral)}\b", text):
            austral_count += 1
            print("DEBUG: matched inflection Australia:", austral)
        if nz and re.search(rf"\b{re.escape(nz)}\b", text):
            nz_count += 1
            print("DEBUG: matched inflection New Zealand:", nz)
        if scot and re.search(rf"\b{re.escape(scot)}\b", text):
            scot_count += 1
            print("DEBUG: matched inflection Scotland:", scot)
        if irish and re.search(rf"\b{re.escape(irish)}\b", text):
            irish_count += 1
            print("DEBUG: matched inflection Ireland:", irish)
        if ind and re.search(rf"\b{re.escape(ind)}\b", text):
            ind_count += 1
            print("DEBUG: matched inflection India:", ind)
        if eafr and re.search(rf"\b{re.escape(eafr)}\b", text):
            eafr_count += 1
            print("DEBUG: matched inflection East Africa:", eafr)
        if wafr and re.search(rf"\b{re.escape(wafr)}\b", text):
            wafr_count += 1
            print("DEBUG: matched inflection West Africa:", wafr)
        if safr and re.search(rf"\b{re.escape(safr)}\b", text):
            safr_count += 1
            print("DEBUG: matched inflection South Africa:", safr)
        if nafr and re.search(rf"\b{re.escape(nafr)}\b", text):
            nafr_count += 1
            print("DEBUG: matched inflection North Africa:", nafr)
        if neng and re.search(rf"\b{re.escape(neng)}\b", text):
            neng_count += 1
            print("DEBUG: matched inflection New England:", neng)
        if easi and re.search(rf"\b{re.escape(easi)}\b", text):
            easi_count += 1
            print("DEBUG: matched inflection East Asia:", easi)
        if wasi and re.search(rf"\b{re.escape(wasi)}\b", text):
            wasi_count += 1
            print("DEBUG: matched inflection West Asia:", wasi)
        if sasi and re.search(rf"\b{re.escape(sasi)}\b", text):
            sasi_count += 1
            print("DEBUG: matched inflection South Asia:", sasi)
        if nasi and re.search(rf"\b{re.escape(nasi)}\b", text):
            nasi_count += 1
            print("DEBUG: matched inflection North Asia:", nasi)

    print(f"DEBUG: after inflection detection, brit_count={brit_count}, name_count={name_count}, us_count={us_count}, can_count={can_count}, austral_count={austral_count}, nz_count={nz_count}, scot_count={scot_count}, irish_count={irish_count}, ind_count={ind_count}, eafr_count={eafr_count}, wafr_count={wafr_count}, safr_count={safr_count}, nafr_count={nafr_count}, neng_count={neng_count}, easi_count={easi_count}, wasi_count={wasi_count}, sasi_count={sasi_count}, nasi_count={nasi_count}")
    return brit_count, name_count, us_count, can_count, austral_count, nz_count, scot_count, irish_count, ind_count, eafr_count, wafr_count, safr_count, nafr_count, neng_count, easi_count, wasi_count, sasi_count, nasi_count


def detect_region_phrase(text, lexicon_phrase, brit_count, name_count, us_count, can_count, austral_count,
                             nz_count, scot_count, irish_count, ind_count, eafr_count, wafr_count, safr_count,
                             nafr_count, neng_count, easi_count, wasi_count, sasi_count, nasi_count):

    for entry in lexicon_phrase:
        brit = entry['Great Britain'].lower() if entry['Great Britain'] else None
        name = entry['North America'].lower() if entry['North America'] else None
        us = entry['United States'].lower() if entry['United States'] else None
        can = entry['Canada'].lower() if entry['Canada'] else None
        austral = entry['Australia'].lower() if entry['Australia'] else None
        nz = entry['New Zealand'].lower() if entry['New Zealand'] else None
        scot = entry['Scotland'].lower() if entry['Scotland'] else None
        irish = entry['Ireland'].lower() if entry['Ireland'] else None
        ind = entry['India'].lower() if entry['India'] else None
        eafr = entry['East Africa'].lower() if entry['East Africa'] else None
        wafr = entry['West Africa'].lower() if entry['West Africa'] else None
        safr = entry['South Africa'].lower() if entry['South Africa'] else None
        nafr = entry['North Africa'].lower() if entry['North Africa'] else None
        neng = entry['New England'].lower() if entry['New England'] else None
        easi = entry['East Asia'].lower() if entry['East Asia'] else None
        wasi = entry['West Asia'].lower() if entry['West Asia'] else None
        sasi = entry['South Asia'].lower() if entry['South Asia'] else None
        nasi = entry['North Asia'].lower() if entry['North Asia'] else None

        if brit and re.search(rf"\b{re.escape(brit)}\b", text):
            brit_count += 1
            print("DEBUG: matched phrase Great Britain:", brit)
        if name and re.search(rf"\b{re.escape(name)}\b", text):
            name_count += 1
            print("DEBUG: matched phrase North America:", name)
        if us and re.search(rf"\b{re.escape(us)}\b", text):
            us_count += 1
            print("DEBUG: matched phrase United States:", us)
        if can and re.search(rf"\b{re.escape(can)}\b", text):
            can_count += 1
            print("DEBUG: matched phrase Canada:", can)
        if austral and re.search(rf"\b{re.escape(austral)}\b", text):
            austral_count += 1
            print("DEBUG: matched phrase Australia:", austral)
        if nz and re.search(rf"\b{re.escape(nz)}\b", text):
            nz_count += 1
            print("DEBUG: matched phrase New Zealand:", nz)
        if scot and re.search(rf"\b{re.escape(scot)}\b", text):
            scot_count += 1
            print("DEBUG: matched phrase Scotland:", scot)
        if irish and re.search(rf"\b{re.escape(irish)}\b", text):
            irish_count += 1
            print("DEBUG: matched phrase Ireland:", irish)
        if ind and re.search(rf"\b{re.escape(ind)}\b", text):
            ind_count += 1
            print("DEBUG: matched phrase India:", ind)
        if eafr and re.search(rf"\b{re.escape(eafr)}\b", text):
            eafr_count += 1
            print("DEBUG: matched phrase East Africa:", eafr)
        if wafr and re.search(rf"\b{re.escape(wafr)}\b", text):
            wafr_count += 1
            print("DEBUG: matched phrase West Africa:", wafr)
        if safr and re.search(rf"\b{re.escape(safr)}\b", text):
            safr_count += 1
            print("DEBUG: matched phrase South Africa:", safr)
        if nafr and re.search(rf"\b{re.escape(nafr)}\b", text):
            nafr_count += 1
            print("DEBUG: matched phrase North Africa:", nafr)
        if neng and re.search(rf"\b{re.escape(neng)}\b", text):
            neng_count += 1
            print("DEBUG: matched phrase New England:", neng)
        if easi and re.search(rf"\b{re.escape(easi)}\b", text):
            easi_count += 1
            print("DEBUG: matched phrase East Asia:", easi)
        if wasi and re.search(rf"\b{re.escape(wasi)}\b", text):
            wasi_count += 1
            print("DEBUG: matched phrase West Asia:", wasi)
        if sasi and re.search(rf"\b{re.escape(sasi)}\b", text):
            sasi_count += 1
            print("DEBUG: matched phrase South Asia:", sasi)
        if nasi and re.search(rf"\b{re.escape(nasi)}\b", text):
            nasi_count += 1
            print("DEBUG: matched phrase North Asia:", nasi)

    print(f"DEBUG: after phrase detection, brit_count={brit_count}, name_count={name_count}, us_count={us_count}, can_count={can_count}, austral_count={austral_count}, nz_count={nz_count}, scot_count={scot_count}, irish_count={irish_count}, ind_count={ind_count}, eafr_count={eafr_count}, wafr_count={wafr_count}, safr_count={safr_count}, nafr_count={nafr_count}, neng_count={neng_count}, easi_count={easi_count}, wasi_count={wasi_count}, sasi_count={sasi_count}, nasi_count={nasi_count}")
    return brit_count, name_count, us_count, can_count, austral_count, nz_count, scot_count, irish_count, ind_count, eafr_count, wafr_count, safr_count, nafr_count, neng_count, easi_count, wasi_count, sasi_count, nasi_count


# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

def detect_region_with_spacy(text, lexicon_root, brit_count, name_count, us_count, can_count, austral_count,
                             nz_count, scot_count, irish_count, ind_count, eafr_count, wafr_count, safr_count,
                             nafr_count, neng_count, easi_count, wasi_count, sasi_count, nasi_count):

    doc = nlp(text)
    lemmas = [token.lemma_ for token in doc]
    dict_counter = collections.Counter(lemmas)

    for entry in lexicon_root:
        brit = entry['Great Britain'].lower() if entry['Great Britain'] else None
        name = entry['North America'].lower() if entry['North America'] else None
        us = entry['United States'].lower() if entry['United States'] else None
        can = entry['Canada'].lower() if entry['Canada'] else None
        austral = entry['Australia'].lower() if entry['Australia'] else None
        nz = entry['New Zealand'].lower() if entry['New Zealand'] else None
        scot = entry['Scotland'].lower() if entry['Scotland'] else None
        irish = entry['Ireland'].lower() if entry['Ireland'] else None
        ind = entry['India'].lower() if entry['India'] else None
        eafr = entry['East Africa'].lower() if entry['East Africa'] else None
        wafr = entry['West Africa'].lower() if entry['West Africa'] else None
        safr = entry['South Africa'].lower() if entry['South Africa'] else None
        nafr = entry['North Africa'].lower() if entry['North Africa'] else None
        neng = entry['New England'].lower() if entry['New England'] else None
        easi = entry['East Asia'].lower() if entry['East Asia'] else None
        wasi = entry['West Asia'].lower() if entry['West Asia'] else None
        sasi = entry['South Asia'].lower() if entry['South Asia'] else None
        nasi = entry['North Asia'].lower() if entry['North Asia'] else None


        if brit and brit in dict_counter.keys():
            brit_count += dict_counter[brit]
            print(f"DEBUG: found Great Britain root: {brit}")
        if name and name in dict_counter.keys():
            name_count += dict_counter[name]
            print(f"DEBUG: found North America root: {name}")
        if us and us in dict_counter.keys():
            us_count += dict_counter[us]
            print(f"DEBUG: found North America root: {us}")
        if can and can in dict_counter.keys():
            can_count += dict_counter[can]
            print(f"DEBUG: found Canada root: {can}")
        if austral and austral in dict_counter.keys():
            austral_count += dict_counter[austral]
            print(f"DEBUG: found Australia root: {austral}")
        if nz and nz in dict_counter.keys():
            nz_count += dict_counter[nz]
            print(f"DEBUG: found New Zealand root: {nz}")
        if scot and scot in dict_counter.keys():
            scot_count += dict_counter[scot]
            print(f"DEBUG: found Scotland root: {scot}")
        if irish and irish in dict_counter.keys():
            irish_count += dict_counter[irish]
            print(f"DEBUG: found Ireland root: {irish}")
        if ind and ind in dict_counter.keys():
            ind_count += dict_counter[ind]
            print(f"DEBUG: found India root: {ind}")
        if eafr and eafr in dict_counter.keys():
            eafr_count += dict_counter[eafr]
            print(f"DEBUG: found East Africa root: {eafr}")
        if wafr and wafr in dict_counter.keys():
            wafr_count += dict_counter[wafr]
            print(f"DEBUG: found West Africa root: {wafr}")
        if safr and safr in dict_counter.keys():
            safr_count += dict_counter[safr]
            print(f"DEBUG: found South Africa root: {safr}")
        if nafr and nafr in dict_counter.keys():
            nafr_count += dict_counter[nafr]
            print(f"DEBUG: found North Africa root: {nafr}")
        if neng and neng in dict_counter.keys():
            neng_count += dict_counter[neng]
            print(f"DEBUG: found New England root: {neng}")
        if easi and easi in dict_counter.keys():
            easi_count += dict_counter[easi]
            print(f"DEBUG: found East Asia root: {easi}")
        if wasi and wasi in dict_counter.keys():
            wasi_count += dict_counter[wasi]
            print(f"DEBUG: found West Asia root: {wasi}")
        if sasi and sasi in dict_counter.keys():
            sasi_count += dict_counter[sasi]
            print(f"DEBUG: found South Asia root: {sasi}")
        if nasi and nasi in dict_counter.keys():
            nasi_count += dict_counter[nasi]
            print(f"DEBUG: found North Asia root: {nasi}")
    print(f"DEBUG: after root detection, brit_count={brit_count}, name_count={name_count}, us_count={us_count}, can_count={can_count}, austral_count={austral_count}, nz_count={nz_count}, scot_count={scot_count}, irish_count={irish_count}, ind_count={ind_count}, eafr_count={eafr_count}, wafr_count={wafr_count}, safr_count={safr_count}, nafr_count={nafr_count}, neng_count={neng_count}, easi_count={easi_count}, wasi_count={wasi_count}, sasi_count={sasi_count}, nasi_count={nasi_count}")
    total = brit_count + name_count + us_count + can_count + austral_count + nz_count + scot_count + irish_count + ind_count + eafr_count + wafr_count + safr_count + nafr_count + neng_count + easi_count + wasi_count + sasi_count + nasi_count
    return {
        "brit_count": brit_count,
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
        "nafr_count": nafr_count,
        "neng_count": neng_count,
        "easi_count": easi_count,
        "wasi_count": wasi_count,
        "sasi_count": sasi_count,
        "nasi_count": nasi_count,
        "total": total
    }


if __name__ == "__main__":
    
    # Fetch a text from Wikipedia
    ariticle = get_wikipedia_text.fetch_wikipedia_article()
    text = ariticle['content']
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
