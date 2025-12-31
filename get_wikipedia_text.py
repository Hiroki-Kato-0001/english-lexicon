print("DEBUG: script started")

import wikipedia
import re
from urllib.parse import urlparse, unquote

wikipedia.set_lang("en")

def fetch_wikipedia_article():
    print("DEBUG: asking for input now")

    page_link = input("Enter a URL of an article on Wikipedia: ").strip()
    print("DEBUG: user gave:", page_link)

    try:
        # Extract the title from the URL
        path = urlparse(page_link).path
        title = unquote(path.split("/wiki/")[-1])

        print("DEBUG: extracted title:", title)

        page = wikipedia.page(title, auto_suggest=False)
        print("DEBUG: A page was found via title.")

        text = page.content

        # Clean the text
        text = re.sub(r'\[\d+\]', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        text = text.replace('=', '')

        return {
            "title": page.title,
            "url": page_link,
            "content": text
        }

    except wikipedia.PageError:
        print("DEBUG: No page found for the given URL/title")
        return None

    except Exception as e:
        print("Unexpected error:", e)
        return None


if __name__ == "__main__":
    print("DEBUG: calling fetch_wikipedia_article() now")
    result = fetch_wikipedia_article()
    print("DEBUG: returned:", result)