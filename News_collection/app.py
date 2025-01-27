
# Backend Code
from flask import Flask, jsonify, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

def scrape_news(no_page):
    url = "https://www.moneycontrol.com/news/business/markets/"
    urls = [url]
    for i in range(2, no_page + 1):
        urls.append(url + f"page-{i}")

    news_data = []
    for u in urls:
        content = requests.get(u)
        soup = BeautifulSoup(content.text, 'html.parser')
        tags = soup.findAll('ul', id="cagetory")

        for tag in tags:
            links = tag.findAll('a')
            for link in links:
                news_data.append(link.get_text(strip=True))
    
    return news_data

@app.route('/news/<int:no_page>', methods=['GET'])
def get_news(no_page):
    news = scrape_news(no_page)
    return jsonify(news)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
