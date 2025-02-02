from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
import pandas as pd
import ssl
import time  # Import time module to avoid NameError

app = Flask(__name__)

def scrape_news():
    # Example HTML for scraping
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = "https://pulse.zerodha.com/"
    content = requests.get(url)

    soup = BeautifulSoup(content.text, 'html.parser')

    tag2 = soup.find_all('ul', id='news')

    titles = []
    descriptions = []
    dates = []
    sources = []
    urls = []
    
    for ul in tag2:
        for li in ul.find_all('li', class_='box item'):
            title = li.find('h2', class_='title').get_text(strip=True)
            desc = li.find('div', class_='desc').get_text(strip=True)
            date = li.find('span', class_='date').get_text(strip=True)
            source = li.find('span', class_='feed').get_text(strip=True)
            url = li.find('h2', class_='title').find('a').get('href')

            titles.append(title)
            descriptions.append(desc)
            dates.append(date)
            sources.append(source)
            urls.append(url)

    news_df = pd.DataFrame({
        'Title': titles,
        'Description': descriptions,
        'Date': dates,
        'Source': sources,
        "Urls": urls
    })
    news_df.to_csv("Zerodha_News_live.csv")
    return news_df

@app.route('/page/<int:page_num>')
def index(page_num):
    news_df = scrape_news()
    per_page = 6  # Display 6 news items per page
    start = (page_num - 1) * per_page
    end = page_num * per_page
    page_news = news_df[start:end]

    total_pages = (len(news_df) + per_page - 1) // per_page  # Calculate total number of pages
    news = page_news.to_dict(orient='records')

    return render_template('index.html', news=news, page_num=page_num, total_pages=total_pages)

if __name__ == '__main__':
    app.run(debug=True)



