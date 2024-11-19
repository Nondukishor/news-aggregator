
# News Aggregator with Topic Extraction

## Overview

This program aggregates news articles from multiple RSS feeds, persists the data into a JSON file, and extracts topics and named entities from the articles. It includes additional functionalities such as filtering articles based on keywords or date ranges. The focus is on functionality, efficiency, and extensibility.

---

## Features

- **RSS Feed Aggregation**: Fetches news articles from RSS feeds provided in the configuration.
- **Data Persistence**: Stores the fetched articles in a JSON file to ensure durability across sessions.
- **Topic Extraction**: Identifies keywords and topics using NLTK for natural language processing.
- **Named Entity Recognition (NER)**: Extracts named entities like people, locations, and organizations.
- **Filtering**: Supports filtering of articles by keywords and publication dates.
- **Error Handling**: Gracefully handles missing data or RSS feed errors.
- **Extensibility**: Easily add new RSS feeds or extend functionalities like visualization.

---

## Approach

### 1. **Data Structures**

- **Articles**: Stored as a list of dictionaries, where each dictionary represents a news article with the following keys:
  - `title`: The title of the article.
  - `description`: A brief summary of the article.
  - `publication_date`: The publication date (ISO format).
  - `source_url`: The URL of the article.
  - `topics`: Extracted keywords/topics.
  - `named_entities`: Named entities categorized into people, locations, and organizations.

- **Topics**: Extracted as a list of unique keywords for each article using tokenization and stopword removal.

### 2. **Topic Extraction Method**

- Tokenization: Articles are tokenized using `nltk.word_tokenize`.
- Stopword Removal: Common English stopwords are filtered using `nltk.corpus.stopwords`.
- Keyword Selection: Only alphanumeric tokens not present in the stopword list are considered keywords.

### 3. **Named Entity Recognition (NER)**

- Tokenization and POS Tagging: Articles are tokenized and part-of-speech (POS) tagged using NLTK.
- Chunking: Named entities are identified using `nltk.ne_chunk`, which labels entities like PERSON, GPE (locations), and ORGANIZATION.

---

## Installation

### Prerequisites

- Python 3.8+
- Required libraries: `feedparser`, `nltk`, `numpy`, `dateutil`

### Steps

1. Clone the repository:
   ```bash
   git clone git@github.com:Nondukishor/news-aggregator.git
   cd news-aggregator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download NLTK resources:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   nltk.download('maxent_ne_chunker')
   nltk.download('words')
   ```

4. Run the program:
   ```bash
   python main.py
   ```

---

## Usage

### Configuration

Add or modify RSS feeds in the `rss_feeds` dictionary in the script:
```python
rss_feeds = {
    "TechCrunch": "https://techcrunch.com/feed",
    "BBC News - World": "https://feeds.bbci.co.uk/news/world/rss.xml",
    "Reuters": "https://feeds.reuters.com/Reuters/worldNews",
}
```

### Filtering Articles

Modify the `filter_news` function to filter articles based on:
- **Keywords**: Pass a list of keywords to filter articles.
- **Date Range**: Provide `start_date` and `end_date` as `datetime` objects.

### Data Storage

Fetched articles are stored in `news_articles.json`. Each article is represented as a dictionary with metadata and extracted information.

---

## Evaluation Criteria

### Functionality
- Aggregates news articles from RSS feeds and persists data to a JSON file.
- Extracts meaningful topics and named entities.
- Handles errors like missing or invalid RSS feeds gracefully.

### Efficiency
- Prevents duplication by comparing URLs before storing new articles.
- Uses lightweight data structures for processing and storage.

### Error Handling
- Provides meaningful error messages for issues such as network failures or missing RSS fields.

### Documentation
- Detailed explanation of data structures, topic extraction method, and usage instructions.
- Extensible and easy-to-understand code with inline comments.

---

## Future Enhancements

- **Visualization**: Add support for visualizing topics and trends using libraries like Matplotlib or Plotly.
- **Database Integration**: Use a relational or NoSQL database for scalable data storage.
- **Advanced Topic Modeling**: Employ machine learning models like LDA or transformers for more accurate topic extraction.
- **Web Interface**: Create a user-friendly web interface for browsing and filtering articles.

---

## License

This project is licensed under the MIT License. Feel free to use and modify it as needed.

---

## Acknowledgments

- **Libraries Used**: `feedparser`, `nltk`, `numpy`, `dateutil`
- **Inspiration**: RSS feed aggregators and topic extraction tools.