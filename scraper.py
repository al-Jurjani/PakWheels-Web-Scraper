# bismillah
# started project on 12-04-1446/16-10-2024

from bs4 import BeautifulSoup as bs4
from selenium import webdriver
from pathlib import Path
import pandas as pd
import numpy as np
import time

url = 'https://www.pakwheels.com/used-cars/search/-/'
driver =  webdriver.Edge()
driver.get(url)
print("waiting")
time.sleep(10)

soup = bs4(driver.page_source, 'lxml')
listings = soup.find_all('div', class_ = "well search-list clearfix ad-container page-")

for index, car in enumerate(listings):
    name = car.find('a', class_ = "car-name ad-detail-path")['title']
    link = car.find('a', class_ = "car-name ad-detail-path")['href']
    price = car.find('div', class_ = "price-details generic-dark-grey").text.strip()
    price = price.replace('PKR ', "")
    price = price.replace('.', "")
    if 'lacs' in price:
        price = price.replace(' lacs', '00000')
    elif 'crore' in price:
        price = price.replace(' crore', '000000')
    city = car.find('ul', class_ = "list-unstyled search-vehicle-info fs13").text.strip()
    info = car.find('ul', class_ = "list-unstyled search-vehicle-info-2 fs13").text.strip()
    bits = info.split("\n")

    print(str(index) + f'] - {name}')
    print(f'price: {price.replace(',', "")}')
    print(f'city: {city}')
    print(f'production year: {bits[0]}')
    print(f'driven (kilometers): {bits[1].replace('km', "").replace(',', "").strip()}')
    print(f'engine type: {bits[2]}')
    print(f'horsepower (CC): {bits[3].replace('cc', "")}')
    print(f'transmission: {bits[4]}')
    print(f'link: pakwheels.com{link}\n')