import feedparser
import json
import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag, ne_chunk
from datetime import datetime
from dateutil import parser as date_parser
import sched
import time
from config import rss_feeds, data_file, fetch_interval, default_publication_date

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')

# --- Data Handling ---
def load_news_data():
    if os.path.exists(data_file):
        with open(data_file, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_news_data(data):
    with open(data_file, "w") as f:
        json.dump(data, f, indent=4)

# --- RSS Feed Handling ---
def fetch_news_from_feed(url):
    try:
        feed = feedparser.parse(url)
        articles = []
        for entry in feed.entries:
            # Ensure required fields exist
            title = getattr(entry, 'title', 'No Title')
            summary = getattr(entry, 'summary', 'No Summary')
            published = getattr(entry, 'published', default_publication_date)
            source_url = getattr(entry, 'link', '')

            # Parse publication date
            try:
                publication_date = date_parser.parse(published).isoformat()
            except Exception:
                publication_date = default_publication_date

            text = f"{title} {summary}"
            article = {
                "title": title,
                "description": summary,
                "publication_date": publication_date,
                "source_url": source_url,
                "topics": extract_topics(text),
                "named_entities": extract_named_entities(text),
            }
            articles.append(article)
        return articles
    except Exception as e:
        print(f"Error fetching news from {url}: {e}")
        return []

# --- Topic Extraction ---
def extract_topics(text):
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    keywords = [word.lower() for word in tokens if word.isalnum() and word.lower() not in stop_words]
    return list(set(keywords))  # Remove duplicates

# --- Named Entity Recognition ---
def extract_named_entities(text):
    try:
        tokens = word_tokenize(text)
        pos_tags = pos_tag(tokens)
        chunks = ne_chunk(pos_tags)
        entities = {"people": [], "locations": [], "organizations": []}

        for chunk in chunks:
            if hasattr(chunk, 'label'):
                entity = " ".join(c[0] for c in chunk)
                if chunk.label() == "PERSON":
                    entities["people"].append(entity)
                elif chunk.label() == "GPE":  # Geographic location
                    entities["locations"].append(entity)
                elif chunk.label() == "ORGANIZATION":
                    entities["organizations"].append(entity)
        return entities
    except Exception as e:
        print(f"Error extracting named entities: {e}")
        return {"people": [], "locations": [], "organizations": []}

# --- Filtering ---
def filter_news(data, keywords=None, start_date=None, end_date=None):
    filtered_data = []
    for article in data:
        if keywords:
            if not any(keyword.lower() in article["title"].lower() or keyword.lower() in article["description"].lower() for keyword in keywords):
                continue
        if start_date:
            if date_parser.parse(article["publication_date"]) < start_date:
                continue
        if end_date:
            if date_parser.parse(article["publication_date"]) > end_date:
                continue
        filtered_data.append(article)
    return filtered_data

# --- Main Execution ---
def fetch_and_store_news():
    all_news = load_news_data()
    for source, url in rss_feeds.items():
        new_articles = fetch_news_from_feed(url)
        existing_urls = {article["source_url"] for article in all_news}
        new_articles = [article for article in new_articles if article["source_url"] not in existing_urls]

        if new_articles:
            print(f"Fetched {len(new_articles)} new articles from {source}")
            all_news.extend(new_articles)

    save_news_data(all_news)

def periodic_fetch(scheduler):
    fetch_and_store_news()
    scheduler.enter(fetch_interval, 1, periodic_fetch, (scheduler,))

def main():
    scheduler = sched.scheduler(time.time, time.sleep)
    periodic_fetch(scheduler)
    scheduler.run()

if __name__ == "__main__":
    main()
