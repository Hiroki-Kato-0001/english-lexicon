import csv
import json

# This script converts a CSV file containing US and UK English lexicon entries
# into a JSON file, skipping entries that lack both a US and UK term.
def make_json_file(csv_file):

    data_inflection = []
    data_phrase = []
    data_root = []
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # rows without category entries are skipped
            if not row['category']:
                continue        
            entry = {
                "id": int(row['id']) if row['id'] else None,
                "Great Britain": row['Brit'].strip(),
                "North America": row['NAme'].strip(),
                "United States": row['US'].strip(),
                "Canada": row['Can'].strip(),
                "Australia": row['Austral'].strip(),
                "New Zealand": row['NZ'].strip(),
                "Scotland": row['Scot'].strip(),
                "Ireland": row['Irish'].strip(),
                "India": row['Ind'].strip(),
                "East Africa": row['EAfr'].strip(),
                "West Africa": row['WAfr'].strip(),
                "South Africa": row['SAfr'].strip(),
                "North Africa": row['NAfr'].strip(),
                "New England": row['NEng'].strip(),
                "East Asia": row['EAsi'].strip(),
                "West Asia": row['WAsi'].strip(),
                "South Asia": row['SAsi'].strip(),
                "North Asia": row['NAsi'].strip(),
                "source": row['source'].strip() if row['source'] else None,
                "notes": row['note'].strip() if row['note'] else None
            }
            if row['category'].strip().lower() == 'inflection':
                data_inflection.append(entry)
            elif row['category'].strip().lower() == 'phrase':
                data_phrase.append(entry)
            else:
                data_root.append(entry)


    json_file = "lexicon_us_uk - inflection.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data_inflection, f, ensure_ascii=False, indent=2)

    print(f"Converted {len(data_inflection)} entries from {csv_file} to {json_file}.")

    json_file = "lexicon_us_uk - phrase.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data_phrase, f, ensure_ascii=False, indent=2)

    print(f"Converted {len(data_phrase)} entries from {csv_file} to {json_file}.")

    json_file = "lexicon_us_uk - root.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data_root, f, ensure_ascii=False, indent=2)

    print(f"Converted {len(data_root)} entries from {csv_file} to {json_file}.")

    return {
    "inflection": len(data_inflection),
    "phrase": len(data_phrase),
    "root": len(data_root)
    }