import bs4
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup as soup
import ssl
import json
import re

# The is to mathc the link with the object
api_key = False

if api_key is False:
    service_url = 'https://www.amazon.in/s?'
    look_up_url='https://www.barcodelookup.com/'


# The is to create a ssl free site
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    value = input('\nEnter the item that you want to search in amazon - ')
    k = value.lower()
    if len(k)<1:    # empty search
        print('CLOSING \n')
        break

    raw_search = dict()
    raw_search['k']= k
    raw_search['ref']=('nb_sb_noss')
    if api_key is not False :
        raw_search['k']=api_key
    url_create = service_url + urllib.parse.urlencode(raw_search)

    print("\nretriving url ----",url_create)

    # url creation complete 

    open_link = urllib.request.urlopen(url_create, context= ctx)
    site_raw_data = open_link.read().decode()
    open_link.close()

    # print('\n retrived data \n',len(site_raw_data ))
    # print('')

    fine_data = soup(site_raw_data, 'html.parser')

    container_data = fine_data.findAll("div",{'class':'a-section a-spacing-medium'})
    no_data=len(container_data)
    print('The total numebr of data found = ',no_data)
    # print(container_data)
    # print(container_data[0])
   
    print('\n')


    # filename = "product.csv"
    # f = open(filename, "w")
    # header = "Name , Price(RS), Rating(out of 5)\n"
    # f.write(header)

    for k in range(no_data):
        print(k)
        contain = container_data[k]

        # get the name of the product 
        name_raw = contain.findAll("span",{'class':'a-size-medium a-color-base a-text-normal'})
        # print(name_raw)
        name = name_raw[0].text
        print(name)
    
        price_raw=contain.findAll('span',{'class':'a-price-whole'})
        # print(price_raw)
        price = price_raw[0].text
        print('Rs.'+ price)

        rate_raw=contain.findAll('span',{'class':'a-icon-alt'})
        # print(rate_raw)
        rate = rate_raw[0].text
        print(rate)
        print("")
        # f.write(name.replace(',', " ") +','+price.replace(',', "") +','+rate +'\n')

    print("SEARCHING GLOBAL TRADE ITEM NUMBER (GTIN)")



# f.close()