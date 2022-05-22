# requests library used to fetch the content from the URL given
import requests
# beautiful soup library used to fetch data using Html tag, class, id, css selector and many more ways.
from bs4 import BeautifulSoup

url = "https://www.patanjaliayurved.net/category/natural-food-products/2"

response = requests.get(url)
# The get() method sends a GET request to the specified url
print(response.status_code)

soup = BeautifulSoup(response.content, 'lxml')
# lxml is a Python library which allows for easy handling of XML and HTML files
# print(soup)

divs = soup.find_all('div', {'class': "col-md-9 col-sm-9 col-xs-12 filter-sidebar-box-right"})
print(divs)

names = divs[0].find_all('a', {'class': "product-name tool_tip"})
print(names)

product_names = [name.string.strip() for name in names]
print(product_names)

prices = divs[0].find_all('p', {'class': "product-price"})
print(prices)

product_prices = [price.string.strip() for price in prices]
print(product_prices)

weights = divs[0].find_all('div', {'class': "block-name list-page-blog-name"})
product_weights = [weight.text.strip() for weight in weights]
print(product_weights)

import re

weight_list = []
for i in range(len(product_weights)):
    a = product_weights[i].find("\n")
    b = product_weights[i].find("Rs")
    c = product_weights[i][:b]
    d = c[a+110:]
    d = re.sub("\xa0", " ", d)
    weight_list.append(d.strip())
print(weight_list)

# urlopen function is able to fetch URLs using a variety of different protocols.
from urllib.request import urlopen

image_links = []
htmldata = urlopen('https://www.patanjaliayurved.net/category/natural-food-products/2')
soups = BeautifulSoup(htmldata, 'html.parser')
images = soups.find_all('img', {'class': 'img-responsive'})
  
for item in images:
    image_links.append(item['src'])

print(image_links)

product_links = []
links = soups.find_all('a', {'class': 'figure-href'})
  
for link in links:
    product_links.append(link['href'])

print(product_links)

import pandas as pd

products = pd.DataFrame()
products['Product_Names'] = product_names
products['Images'] = image_links
products['Product Type'] = "Natural Food Products"
products['Weight'] = weight_list
products['Price'] = product_prices
products['Products Links'] = product_links

print(products)
