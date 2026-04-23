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

    links = []

    for item in soup.find_all("a"):
        title = item.text.strip()

        if len(title) > 30:
            link = item.get("href")

            if link and not link.startswith("http"):
                link = "https://timesofindia.indiatimes.com" + link

            # 🔥 only sports related links when category is sports
            if category == "sports" and "sports" not in link:
                continue

            links.append((title, link))

    def process(link_tuple):
        title, link = link_tuple
        return {
            "title": title,
            "content": title,
            "url": link,
            "published_at": str(datetime.now()),
            "category": category
        }

    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(process, links[:25]))  # 🔥 increased coverage

    return results