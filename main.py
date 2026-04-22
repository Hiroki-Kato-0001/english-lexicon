from import_csv import csv_to_db
from load_lexicon import load_lexicon
from get_wikipedia_text import fetch_wikipedia_article
from load_text_file import load_text_from_txt
from load_pdf_file import load_text_from_pdf
from analyse_text import analyze_text, analyze_text_with_spacy
from visualise import plot_region_bar
from db_config import get_connection

# Get database connection
conn = get_connection()
cursor = conn.cursor(dictionary=True)

def get_id_by_name(conn, cursor, table, name):
    cursor.execute(
        f"SELECT id FROM {table} WHERE name = %s",
        (name,)
    )
    result = cursor.fetchone()
    return result['id'] if result else None

csv_file = "lexicon - raw data.csv"

# Import CSV data into MySQL database
print("Importing CSV into MySQL database...")
csv_to_db(conn, cursor, csv_file)
print("Done.")

# Fetch a text from Wikipedia/TXT/PDF
print("Asking for a Wikipedia URL or a local file path (TXT/PDF) to analyze...")
link_or_path = input("Enter Wikipedia URL or local file path: ").strip()
print("User gave input:", link_or_path)

if link_or_path.lower().endswith(".txt"):
    print("Loading text from TXT file...")
    text = load_text_from_txt(link_or_path)
elif link_or_path.lower().endswith(".pdf"):
    print("Loading text from PDF file...")
    text = load_text_from_pdf(link_or_path)
else:
    print("Fetching text from Wikipedia article...")
    article = fetch_wikipedia_article(link_or_path)
    text = article["content"]

text = text.lower()
print(f"Fetched text: {text[10000:10100]}...")

# Load lexicon data from MySQL database
print("Loading lexicon data from MySQL database...")
data = load_lexicon(conn, cursor)
print(f"Loaded {len(data)} lexicon entries.")

# Create a new analysis record
cursor.execute("""
    INSERT INTO analysis (file_or_url) VALUES (%s)
""", (link_or_path,))
analysis_id = cursor.lastrowid
conn.commit()

# Analyze the text using the lexicon data
try:
    print("Analyzing the text with the inflection and phrase lexicon data...")
    inflection_and_phrase_counts = analyze_text(conn, cursor, text, data, analysis_id)

    print("Analyzing the text with the root lexicon data")
    final_counts = analyze_text_with_spacy(conn, cursor, text, data, analysis_id, *inflection_and_phrase_counts)
finally:
    cursor.close()
    conn.close()

# Visualize the results
print("Visualizing the results...")
image_path = plot_region_bar(final_counts)
print(f"Visualization saved to {image_path}")