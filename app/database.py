import sqlite3

conn = sqlite3.connect("news.db", check_same_thread=False)
cursor = conn.cursor()

def create_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS articles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        content TEXT,
        url TEXT,
        published_at TEXT,
        category TEXT
    )
    """)
    conn.commit()


def insert_article(article):
    # avoid duplicates
    cursor.execute("SELECT 1 FROM articles WHERE title = ?", (article["title"],))
    if cursor.fetchone():
        return

    cursor.execute("""
    INSERT INTO articles (title, content, url, published_at, category)
    VALUES (?, ?, ?, ?, ?)
    """, (
        article["title"],
        article["content"],
        article["url"],
        article["published_at"],
        article["category"]
    ))

    conn.commit()


def fetch_articles():
    cursor.execute("SELECT * FROM articles ORDER BY id DESC LIMIT 50")
    return cursor.fetchall()