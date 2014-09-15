#!/usr/bin/env python3
# Make csv files from shop lists in the official page
import re
from urllib.parse import quote_plus

import requests
from bs4 import BeautifulSoup

BASE_URL = 'http://pripara.jp/shop/search_list?pref_name={}'

# get pref_list
soup = BeautifulSoup(requests.get('http://pripara.jp/shop/').text)
pref_list = [i['value'] for i in soup('option', value=re.compile(r'.+'))]

for pref_num, pref in enumerate(pref_list):
    url = BASE_URL.format(quote_plus(pref))
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    h2 = soup('h2')
    file_number = len(h2) // 100   # max length of one csv is 100 to import to google map lite
    for num in range(file_number+1):
        filename = 'csv/{:02d}-{}-{}.csv'.format(pref_num, pref, num)
        with open(filename, 'w') as f:
            f.write(','.join(['place', 'address']) + '\n')
        start = num * 100
        end = num * 100 + 100
        for i in h2[start:end]:
            shop = i.text
            address = i.find_next('p').text
            address = re.sub(r'玩.{0,5}場', '', address)
            address = re.sub(r'　', '', address)   # avoid import error
            with open(filename, 'a') as f:
                f.write(','.join([shop, address]) + '\n')
