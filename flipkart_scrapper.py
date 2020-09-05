import bs4
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup as soup
import ssl
import json
import re

# The is to mathc the link with the object
api_key = False

if api_key is False:
    service_url = 'https://www.flipkart.com/search?'

# The is to create a ssl free site
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    value = input('\nEnter the item that you want to search in Flipkart - ')
    q = value.lower()
    if len(q)<1:    # empty search
        print('CLOSING \n')
        break

    raw_search = dict()
    raw_search['q']=q  
    raw_search['ontraker']=('search')  
    raw_search['otracker1']=('search')  
    raw_search['marketplace']=('FLIPKART')  
    raw_search['as-shown']=('on')  
    raw_search['as']=('off')  
    if api_key is not False :
        raw_search['q']=api_key
    url_create = service_url + urllib.parse.urlencode(raw_search)

    print("\nretriving url ----",url_create)

    # url creation complete 

    open_link = urllib.request.urlopen(url_create, context= ctx)
    site_raw_data = open_link.read().decode()
    open_link.close()
    
    fine_data = soup(site_raw_data, 'html.parser')

    
    container_data = fine_data.findAll("div",{'class':'bhgxx2 col-12-12'})
    no_data= len(container_data)
    print("'The total no of data found was = ", no_data)

    # print(container_data)
    print('\n')
    # print(container_data[6])
    

    for k in range (4 , no_data-5):
        print(k)
        contain = container_data[k]
        # name_raw = contain.findAll("div",{'class':'_1-2Iqu row'})
        # name_raw = contain.findAll("div",{'class':'col col-7-12'})
        name_raw = contain.findAll("div",{'class':'_3wU53n'})
        name = name_raw[0].text
        print(name)
        
        price_raw = contain.findAll("div",{'class':'_1vC4OE _2rQ-NK'})
        price = price_raw[0].text
        print('Rs.'+ price)
        
        
        rate_raw = contain.findAll("div",{'class':'hGSR34'})
        rate = rate_raw[0].text
        print(rate)
        print("")


