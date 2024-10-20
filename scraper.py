# bismillah
# started project on 12-04-1446/16-10-2024

from bs4 import BeautifulSoup as bs4
from selenium import webdriver
from pathlib import Path
import pandas as pd
import numpy as np
import time

def findCars(soup = bs4) -> int:
    count = 0
    listings = soup.find_all('li', class_ = "classified-listing featured-listing managed-pw") + soup.find_all('li', class_ = "classified-listing featured-listing") + soup.find_all('li', class_ = "classified-listing")
    # print(listings)
    # print("BRUB BRRUH BRUH BUHBR BRUH BRUH BURB BURBB BUHRB UBRB")

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

        print(str(index+1) + f'] - {name}')
        print(f'price: {price.replace(',', "")}')
        print(f'city: {city}')
        print(f'production year: {bits[0]}')
        print(f'driven (kilometers): {bits[1].replace('km', "").replace(',', "").strip()}')
        print(f'engine type: {bits[2]}')
        print(f'horsepower (CC): {bits[3].replace('cc', "")}')
        print(f'transmission: {bits[4]}')
        print(f'link: pakwheels.com{link}\n')
        count += 1
    print("Listings from Page Completed!")
    print(f"Total cars in the Page: {count}\n\n")
    return count

def scrapePages(link = str) -> int:
    url = link
    total = 0

    while True:
        driver =  webdriver.Edge()
        driver.get(url)
        print("waiting for page to completely load.")
        time.sleep(10)

        soup = bs4(driver.page_source, 'lxml')
        next_page = soup.find('li', class_ = "next_page")
        # print(next_page) # prints 'None' if no next_page
        total += findCars(soup)

        if next_page == None:
            print("No more listings available!")
            return total
        else:
            url = 'https://www.pakwheels.com' + next_page.a['href']
            print(url)

if __name__ == '__main__':
    total_cars = scrapePages('https://www.pakwheels.com/used-cars/search/-/ct_taxila/')
    print(f'The total number of cars for your search criteria right now are: {total_cars}')

# url = 'https://www.pakwheels.com/used-cars/search/-/?page=1'
# driver =  webdriver.Edge()
# driver.get(url)

# soup = bs4(driver.page_source, 'lxml')
# error = soup.find('div', class_ = "row error-block-head")
# print(error) # prints 'None' if not found, meaning not error page

# 'div', class = "row error-block-head"