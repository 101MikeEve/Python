# Код для парсинга сайта и записи данных в CSV-файл

import requests
from bs4 import BeautifulSoup as BS
import csv
import asyncio
import aiohttp

# Ссылка на сайт для парсинга
LINK1 = "https://xn-----6kcchdobcrffeabaodndk4ch3arzuz1nze.xn--p1ai/#"

# Названия столбцов в CSV-файле
field_names = ["Производитель", "Наименование", "Марка"]

async def main():
    # Создание сессии для работы с сайтом
    async with aiohttp.ClientSession() as session:
        # Отправка запроса на сайт и получение ответа
        async with session.get(LINK1) as response:
            # Чтение содержимого ответа
            r = await response.content.read()
            # Создание объекта BeautifulSoup для парсинга HTML
            soup = BS(r, "html.parser")

            # Поиск всех элементов div с классом col-md-6
            items = soup.find_all("div", {"class": "col-md-6"})
            # Поиск таблицы на странице
            table = soup.find('table')
            # Открытие CSV-файла для записи данных
            with open('fki.csv', 'a', encoding='utf-8-sig') as f:
                # Создание объекта writer для записи в CSV-файл с разделителем ","
                writer = csv.writer(f, delimiter=",")
                # Запись названий столбцов в первую строку файла
                writer.writerow(field_names)
                # Парсинг данных из элементов div
                for item in items:
                    # Поиск наименования товара
                    title = item.find("a", {"class": "cardName"}).text.strip()
                    # Создание списка данных для записи в CSV-файл
                    row = [title.strip()]
                    # Поиск и добавление остальных данных в список
                    for td in item.find_all("td"):
                        row.append(td.text.strip())
                    # Запись списка данных в CSV-файл
                    writer.writerow(row)
                # Парсинг данных из таблицы
                for tr in table.find_all("tr"):
                    row = []
                    for td in tr.find_all("td"):
                        row.append(td.text.strip())
                    writer.writerow(row)

if __name__ == '__main__':
    # Создание и запуск цикла событий asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())