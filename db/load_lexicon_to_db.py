import json
import csv
import mysql.connector
import os
import dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Database connection parameters from environment variables
conn = mysql.connector.connect(
    host = os.getenv('DB_HOST'),
    port = os.getenv('DB_PORT'),
    user = os.getenv('DB_USER'),
    password = os.getenv('DB_PASSWORD'),
    database = os.getenv('DB_NAME')
)

cursor = conn.cursor()

# Insert data into the database
def insert_entry(word, entry_type, region):
    sql = """
        INSERT INTO lexicon_entries (word, entry_type, region_code)
        VALUES (%s, %s, %s)
    """
    cursor.execute(sql, (word, entry_type, region))

# Load JSON lexicons
def load_json_lexicon(path, entry_type):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    count = 0
    for region, words in data.items():
        for word in words:
            insert_entry(word, entry_type, region)
            count += 1
    print(f"Inserted {count} {entry_type} entries from {path}")

# Main
def main():
    cursor.excute("DELETE FROM lexicon_entries")
    conn.commit()

    load_json_lexicon('lexicon - inflection.json', 'inflection')
    load_json_lexicon('lexicon - phrase.json', 'phrase')
    load_json_lexicon('lexicon - root.json', 'root')

    conn.commit()
    print("Lexicon loading completed.")


if __name__ == "__main__":
    main()