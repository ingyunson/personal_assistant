import requests
from bs4 import BeautifulSoup as bs

url = 'https://news.yahoo.co.jp/'
news = requests.get(url)
html = news.text
soup = bs(html, 'lxml')

headline_title = []
headline_url = []

news_head = soup.select('#epTabTop > ul.topics > li.topTpi > div > h1 > a')
headline_title.append(news_head[0].text.replace("写真",""))
headline_url.append(news_head[0].get('href'))

for i in range(2,9):
    news_info = soup.select('#epTabTop > ul.topics > li:nth-of-type({0}) > div > p > a'.format(i))
    headline_title.append(news_info[0].text.replace("写真",""))
    headline_url.append(news_info[0].get('href'))

print(headline_title, headline_url)