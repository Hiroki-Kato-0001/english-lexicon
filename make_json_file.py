import csv
import json

# This script converts a CSV file containing US and UK English lexicon entries
# into a JSON file, skipping entries that lack both a US and UK term.
csv_file = "lexicon_us_uk - inflection.csv"
json_file = "lexicon_us_uk - inflection.json"

data_inflection = []
with open(csv_file, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # rows without either of us and uk entries are skipped
        if not row['us'] and not row['uk']:
            continue

        entry = {
            "id": int(row['id']) if row['id'] else None,
            "category": row['category'].strip(),
            "uk": row['uk'].strip(),
            "us": row['us'].strip(),
            "source": row['source'].strip() if row['source'] else None,
            "notes": row['notes'].strip() if row['notes'] else None
        }
        data_inflection.append(entry)
    
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(data_inflection, f, ensure_ascii=False, indent=2)

print(f"Converted {len(data_inflection)} entries from {csv_file} to {json_file}.")


csv_file = "lexicon_us_uk - phrase.csv"
json_file = "lexicon_us_uk - phrase.json"

data_phrase = []
with open(csv_file, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # rows without either of us and uk entries are skipped
        if not row['us'] and not row['uk']:
            continue

        entry = {
            "id": int(row['id']) if row['id'] else None,
            "category": row['category'].strip(),
            "uk": row['uk'].strip(),
            "us": row['us'].strip(),
            "source": row['source'].strip() if row['source'] else None,
            "notes": row['notes'].strip() if row['notes'] else None
        }
        data_phrase.append(entry)
    
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(data_phrase, f, ensure_ascii=False, indent=2)

print(f"Converted {len(data_phrase)} entries from {csv_file} to {json_file}.")


csv_file_root = "lexicon_us_uk - root.csv"
json_file_root = "lexicon_us_uk - root.json"

data_root = []
with open(csv_file_root, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # rows without either of us and uk entries are skipped
        if not row['us'] and not row['uk']:
            continue

        entry = {
            "id": int(row['id']) if row['id'] else None,
            "category": row['category'].strip(),
            "uk": row['uk'].strip(),
            "us": row['us'].strip(),
            "source": row['source'].strip() if row['source'] else None,
            "notes": row['notes'].strip() if row['notes'] else None
        }
        data_root.append(entry)

with open(json_file_root, 'w', encoding='utf-8') as f:
    json.dump(data_root, f, ensure_ascii=False, indent=2)

print(f"Converted {len(data_root)} entries from {csv_file_root} to {json_file_root}.")