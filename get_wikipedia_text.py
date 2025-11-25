import wikipedia
import re

wikipedia.set_lang("en")  # Set language to English

def fetch_wikipedia_article():
    keywod = input("Enter a keyword to search on Wikipedia: ").strip()
    search_results = wikipedia.search(keywod)

    if not search_results:
        print("No results found for the given keyword.")
    else:
        print(f"Search results for '{keywod}':")
        for idx, title in enumerate(search_results, start=1):
            print(f"{idx}. {title}")

        choice = int(input("Enter the number of the article you want to read more about: "))
        if 1 <= choice <= len(search_results):
            selected_title = search_results[choice - 1]

            try:
                page = wikipedia.page(selected_title, auto_suggest=False)
                text = page.content

                # Clean the text by removing extra whitespace and numbered references
                text = re.sub(r'\[\d+\]', '', text)  # Remove numbered references
                text = re.sub(r'\s+', ' ', text).strip()

                return {selected_title, text}
                        
            except wikipedia.DisambiguationError as e:
                print(f"The title '{selected_title}' is ambiguous. Possible options are:\n{e.options}")
                return None
            
            except wikipedia.PageError:
                print(f"The page '{selected_title}' does not exist.")
                return None
        else:
            print("Invalid choice.")
            return None