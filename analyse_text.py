import re
import spacy
import collections

def load_id_map(cursor, table):
    cursor.execute(f"SELECT id, name FROM {table}")
    return {row['name']: row['id'] for row in cursor.fetchall()}


def analyze_text(conn, cursor, file_or_url, text, data):

    results_to_insert = []

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

    entry_type_map = load_id_map(cursor, "entry_types")
    region_map = load_id_map(cursor, "regions")

    for entry in data:

        if entry['entry_type'] == "Inflection" or entry['entry_type'] == "Phrase":
            word = entry['word']
            pattern = rf"\b{re.escape(word)}\b"
            matches = re.findall(pattern, text)
            count = len(matches)
            
            if count == 0:
                continue
            
            region = entry['region']            

            if region == "United Kingdom":
                uk_count += count
                print(f"matched inflection/phrase United Kingdom:{word} x {count}")
            if region == "North America":
                name_count += count
                print(f"matched inflection/phrase North America:{word} x {count}")
            if region == "United States":
                us_count += count
                print(f"matched inflection/phrase United States:{word} x {count}")
            if region == "Canada":
                can_count += count
                print(f"matched inflection/phrase Canada:{word} x {count}")
            if region == "Australia":
                austral_count += count
                print(f"matched inflection/phrase Australia:{word} x {count}")
            if region == "New Zealand":
                nz_count += count
                print(f"matched inflection/phrase New Zealand:{word} x {count}")
            if region == "Scotland":
                scot_count += count
                print(f"matched inflection/phrase Scotland:{word} x {count}")
            if region == "Ireland":
                irish_count += count
                print(f"matched inflection/phrase Ireland:{word} x {count}")
            if region == "India":
                ind_count += count
                print(f"matched inflection/phrase India:{word} x {count}")
            if region == "East Africa":
                eafr_count += count
                print(f"matched inflection/phrase East Africa:{word} x {count}")
            if region == "West Africa":
                wafr_count += count
                print(f"matched inflection/phrase West Africa:{word} x {count}")
            if region == "South Africa":
                safr_count += count
                print(f"matched inflection/phrase South Africa:{word} x {count}")
            if region == "Wales":
                welsh_count += count
                print(f"matched inflection/phrase Wales:{word} x {count}")
            if region == "New England":
                neng_count += count
                print(f"matched inflection/phrase New England:{word} x {count}")
            if region == "East Asia":
                easi_count += count
                print(f"matched inflection/phrase East Asia:{word} x {count}")
            if region == "West Asia":
                wasi_count += count
                print(f"matched inflection/phrase West Asia:{word} x {count}")
            if region == "South Asia":
                sasi_count += count
                print(f"matched inflection/phrase South Asia:{word} x {count}")
            if region == "South-East Asia":
                seasi_count += count
                print(f"matched inflection/phrase South-East Asia:{word} x {count}")
            
# Add the results to the list for database insertion
#
#        entry_type_id = entry_type_map[entry['entry_type']]
#        region_id = region_map[region]
#
#        results_to_insert.append((
#            file_or_url, 
#            word, 
#            entry_type_id, 
#            region_id, 
#            count
#        ))
#
# Insert the results into the database
#    if results_to_insert:
#        cursor.executemany("""
#            INSERT INTO analysis_results
#            (file_or_url, word, entry_type_id, region_id, count)
#            VALUES (%s, %s, %s, %s, %s)
#        """, results_to_insert)
#
#        conn.commit()
#    print(f"Inserted {len(results_to_insert)} analysis results into the database.")
    
    print(f"After analyzing the text, the inflection and phrase counts are: uk_count={uk_count}, name_count={name_count}, us_count={us_count}, can_count={can_count}, austral_count={austral_count}, nz_count={nz_count}, scot_count={scot_count}, irish_count={irish_count}, ind_count={ind_count}, eafr_count={eafr_count}, wafr_count={wafr_count}, safr_count={safr_count}, welsh_count={welsh_count}, neng_count={neng_count}, easi_count={easi_count}, wasi_count={wasi_count}, sasi_count={sasi_count}, seasi_count={seasi_count}")
    return uk_count, name_count, us_count, can_count, austral_count, nz_count, scot_count, irish_count, ind_count, eafr_count, wafr_count, safr_count, welsh_count, neng_count, easi_count, wasi_count, sasi_count, seasi_count

