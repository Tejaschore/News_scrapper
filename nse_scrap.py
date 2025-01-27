import requests
from bs4 import BeautifulSoup

# Define the NSE News URL
url = "https://www.nseindia.com/market-data/market-watch"

# Headers to mimic a browser visit
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

try:
    # Make the GET request
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an error for bad HTTP responses
    
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Locate the news data in the HTML (adjust selectors based on inspection of the NSE site)
    news_section = soup.find('div', {'class': 'news-section-class'})  # Replace with actual class or tag
    news_items = news_section.find_all('a') if news_section else []

    # Extract news headlines and links
    for news_item in news_items:
        headline = news_item.get_text(strip=True)
        link = news_item['href']
        print(f"Headline: {headline}")
        print(f"Link: {link}")
        print("-" * 50)

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
