from db_config import get_connection

def load_lexicon():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
                SELECT
                    lexicon_entries.word,
                    regions.name AS region,
                    entry_types.name AS entry_type
                FROM lexicon_entries
                JOIN regions 
                ON lexicon_entries.region_id = regions.id
                JOIN entry_types 
                ON lexicon_entries.entry_type_id = entry_types.id
                """)
    
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data