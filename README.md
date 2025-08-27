# Telegraph News Scraper 📰

This project automatically scrapes the latest news from [telegraph.bg](https://telegraph.bg/posledni-novini) and stores them in a SQLite database (`articles.db`).  
The scraper can be run locally or scheduled to run automatically every hour via **GitHub Actions**.

---

## 🚀 Features
- Collects and stores:
  - **Title**
  - **Body**
  - **Author**
  - **URL** (unique)
  - **Scraped timestamp**
- Prevents duplicate entries with a **UNIQUE constraint** on URLs.
- Modular structure (inspired by Scrapy):
  - `items.py` → data model
  - `pipelines.py` → database pipeline
  - `scraper.py` → scraping logic
  - `main.py` → entry point
- GitHub Actions workflow runs hourly to update the database automatically.

---

## 🛠 Installation (Local)
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/telegraph-scraper.git
   cd telegraph-scraper
   

2. (Optional) Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows


3. Install dependencies:
pip install -r requirements.txt


4. Run the scraper:
python main.py

---

## 📂 Project Structure
telegraph-scraper/<br />
│<br />
├── items.py        # Defines the ArticleItem data model<br />
├── pipelines.py    # SQLite pipeline<br />
├── scraper.py      # Scraper implementation<br />
├── main.py         # Entry point that runs the pipeline<br />
├── articles.db     # SQLite database (generated/updated)<br />
├── flowchart_telegraph_latest_news.jpg     # workflow<br />
├── requirements.txt<br />
└── .github/<br />
    └── workflows/<br />
        └── scraper.yml   # GitHub Actions workflow<br />
---

## ⚙️ GitHub Actions

The workflow (.github/workflows/scraper.yml) is configured to:
Run every hour (UTC) via cron,
Scrape new articles and update articles.db,
Commit and push the updated database back to the repository.
Manual workflow runs are also supported.

---

## 🧑‍💻 Contributing<br />

Contributions are welcome!<br />
You can extend the project by adding new pipelines (e.g., JSON/CSV export, API integration) or improving scraping performance.<br />
