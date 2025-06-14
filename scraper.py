import requests
from bs4 import BeautifulSoup
from models import save_jobs_to_db
import pandas as pd

def extract_tags(title):
    keywords = ['python', 'javascript', 'django', 'flask', 'react', 'node', 'aws', 'remote', 'sql', 'devops']
    found = [kw for kw in keywords if kw.lower() in title.lower()]
    return ', '.join(found)

def scrape_remoteok():
    url = "https://remoteok.io/remote-dev-jobs"
    headers = {'User-Agent': 'Mozilla/5.0'}
    soup = BeautifulSoup(requests.get(url, headers=headers).text, 'html.parser')
    jobs = []
    for row in soup.find_all('tr', class_='job'):
        title = row.find('h2')
        company = row.find('h3')
        link = row.get('data-href')
        if title and company and link:
            title_text = title.text.strip()
            jobs.append({
                "title": title_text,
                "company": company.text.strip(),
                "link": f"https://remoteok.io{link}",
                "tags": extract_tags(title_text)
            })
    return jobs

def scrape_weworkremotely():
    url = "https://weworkremotely.com/categories/remote-programming-jobs"
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    jobs = []
    for li in soup.select('section.jobs li:not(.view-all)'):
        anchor = li.find('a', href=True)
        company = li.find('span', class_='company')
        title = li.find('span', class_='title')
        if anchor and title and company:
            title_text = title.text.strip()
            jobs.append({
                "title": title_text,
                "company": company.text.strip(),
                "link": f"https://weworkremotely.com{anchor['href']}",
                "tags": extract_tags(title_text)
            })
    return jobs

def scrape_python_jobs():
    url = "https://www.python.org/jobs/"
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    jobs = []
    for job in soup.select('ol.list-recent-jobs li'):
        title = job.h2.a.text.strip()
        company = job.find('span', class_='listing-company-name').text.strip()
        link = f"https://www.python.org{job.h2.a['href']}"
        jobs.append({"title": title, "company": company, "link": link, "tags": extract_tags(title)})
    return jobs

def scrape_all():
    all_jobs = []
    all_jobs.extend(scrape_remoteok())
    all_jobs.extend(scrape_weworkremotely())
    all_jobs.extend(scrape_python_jobs())
    df = pd.DataFrame(all_jobs)
    df.to_csv("jobs.csv", index=False)
    save_jobs_to_db(all_jobs)

if __name__ == "__main__":
    scrape_all()
