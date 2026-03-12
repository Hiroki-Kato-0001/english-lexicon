import csv
from db_config import get_connection


conn = get_connection()
cursor = conn.cursor(dictionary=True)

def get_or_create_id(table, code, name=None):


    cursor.execute(
        f"SELECT id FROM {table} WHERE code = %s",
        (code,)
    )
    result = cursor.fetchone()
    if result:
        return result["id"]
    
    if table == "sources":
        cursor.execute(
                "INSERT INTO sources(code, name) VALUES (%s, %s)",
                (code, name or code)
        )
    elif table == "regions":
        cursor.execute(
                "INSERT INTO regions (code, name) VALUES (%s, %s)",
                (code, name or code)
        )
    elif table == "entry_types":
        cursor.execute(
                "INSERT INTO entry_types (code, name) VALUES (%s, %s)",
                (code, name or code)
        )
    
    conn.commit()
    return cursor.lastrowid

def csv_to_db(csv_file):


    try:
        with open(csv_file, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                word = row["word"].strip()
                entry_type_code = row["entry_type_code"]
                region_code = row["region_code"]
                source_code = row["source_code"]
                note = row["note"]

                entry_type_id = get_or_create_id("entry_types", entry_type_code)
                region_id = get_or_create_id("regions", region_code)
                source_id = get_or_create_id("sources", source_code)

                cursor.execute("""
                    INSERT IGNORE INTO lexicon_entries
                    (word, entry_type_id, region_id, source_id, note)
                    VALUES (%s, %s, %s, %s, %s)
                """, (word, entry_type_id, region_id, source_id, note)
                )

        conn.commit()
    finally:
        cursor.close()
        conn.close()
    
    