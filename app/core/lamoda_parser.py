import httpx
from bs4 import BeautifulSoup

from services.mongo import MongoDBService


async def parse_lamoda(category_url):
    async with httpx.AsyncClient() as client:
        response = await client.get(category_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            mongo_service = MongoDBService()  # Instantiate the MongoDB service

            products = soup.find_all('div', class_='x-product-card__card')

            for product in products:
                name = product.find('div', class_='x-product-card-description__product-name').text.strip()
                brand = product.find('div', class_='x-product-card-description__brand-name').text.strip()
                try:
                    price = product.find('span', class_='x-product-card-description__price-single').text.strip()
                except AttributeError:
                    price = product.find('span', class_='x-product-card-description__price-new').text.strip()

                # Insert the parsed data into MongoDB
                mongo_service.insert_document("lamoda_products", {"name": name, "brand": brand, "price": price})
        else:
            print("Page Not Found")