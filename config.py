from datetime import datetime

# --- Configuration ---
rss_feeds = {
    "TechCrunch": "https://techcrunch.com/feed",
    "BBC News - World": "https://feeds.bbci.co.uk/news/world/rss.xml",
    "Reuters": "https://feeds.reuters.com/Reuters/worldNews",
}

# File to store the news articles
data_file = "news_articles.json"

# Interval for fetching news (in seconds)
fetch_interval = 3600  # 1 hour

# Default publication date if unavailable
default_publication_date = datetime.now().isoformat()
