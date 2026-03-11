import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="hiroki-A520M-S2H",
        user="root",
        password="Database2@25",
        database="english_lexicon"
    )