# Load the spaCy model        
nlp = spacy.load("en_core_web_sm")
# Increase the maximum length of text that spaCy can process if needed
nlp.max_length = 6000000


def analyze_text_with_spacy(conn, cursor, file_or_url, text, data, uk_count, name_count, us_count, can_count, austral_count,
                             nz_count, scot_count, irish_count, ind_count, eafr_count, wafr_count, safr_count,
                             welsh_count, neng_count, easi_count, wasi_count, sasi_count, seasi_count):

    results_to_insert = []

    doc = nlp(text)
    lemmas = [token.lemma_ for token in doc]
    dict_counter = collections.Counter(lemmas)
    
    entry_type_map = load_id_map(cursor, "entry_types")
    region_map = load_id_map(cursor, "regions")

    for entry in data:

        if entry['entry_type'] == "Root":

            word = entry['word']
            count = dict_counter[word]

            if count == 0:
                continue

            region = entry['region']
                
            if region == "United Kingdom":
                uk_count += count
                print(f"matched root United Kingdom:{word} x {count}")
            if region == "North America":
                name_count += count
                print(f"matched root North America:{word} x {count}")
            if region == "United States":
                us_count += count
                print(f"matched root United States:{word} x {count}")
            if region == "Canada":
                can_count += count
                print(f"matched root Canada:{word} x {count}")
            if region == "Australia":
                austral_count += count
                print(f"matched root Australia:{word} x {count}")
            if region == "New Zealand":
                nz_count += count
                print(f"matched root New Zealand:{word} x {count}")
            if region == "Scotland":
                scot_count += count
                print(f"matched root Scotland:{word} x {count}")
            if region == "Ireland":
                irish_count += count
                print(f"matched root Ireland:{word} x {count}")
            if region == "India":
                ind_count += count
                print(f"matched root India:{word} x {count}")
            if region == "East Africa":
                eafr_count += count
                print(f"matched root East Africa:{word} x {count}")
            if region == "West Africa":
                wafr_count += count
                print(f"matched root West Africa:{word} x {count}")
            if region == "South Africa":
                safr_count += count
                print(f"matched root South Africa:{word} x {count}")
            if region == "Wales":
                welsh_count += count
                print(f"matched root Wales:{word} x {count}")
            if region == "New England":
                neng_count += count
                print(f"matched root New England:{word} x {count}")
            if region == "East Asia":
                easi_count += count
                print(f"matched root East Asia:{word} x {count}")
            if region == "West Asia":
                wasi_count += count
                print(f"matched root West Asia:{word} x {count}")
            if region == "South Asia":
                sasi_count += count
                print(f"matched root South Asia:{word} x {count}")
            if region == "South-East Asia":
                seasi_count += count
                print(f"matched root South-East Asia:{word} x {count}")


# Add the results to the list for database insertion

#        entry_type_id = entry_type_map[entry['entry_type']]
#        region_id = region_map[region]
#
#        results_to_insert.append((
#            file_or_url, 
#            word, 
#            entry_type_id, 
#            region_id, 
#            count
#        ))
#
# Insert the results into the database
#    if results_to_insert:
#        cursor.executemany("""
#            INSERT INTO analysis_results
#            (file_or_url, word, entry_type_id, region_id, count)
#            VALUES (%s, %s, %s, %s, %s)
#        """, results_to_insert)
#
#        conn.commit()
#    print(f"Inserted {len(results_to_insert)} analysis results into the database.")
#
    print(f"After analyzing the text with spaCy, the final counts are: uk_count={uk_count}, name_count={name_count}, us_count={us_count}, can_count={can_count}, austral_count={austral_count}, nz_count={nz_count}, scot_count={scot_count}, irish_count={irish_count}, ind_count={ind_count}, eafr_count={eafr_count}, wafr_count={wafr_count}, safr_count={safr_count}, welsh_count={welsh_count}, neng_count={neng_count}, easi_count={easi_count}, wasi_count={wasi_count}, sasi_count={sasi_count}, seasi_count={seasi_count}")
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