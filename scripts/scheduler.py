import time
from app.scraper import scrape_toi
from app.database import insert_article, create_table

create_table()

categories = ["sports", "business", "technology", "india"]

while True:
    print("🔄 Fetching latest news...")

    for category in categories:
        articles = scrape_toi(category)

        for article in articles:
            insert_article(article)

    print("✅ Updated!")

    # 🔥 wait 10 minutes
    time.sleep(600)