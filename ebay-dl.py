from bs4 import BeautifulSoup
import requests
import argparse
import json

parser = argparse.ArgumentParser(description='Scrape Ebay Items by Search')
parser.add_argument('search', metavar='search', type=str, help='what item you are looking to scrape')
args = parser.parse_args()
term = args.search
search = 'https://www.ebay.com/sch/i.html?_from=R40&_sacat=0&_nkw=' + term.replace(' ', '+') + '&_sop=20&_pgn='
r = requests.get(search)
text = r.text
dict1 = {"names": [], "prices": [], "statuses": [], "shippings": [], "free_returnses": [], "items_solds": []}
for page in range(1, 10):

    page = requests.get(search + str(page))
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

with open(term.replace(' ', '+') + '.json', 'w') as fp:
    json.dump(dict1, fp)
