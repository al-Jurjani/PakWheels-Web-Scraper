# bismillah
# started project on 12-04-1446/16-10-2024
# project ended on 18-04-1446/21-10-2024
# alhumdulillah

from bs4 import BeautifulSoup as bs4
from selenium import webdriver
import time
from typing import List
import csv

# called by scrapePages()
def findCars(soup = bs4) -> List[str]:
    count = 0
    listings = soup.find_all('li', class_ = "classified-listing featured-listing managed-pw") + soup.find_all('li', class_ = "classified-listing featured-listing") + soup.find_all('li', class_ = "classified-listing")
    # I found three types of listings, perhaps they may be more types.

    data = [
        ['name', 'price', 'city', 'production_year', 'km_driven', 'engine_type', 'horsepower', 'transmission', 'link']
    ]

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
        bits = info.split("\n") # prod year, km_driven, engine_type, horsepower, transmission

        tuple = ['', '', '', '', '', '', '', '', '']
        tuple[0] = name
        tuple[1] = price.replace(',', "")
        tuple[2] =  city
        tuple[3] =  bits[0]
        tuple[4] =  bits[1].replace('km', "").replace(',', "").strip()
        tuple[5] =  bits[2]
        tuple[6] = bits[3].replace('cc', "")
        tuple[7] =  bits[4]
        tuple[8] =  'pakwheels.com' + link
        data.append(tuple)
        count += 1
    print("Listings from Page Completed!")
    print(f"Total cars in the Page: {count}\n\n")
    return data

def scrapePages(link = str) -> int:
    url = link
    total = 0
    data = []

    while True:
        driver =  webdriver.Edge()
        driver.get(url)
        print("waiting for page to completely load.")
        time.sleep(10)

        soup = bs4(driver.page_source, 'lxml')
        next_page = soup.find('li', class_ = "next_page")
        # print(next_page) # prints 'None' if no next_page
        search = soup.find('div', class_ = "used-car-search-results").h1.text
        data = findCars(soup)

        if total == 0: # creating new file
            with open(f'files/{search.replace(' ', '_')}.csv', mode = 'w', newline = '') as file:
                writer = csv.writer(file)
                writer.writerows(data)
        else: # file already exists, need to append it
            with open(f'files/{search.replace(' ', '_')}.csv', mode = 'a', newline = '') as file:
                writer = csv.writer(file)
                writer.writerows(data)

        total += len(data)
        if next_page == None:
            print("No more listings available!")
            return total
        else:
            url = 'https://www.pakwheels.com' + next_page.a['href']
            # print(url)

if __name__ == '__main__':
    total_cars = scrapePages('https://www.pakwheels.com/used-cars/search/-/mk_toyota/tr_automatic/cert_pakwheels-certified/')
    print(f'The total number of cars for your search criteria right now are: {total_cars - 1}')