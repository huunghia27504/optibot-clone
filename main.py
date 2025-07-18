from scraper import scrape_articles
from vector_store import get_or_create_vector_store, upload_to_openai
from assistant import create_assistant

def main():
    scraped_files = scrape_articles()
    vector_store = get_or_create_vector_store()
    upload_to_openai(scraped_files, vector_store)
    create_assistant(vector_store.id)

if __name__ == "__main__":
    main()
