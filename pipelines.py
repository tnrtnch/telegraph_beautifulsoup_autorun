import sqlite3

DB_NAME = "articles.db"

class SQLitePipeline:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS articles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                body TEXT,
                author TEXT,
                url TEXT UNIQUE,
                scraped_at TIMESTAMP
            )
        """)
        self.conn.commit()

    def process_item(self, item):
        try:
            self.cursor.execute("""
                INSERT INTO articles (title, body, author, url, scraped_at)
                VALUES (?, ?, ?, ?, ?)
            """, (item.title, item.body, item.author, item.url, item.scraped_at))
            self.conn.commit()
            print(f"[+] Saved: {item.title}")
        except sqlite3.IntegrityError:
            print(f"[!] Already exists: {item.url}")
        return item

    def close(self):
        self.conn.close()
