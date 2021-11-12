import requests
import json
from bs4 import BeautifulSoup
import argparse
from requests.models import CONTENT_CHUNK_SIZE

if __name__ =='__main__':    

    parser = argparse.ArgumentParser(description='Get ebay product data by search term')
    parser.add_argument('searchterm')
    args = parser.parse_args()
    print('args.searchterms', args.searchterm)
    items=[]

    for pg in range(1,11):
        
        url = 'https://www.ebay.com/sch/i.html?_from=R40&_sacat=0&_nkw=' + args.searchterm + '&_sop=20&_pgn=' + str(pg) +'&rt=nc'
        
        x = requests.get(url)
        html = x.text

        soup = BeautifulSoup(html,'html.parser')

        products = soup.select(".s-item")
        for product in products:
            
            #extract the name
            name = None
            names = product.select(".s-item__title")
            for i in names:
                name = i.text
            
            #extract the free returns
            freereturn = False
            freereturns = product.select('.s-item__free-returns')
            for i in freereturns:
                freereturn = True
            
            itemssold = None
            itemssolds = product.select('.s-item__hotness')
            for i in itemssolds:
                output = ''
                for num in i.text:
                    if num in '0123456789':
                        output += num
                if 'sold'in i.text:
                    itemssold = int(output)
                else:
                    itemssold = 0


            status = None
            statuses = product.select(".SECONDARY_INFO")
            for i in statuses:
                status = i.text

            shipping = None
            shippings = product.select(".s-item__shipping, .s-item__logisticsCost")
            for i in shippings:
                    output = ''
                    for num in i.text:
                        if num in '1234567890':
                            output+= num
                    if "Free shipping" in i.text or len(output)<2:
                        shipping = 0
                    else:
                        shipping = int(output)
            
            price = None
            prices = product.select(".s-item__price")
            for i in prices:
                    output = ''
                    for num in i.text:
                        if num == 't':
                            break
                        if num in '0123456789':
                            output += num
                    if not output:
                        price = None
                    else:
                        price = int(output)

            
            item = {
                'name': name,
                'free_returns': freereturn,
                'items_sold': itemssold,
                'status': status,
                'shipping': shipping,
                'price': price
            } 

            items.append(item)

    filename = args.searchterm +'.json'
    with open (filename, 'w', encoding= 'ascii') as f:
        f.write(json.dumps(items))