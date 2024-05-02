from bs4 import BeautifulSoup
from lxml import etree 
import requests


URL = 'https://www.nutritionvalue.org'
SEARCH = '/search.php?food_query='
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36'
headers = {'User-Agent': user_agent}

food_name = input('Enter food name: ')

content = requests.get(URL+SEARCH+food_name, headers=headers).text
soup = BeautifulSoup(content, "html.parser")

link = soup.find("a", {"class": "table_item_name"}).get("href")
content = requests.get(URL+link+'?size=100+g', headers=headers).text
soup = BeautifulSoup(content, "html.parser")
dom = etree.HTML(str(soup))



text = soup.find("td", {"class": "desc"}).getText()


print(text)

