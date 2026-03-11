from import_csv import csv_to_db

def main():
    csv_file = "lexicon - raw data.csv"

    print("Importing CSV into MySQL database...")

    csv_to_db(csv_file)

    print("Done.")

if __name__ == "__main__":
    main()