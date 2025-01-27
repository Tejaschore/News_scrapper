from flask import Flask, render_template
from bs4 import BeautifulSoup
import re
import pandas as pd
import requests
import ssl


app = Flask(__name__)

def scrape_news():
    # Example HTML for scraping
    ctx=ssl.create_default_context()
    ctx.check_hostname=False
    ctx.verify_mode=ssl.CERT_NONE

    url="https://pulse.zerodha.com/"
    content=requests.get(url)

    soup=BeautifulSoup(content.text,'html.parser')


    news_item=soup.find_all('ul', id='news')

    tag2 = soup.find_all('ul', id='news')


    titles = []
    descriptions = []
    dates = []
    sources=[]
    urls=[]
    for ul in tag2:
        for li in ul.find_all('li', class_='box item'):
        
            title = li.find('h2', class_='title').get_text(strip=True)
      
            desc = li.find('div', class_='desc').get_text(strip=True)
    
            date = li.find('span', class_='date').get_text(strip=True)

            source=li.find('span', class_='feed').get_text(strip=True)

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
    "Urls":urls
        })
    news_df.to_csv("Zerodha_News_live.csv")
    return news_df
    
@app.route('/')
def index():
    news_df = scrape_news()
    news = news_df.to_dict(orient='records')  # Convert DataFrame to a list of dictionaries
    return render_template('index.html', news=news)

if __name__ == '__main__':
    app.run(debug=True)
