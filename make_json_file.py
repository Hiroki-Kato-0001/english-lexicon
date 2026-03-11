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
            # rows without word entries are skipped
            if not row['word']:
                continue 
            entry = {
                "entry_type_code": row['entry_type_code'].strip() if row['entry_type_code'] else None,
                "word": row['word'].strip() if row['word'] else None,
                "region_code": row['region_code'].strip() if row['region_code'] else None,
                "source_code": row['source_code'].strip() if row['source_code'] else None,
                "note": row['note'].strip() if row['note'] else None
            }
            if row['entry_type_code'].strip().lower() == 'inflection':
                data_inflection.append(entry)
            elif row['entry_type_code'].strip().lower() == 'phrase':
                data_phrase.append(entry)
            else:
                data_root.append(entry)


    json_file = "lexicon - inflection.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data_inflection, f, ensure_ascii=False, indent=2)

    print(f"Converted {len(data_inflection)} entries from {csv_file} to {json_file}.")

    json_file = "lexicon - phrase.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data_phrase, f, ensure_ascii=False, indent=2)

    print(f"Converted {len(data_phrase)} entries from {csv_file} to {json_file}.")

    json_file = "lexicon - root.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data_root, f, ensure_ascii=False, indent=2)

    print(f"Converted {len(data_root)} entries from {csv_file} to {json_file}.")

    return {
    "inflection": len(data_inflection),
    "phrase": len(data_phrase),
    "root": len(data_root)
    }