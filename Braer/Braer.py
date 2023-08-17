import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

dict_sample = {}
all_dict = {}
for n in range(1,5):
    url = "https://braer.ru/products-category?category=kirpich&url=category&page={}&filters=%7B%221%22:%7B%22model%22:1,%22name%22:%22%22,%22type%22:%221%22,%22value%22:%22%22,%22values%22:true%7D,%222%22:%7B%22model%22:2,%22name%22:%22%22,%22type%22:%221%22,%22value%22:%22%22,%22values%22:true%7D,%223%22:%7B%22model%22:3,%22name%22:%22%22,%22type%22:%221%22,%22value%22:%22%22,%22values%22:true%7D%7D".format(n)

    dict_sample = {}

    response = requests.get(url).json()
    response2 = response['data']
    for i in range(len(response2)):
        link = response2[i]['link']
        req = requests.get(link).text
        soup = BeautifulSoup(req, 'lxml')

        product_name = soup.find('h1').text
        product_chars = soup.findAll('div', class_='param_value')
        char_name_txt = []
        char_value_txt = []
        for product in product_chars:
            char_value_txt.append(product.text)
        char_names = soup.findAll('div', class_='param_label')

        for char_name in char_names:
            char_name_txt.append(char_name.text)

        for k in range(len(char_name_txt)):
            dict_sample[char_name_txt[k].replace('\n','')] = char_value_txt[k].replace('\n','')
            all_dict[product_name.replace('\n','')] = dict_sample
