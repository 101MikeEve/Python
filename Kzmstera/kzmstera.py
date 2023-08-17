import requests
from bs4 import BeautifulSoup as BS
import csv
import asyncio
import aiohttp

LINK1 = "https://www.kzmstera.ru/"

# Названия столбцов в CSV-файле
field_names = ["Наименование", "Марка", "Масса и размер"]


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(LINK1) as response:
            r = await response.content.read()
            soup = BS(r, "html.parser")
            items = soup.find_all("div", {"class": "col-md-6"})
            table = soup.find('table')
            with open('sw_data_new.csv', 'a', encoding='utf-8-sig') as f:
                writer = csv.writer(f, delimiter=",")
                writer.writerow(field_names)

                for item in items:
                    title = item.find("a", {"class": "cardName"}).text.strip()
                    row = [title.strip()]
                    for td in item.find_all("td"):
                        row.append(td.text.strip())
                    writer.writerow(row)
                for tr in table.find_all("tr"):
                    row = []
                    for td in tr.find_all("td"):
                        row.append(td.text.strip())
                    writer.writerow(row)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())