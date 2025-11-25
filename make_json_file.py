import csv
import json

csv_file = "lexicon_us_uk.csv"
json_file = "lexicon_us_uk.json"

data = []
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
        data.append(entry)
    
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Converted {len(data)} entries from {csv_file} to {json_file}.")
# This script converts a CSV file containing US and UK English lexicon entries
# into a JSON file, skipping entries that lack both a US and UK term.