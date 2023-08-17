import csv
import lxml
from bs4 import BeautifulSoup
import requests
import asyncio
import aiohttp

products = []
field_names = ["Наименование", "Характеристики"]


url = 'https://kraska.starateli.ru/'
#print(url) #для проверки что он собирает странички с 1 по 9 с сетками товаров
req = requests.get(url)
html = req.text

#сбор данных
soup = BeautifulSoup(html, 'lxml')
product_block = soup.findAll("div", class_="product-name")

#print(product_block)

for i in product_block:
    href = i.find_all('a', href = True)
    for link in href:
        link = link.get('href')
        products.append(link)



#print(len(products)) #len - кол-во объектов внутри списка

clear_product = list(set(products)) #чистит словарь, выбирает уникальные

#print(len(clear_product)) #чистый словарь из уникальных значений

#with open('data.csv', 'a') as f:
#    writer = csv.writer(f, delimiter=';', lineterminator='\r') #lineterminator - чтобы не было пустых строк между данными которые собрали
 #   for item in clear_product:
  #      writer.writerow([item])

#print("Готово")

for k in clear_product:
    req = requests.get(k)
    html1 = req.text
    soup = BeautifulSoup(html1, 'lxml')
    product_name = soup.find('h1')
    product_char = soup.findAll('td')
    p2 = []
    for i in range(len(product_char)):
        p2.append(product_char[i].text)
    row = [product_name.text.strip(), p2]
    print(len(row))


    with open('starateli.csv', 'a', encoding='utf-8-sig') as g:
        writer = csv.writer(g, delimiter=';', lineterminator='\r')
        for item in row:
            writer.writerow([item])