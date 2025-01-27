import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
#use url>>> https://www.nseindia.com/
#https://www.livemint.com/market
url=input("Enter the URl")
opurl=urllib.request.urlopen(url,context=ctx).read()
htmc=BeautifulSoup(opurl,'html.parser')

tags=htmc('a')
lis=list()
for tag in tags:
    cont=tag.get('href',None)
    lis.append(cont)
first=lis[17]
print(first)

import requests
import pandas as pd

import requests
from bs4 import BeautifulSoup
import pandas as pd

# NSE India Daily Stock News URL
url = "https://www.nseindia.com/market-data/news"

# Add headers to bypass anti-bot mechanisms
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

# Send GET request
response = requests.get(url, headers=headers)

# Check for successful request
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find the news section (Update the div class based on actual structure)
    news_section = soup.find_all("div", class_="news-content")  # Adjust class based on NSE's website structure
    
    # Extract data from the news section
    news_data = []
    for news in news_section:
        headline = news.find("a").text.strip() if news.find("a") else "N/A"
        link = news.find("a")["href"].strip() if news.find("a") else "N/A"
        timestamp = news.find("time").text.strip() if news.find("time") else "N/A"
        
        # Append to the list
        news_data.append({"Headline": headline, "Link": link, "Timestamp": timestamp})
    
    # Create a DataFrame
    df = pd.DataFrame(news_data)
    
    # Save the DataFrame to a CSV file
    output_file = "nse_daily_stock_news.csv"
    df.to_csv(output_file, index=False)
    
    print(f"Data has been saved to {output_file}")
else:
    print(f"Failed to fetch the website. HTTP Status: {response.status_code}")
