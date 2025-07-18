import os
import re
import requests
from markdownify import markdownify as md

BASE_URL = "https://support.optisigns.com"
SECTION_ID = "26324076807315"
API_URL = f"{BASE_URL}/api/v2/help_center/en-us/sections/{SECTION_ID}/articles.json"
OUTPUT_DIR = "data"
LIMIT = 30

def slugify(text):
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[\s_-]+", "-", text)

def scrape_articles(limit=LIMIT):
    print("\U0001F680 Fetching articles from Zendesk API...")
    response = requests.get(API_URL)

    if response.status_code != 200:
        raise Exception(f"❌ API request failed with status code {response.status_code}")

    articles = response.json().get("articles", [])[:limit]
    print(f"🔗 Found {len(articles)} articles.")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    added, updated, skipped = [], [], []

    for article in articles:
        title = article["title"]
        html_body = article["body"]
        markdown = md(html_body)

        filename = slugify(title) + ".md"
        filepath = os.path.join(OUTPUT_DIR, filename)

        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                existing = f.read()
            if existing.strip() == markdown.strip():
                skipped.append(filepath)
                continue
            else:
                updated.append(filepath)
        else:
            added.append(filepath)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(markdown)

    for path in added:
        print(f"🆕 added: {os.path.basename(path)}")
    for path in updated:
        print(f"🔁 updated: {os.path.basename(path)}")
    for path in skipped:
        print(f"⏭️ skipped: {os.path.basename(path)}")

    print(f"\n📊 Summary: {len(added)} added | {len(updated)} updated | {len(skipped)} skipped")
    return added + updated
