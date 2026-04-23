import requests
from bs4 import BeautifulSoup
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

CATEGORY_URLS = {
    "sports": "https://timesofindia.indiatimes.com/sports",
    "business": "https://timesofindia.indiatimes.com/business",
    "technology": "https://timesofindia.indiatimes.com/technology",
    "india": "https://timesofindia.indiatimes.com/india"
}

def scrape_toi(category):
    url = CATEGORY_URLS.get(category)
    headers = {"User-Agent": "Mozilla/5.0"}

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    articles = []

    links = []

    for item in soup.find_all("a"):
        title = item.text.strip()

        if len(title) > 30:
            link = item.get("href")

            if link and not link.startswith("http"):
                link = "https://timesofindia.indiatimes.com" + link

            links.append((title, link))

    # 🔥 parallel fetch
    def process(link_tuple):
        title, link = link_tuple
        content = fetch_full_article(link)

        return {
            "title": title,
            "content": content if content else title,
            "url": link,
            "published_at": str(datetime.now()),
            "category": category
        }

    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(process, links[:5]))

    return results

def fetch_full_article(url):
    try:
        import requests
        from bs4 import BeautifulSoup

        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers)

        soup = BeautifulSoup(res.text, "html.parser")

        paragraphs = soup.find_all("p")

        cleaned = []

        for p in paragraphs:
            text = p.text.strip()

            # 🔥 remove junk
            if len(text) < 50:
                continue
            if "advertisement" in text.lower():
                continue
            if "subscribe" in text.lower():
                continue

            cleaned.append(text)

        content = " ".join(cleaned)

        return content[:1500]  # limit size

    except Exception as e:
        return ""