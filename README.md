🕷️ Telegraph news with BeautifulSoup
This project downloads current news from telegraph.bg using the beautifulsoup library.
The collected data is stored in a SQLite database (articles.db) and automatically updated every hour via GitHub Actions.

🚀 Features
Extracts article title, body, author, using BeautifulSoup library
Stores all scraped data into a SQLite database (articles.db)
Automated crawling with GitHub Actions (runs every hour) Database updates are version-controlled via Git commits
With each data update, only the last day's data remains in the database file; older data is automatically deleted.


📂Project Structure <br />
telegraph<br />
│<br />
├── .github/workflows/             # GitHub Actions workflows<br />
│&nbsp; &nbsp;  └──actions.yml<br />
├──  .gitignore <br />   
├──  README.md <br />     
├──  main.py <br /> 
├──  news.db <br /> 
└──  requirements.txt <br /> 
<br />


⏰GitHub Actions (Automated Runs)  <br />
<br />
This project includes a workflow at .github/workflows/actions.yml.<br />
The workflow:<br />
<br />
Runs every hour (via cron job)<br />
Executes the spider<br />
Deletes data older than one day
Updates articles.db with new data<br />
Commits changes back to the repository<br />
You can view run logs under the Actions tab in the repository.<br />
<br />

