import csv
import lxml
from bs4 import BeautifulSoup
import requests



urls = ['https://bkrb.ru/catalog/kirpich-keramicheskiy-ryadovoy-polnotelyy/','https://bkrb.ru/catalog/kirpich-silikatnyy/','https://bkrb.ru/catalog/kirpich-oblitsovochnyy/']
for url in urls:
    products = []
    dop_link = 'https://bkrb.ru'
    # for i in range(1,10,1):
    # url = f'https://www.gubskiy-kirpich.ru/shop/page/{i}'
    # print(url) #для проверки что он собирает странички с 1 по 9 с сетками товаров
    req = requests.get(url)
    html = req.text

    # сбор данных
    soup = BeautifulSoup(html, 'lxml')
    product_block = soup.findAll('div', class_='col-6 col-xl-4')

    # print(product_block)

    for i in product_block:
        href = i.find('a', href=True)
        link = href.get('href')
        products.append(dop_link + link)

    # print(len(products)) #len - кол-во объектов внутри списка

    clear_product = list(set(products))  # чистит словарь, выбирает уникальные

    # print(len(clear_product)) #чистый словарь из уникальных значений

    # with open('data.csv', 'a') as f:
    #    writer = csv.writer(f, delimiter=';', lineterminator='\r') #lineterminator - чтобы не было пустых строк между данными которые собрали
    #   for item in clear_product:
    #      writer.writerow([item])

    # print("Готово")

    for k in clear_product:
        req = requests.get(k)
        html1 = req.text
        soup = BeautifulSoup(html1, 'lxml')
        product_name = soup.find('title').text
        product_char = soup.findAll('ul', class_='catalog-inner-char')
        p2 = []
        for i in range(len(product_char)):
            p2.append(product_char[i].text.replace("\n",""))
            row = [product_name.replace("\n",""), p2]
        print(len(row))

        with open('BKRB.csv', 'a', encoding='utf-8-sig') as g:
            writer = csv.writer(g, delimiter=';', lineterminator='\r')
            for item in row:
                writer.writerow([item])
