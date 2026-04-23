from app.database import fetch_articles

KEYWORDS = {
    "ipl": ["cricket", "sports"],
    "cricket": ["ipl", "sports"],
    "football": ["sports"],
    "volleyball": ["sports"],
}

def retrieve_relevant(query):
    articles = fetch_articles()
    query = query.lower()
    query_words = query.split()

    expanded = query_words[:]

    # Expand keywords
    for word in query_words:
        if word in KEYWORDS:
            expanded.extend(KEYWORDS[word])

    results = []

    for article in articles:
        title = article[1].lower()
        category = article[5].lower()

        # Match words in title
        if any(word in title for word in expanded):
            results.append(article)

    # ✅ Case 1: Found relevant results
    if results:
        return results[:5]

    # ✅ Case 2: User asked general query
    if "latest" in query or "news" in query or "india" in query:
        return articles[:5]

    # ✅ Case 3: fallback → still show something
    return articles[:5]