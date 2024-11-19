# News Aggregator with Topic Extraction

## Overview
This program aggregates news articles from multiple RSS feeds, persists the data into a JSON file, and extracts topics and named entities from the articles. It includes additional functionalities such as filtering articles based on keywords or date ranges. The focus is on functionality, efficiency, and extensibility.

## Features
- ***RSS Feed Aggregation:*** Fetches news articles from RSS feeds provided in the configuration.
- ***Data Persistence:*** Stores the fetched articles in a JSON file to ensure durability across sessions.
- ***Topic Extraction:*** Identifies keywords and topics using NLTK for natural language processing.
- ***Named Entity Recognition (NER):*** Extracts named entities like people, locations, and organizations.
- Filtering: Supports filtering of articles by keywords and publication dates.
- ***Error Handling:*** Gracefully handles missing data or RSS feed errors.
- ***Extensibility:*** Easily add new RSS feeds or extend functionalities like visualization.

## Aproach

### 1. Data Structures
- ***Article:*** Stored as a list of dictionaries, where each dictionary represents a news article with the following keys
    - `title:` The title of the article.
    - `description:` A brief summary of the article.
    - `publication_date:` The publication date (ISO format).
    - `source_url:` The URL of the article.
    - `topics:` Extracted keywords/topics.
    - `named_entities:` Named entities categorized into people, locations, and organizations.
- ***Topics:*** Extracted as a list of unique keywords for each article using tokenization and stopword removal.