# 🧠 Job Aggregator — Project Summary

## 🎯 Goal
To build a web application that aggregates remote software job listings from multiple online sources, extracts meaningful tags (skills/technologies), and displays them in a searchable, filterable UI. The aim was to create a full-stack, data-focused scraping project showcasing real-world data handling, parsing, and presentation.

## 🛠️ Tech Stack

| Layer         | Tools Used                                       |
|---------------|--------------------------------------------------|
| **Backend**   | Python, Flask, SQLAlchemy                        |
| **Scraping**  | Requests, BeautifulSoup                          |
| **Database**  | SQLite (via SQLAlchemy ORM)                      |
| **Frontend**  | HTML, CSS, Jinja2 (template engine)              |
| **Storage**   | CSV for raw exports; SQLite for structured data |
| **Deployment** (Optional) | GitHub Pages (static), Render/Heroku (Flask app) |

## 📚 What I Learned

### ✅ Web Scraping
- Navigating inconsistent HTML structures across different job boards
- Avoiding bot detection with custom headers
- Extracting nested data like titles, companies, and links

### ✅ Data Cleaning
- Tagging jobs by scanning job titles for tech keywords (e.g., Python, AWS, React)
- Ensuring uniqueness in job entries using composite keys (`title + company`)
- Exporting structured job data to both `.csv` and a SQLite DB

### ✅ Backend & UI
- Building a minimal Flask app to query and display job listings
- Implementing filters in the UI (by keyword and tag)
- Connecting form inputs with SQLAlchemy queries dynamically

### ✅ General Skills
- Project structure and modular code organization
- Full data pipeline: scraping → processing → saving → serving
- Handling errors and failed page requests gracefully
