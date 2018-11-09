import requests
from bs4 import BeautifulSoup as bs

url = 'https://news.naver.com/'
news = requests.get(url)
html = news.text
soup = bs(html, 'lxml')

headline_title = []
headline_url = []

for i in range(1, 3):
    headline_w_photo = soup.select('#pan_today_main_news > div:nth-of-type({0}) > div > a > div.newsnow_img_mask > p'.format(i))
    headline_w_photo_url = soup.select('#pan_today_main_news > div:nth-of-type({0}) > div > a'.format(i))
    headline_title.append(headline_w_photo[0].text)
    headline_url.append(headline_w_photo_url[0].get('href'))

for idx in range(len(soup.select('#text_today_main_news_801001 > li'))):
    headline_news = soup.select('#text_today_main_news_801001 > li:nth-of-type({0}) > div > a > strong'.format(idx + 1))
    headline_news_url = soup.select('#text_today_main_news_801001 > li:nth-of-type({0}) > div > a'.format(idx + 1))
    headline_title.append(headline_news[0].text)
    headline_url.append(headline_news_url[0].get('href'))

for idx in range(len(soup.select('#text_today_main_news_428288 > li'))):
    headline_news = soup.select('#text_today_main_news_428288 > li:nth-of-type({0}) > div > a > strong'.format(idx + 1))
    headline_news_url = soup.select('#text_today_main_news_428288 > li:nth-of-type({0}) > div > a'.format(idx + 1))
    headline_title.append(headline_news[0].text)
    headline_url.append(headline_news_url[0].get('href'))

print(headline_title, headline_url)

