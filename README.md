# Telegraph.bg News Scraper📰

This project is a simple Python script that scrapes the latest news from telegraph.bg/posledni-novini
 using Requests and BeautifulSoup, and stores the results in a local SQLite database (articles.db).

# Features🚀

Scrapes latest news articles from Telegraph.bg
Extracts:
Title
Body
Author
Publication date
Stores results in a SQLite database (articles.db)
Automatically tracks scraping timestamp (scraped_at)

# Project Structure📂<br />
telegraph<br />
│<br />
├── .github/workflows/             # GitHub Actions workflows<br />
│&nbsp; &nbsp;  └──actions.yml<br />
├──  .gitignore <br />   
├──  articles.db <br /> 
├──  flowchart_telegraph_latest_news.jpg <br /> 
├──  items.py <br /> 
├──  main.py <br /> 
├──  pipelines.py <br /> 
├──  scraper.py <br /> 
├──  requirements.txt <br /> 
└──  README.md <br /> 
<br />

# Requirements⚙️

Python 3.8+
Dependencies:
pip install requests beautifulsoup4

# Usage▶️

Run the scraper:
python scraper.py
If news.db does not exist, it will be created automatically.
New articles are inserted into the database with a UTC timestamp.

# Automating with Cron⏰
A cron job is an automated, scheduled task that runs on a Unix-like system,
using a special syntax called a cron expression to define its frequency and timing. <br />
For example to run every hour:
0 * * * * 

# Example Queries🔍

Open the database in SQLite:
sqlite3 news.db
Show last 5 articles:
SELECT title, pubdate FROM articles ORDER BY id DESC LIMIT 5;
Count total scraped articles:
SELECT COUNT(*) FROM articles;

📌 Notes

The CSS selectors in fetch_articles() may need to be adapted if Telegraph.bg changes its HTML structure.
Extendable: you can easily add JSON/CSV export or more fields.


