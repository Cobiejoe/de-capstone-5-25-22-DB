import random
from bs4 import BeautifulSoup
import requests
from generate_ids import generate_ids


def webscrape_product_data(url_list):

    data = []

    for url in url_list:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        product_items = soup.find_all('div', class_='productBlock', limit=25)

        product_type = soup.find('h1', class_='responsiveProductListHeader_title').text.replace('\n', '')

        for item in product_items:
            product_id = generate_ids()
            product_type = product_type
            product_name = item.find('h3', class_='productBlock_productName').text.replace('\n', '')
            product_price = item.find('span', class_='productBlock_priceValue').text.replace('\n', '')
            stock_quantity = random.randint(0, 100)
            data.append([product_id, product_type, product_name, product_price, stock_quantity])

    return data