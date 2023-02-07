from bs4 import BeautifulSoup
import requests


res = requests.get("https://kun.uz/")


soup = BeautifulSoup(res.content,"html.parser")

block = soup.find("div", class_="col-md-3")
print(block.text)
news_lenta = soup.find_all("a", class_="news-lenta")

for i in news_lenta:
    print(i.text)

countries = soup.find("div", class_="countries-list")
print(countries.text)