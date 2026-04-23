from app.database import fetch_articles

KEYWORDS = {
    "ipl": ["cricket", "sports"],
    "cricket": ["ipl", "sports"],
    "stock": ["business", "market"],
}


def retrieve_relevant(query):
    articles = fetch_articles()
    query_words = query.lower().split()

    expanded_words = query_words[:]

    # 🔥 expand meaning
    for word in query_words:
        if word in KEYWORDS:
            expanded_words.extend(KEYWORDS[word])

    results = []
    category_results = []

    for article in articles:
        title = article[1].lower()
        category = article[5].lower()

        if any(word in title for word in expanded_words):
            results.append(article)

        if any(word in category for word in expanded_words):
            category_results.append(article)

    if results:
        return results[:5]

    if category_results:
        return category_results[:5]

    return articles[:5]