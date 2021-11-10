from bs4 import BeautifulSoup
import requests
import argparse
import json

dict1 = {"names": [], "prices": [], "statuses": [], "shippings": [], "free_returnses": [], "items_solds": []}
dict2 = {"names": [], "prices": [], "statuses": [], "shippings": [], "free_returnses": [], "items_solds": []}
dict3 = {"names": [], "prices": [], "statuses": [], "shippings": [], "free_returnses": [], "items_solds": []}
for page in range(1, 10):

    page = requests.get('https://www.ebay.com/sch/i.html?_from=R40&_sacat=0&_nkw=rick+owens&_sop=20&_pgn=' + str(page))
    soup = BeautifulSoup(page.text, 'html.parser')

    names = soup.find_all('h3', class_='s-item__title')
    prices = soup.find_all('span', class_='s-item__price')
    statuses = soup.find_all('span', class_='SECONDARY_INFO')
    shippings = soup.find_all('span', class_='s-item__shipping s-item__logisticsCost')
    free_returnses = soup.find_all('span', class_='s-item__free-returns s-item__freeReturnsNoFee')
    items_solds = soup.find_all('span', class_='s-item__hotness s-item__itemHotness')

    for name in names:
        dict1['names'].append(name.text)
    for price in prices:
        dict1['prices'].append(price.text)
    for status in statuses:
        dict1['statuses'].append(status.text)
    for shipping in shippings:
        dict1['shippings'].append(shipping.text)
    for free_returns in free_returnses:
        dict1['free_returnses'].append(free_returns.text)
    for items_sold in items_solds:
        dict1['items_solds'].append(items_sold.text)

with open('Rick_Owens.json', 'w') as fp:
    json.dump(dict1, fp)

for page in range(1, 10):

    page = requests.get('https://www.ebay.com/sch/i.html?_from=R40&_sacat=0&_nkw=maison+margiela&_sop=20&_pgn=' + str(page))
    soup = BeautifulSoup(page.text, 'html.parser')

    names = soup.find_all('h3', class_='s-item__title')
    prices = soup.find_all('span', class_='s-item__price')
    statuses = soup.find_all('span', class_='SECONDARY_INFO')
    shippings = soup.find_all('span', class_='s-item__shipping s-item__logisticsCost')
    free_returnses = soup.find_all('span', class_='s-item__free-returns s-item__freeReturnsNoFee')
    items_solds = soup.find_all('span', class_='s-item__hotness s-item__itemHotness')

    for name in names:
        dict2['names'].append(name.text)
    for price in prices:
        dict2['prices'].append(price.text)
    for status in statuses:
        dict2['statuses'].append(status.text)
    for shipping in shippings:
        dict2['shippings'].append(shipping.text)
    for free_returns in free_returnses:
        dict2['free_returnses'].append(free_returns.text)
    for items_sold in items_solds:
        dict2['items_solds'].append(items_sold.text)
    with open('Maison_Margiela.json', 'w') as fp:
        json.dump(dict2, fp)

for page in range(1, 10):

    page = requests.get('https://www.ebay.com/sch/i.html?_from=R40&_sacat=0&_nkw=bathing+ape&_sop=20&_pgn=' + str(page))
    soup = BeautifulSoup(page.text, 'html.parser')

    names = soup.find_all('h3', class_='s-item__title')
    prices = soup.find_all('span', class_='s-item__price')
    statuses = soup.find_all('span', class_='SECONDARY_INFO')
    shippings = soup.find_all('span', class_='s-item__shipping s-item__logisticsCost')
    free_returnses = soup.find_all('span', class_='s-item__free-returns s-item__freeReturnsNoFee')
    items_solds = soup.find_all('span', class_='s-item__hotness s-item__itemHotness')

    for name in names:
        dict3['names'].append(name.text)
    for price in prices:
        dict3['prices'].append(price.text)
    for status in statuses:
        dict3['statuses'].append(status.text)
    for shipping in shippings:
        dict3['shippings'].append(shipping.text)
    for free_returns in free_returnses:
        dict3['free_returnses'].append(free_returns.text)
    for items_sold in items_solds:
        dict3['items_solds'].append(items_sold.text)
    with open('Bathing_Ape.json', 'w') as fp:
        json.dump(dict3, fp)
