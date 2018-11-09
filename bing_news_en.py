import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.bing.com/news'
news = requests.get(url)
html = news.text
soup = bs(html, 'lxml')

headline_title = []
headline_url = []

for i in range(1,11):
    news_info = soup.select('#mainfeed > div:nth-of-type({0}) > div > a'.format(i))
    headline_title.append(news_info[0].text)
    headline_url.append(news_info[0].get('href'))

print(headline_title, headline_url)
