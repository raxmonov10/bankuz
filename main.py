from bs4 import BeautifulSoup
import requests

res = requests.get("https://kun.uz")

soup = BeautifulSoup(res.content, "html.parser")
block = soup.find('span', class_="news-lenta__title")

entry_content = block.find('div', class_="entry-content")




print(block.text)