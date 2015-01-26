#!/usr/bin/env python3
import re
import csv
import xml.etree.ElementTree as etree
from glob import glob
import zenhan

def generalize_address(address):
    print('-'*8)
    print(' ', address)
    
    numeric_table = {
        '一': '1',
        '二': '2',
        '三': '3',
        '四': '4',
        '五': '5',
        '六': '6',
        '七': '7',
        '八': '8',
        '九': '9',
        }

    # 無駄な余白と/を除去
    address = address.strip()
    address = re.sub('\s*/\s*', '', address)
    place = ''

    # ○丁目を変換
    match = re.search(r'((一|二|三|四|五|六|七|八|九|\d+)丁目)', address)
    if match:
        number = match.group(2)
        if not number.isdecimal():
            number = numeric_table[number]
        address = re.sub(match.group(1), number + '-', address)

    # 数字をすべて半角にする
    address = zenhan.z2h(address, mode=(zenhan.ASCII|zenhan.DIGIT))

    # ハイフンを統一
    address = re.sub(r'(ー|−|−|-|－)', r'-', address)

    # 番地と号を消す
    address = re.sub('(番地の|番地|番|号)([^街]?)', r'-\2', address)
    
    match = re.search('''
    (.+?)      # 住所の先頭
    \s*       # スペース
    (\d+[-\dF]*)   # 番地などの数字部分
    \s*       # スペース
    (.*)$      # 店舗名など
    ''', address, re.X)
    
    if match:
        # address
        address = match.group(1)

        # numbers
        numbers = '-'.join([i for i in match.group(2).split('-') if i])
        match_floor = re.search(r'-(\dF)$', numbers)
        floor = ''
        if match_floor:
            floor = match_floor.group(1)
            print('match_floor:', floor)
            numbers = numbers.replace(match_floor.group(), '')        
        address += numbers

        # place
        place = match.group(3)
        place = floor + place
        place = place.replace('-', 'ー')

    return address, place

store_list = []
store_list_coordinates = []

for f in glob('kml/*.kml'):
    tree = etree.parse(f)
    ns = '{http://www.opengis.net/kml/2.2}'
    stores = tree.findall('//{}Placemark'.format(ns))
    for store in stores:
        name = store.find('{}name'.format(ns)).text
        if name:
            name = name.strip()
            name = zenhan.z2h(name, mode=(zenhan.ASCII|zenhan.DIGIT))

        address_orig = store.find('.//{}value'.format(ns)).text
        if address_orig:
            address, place = generalize_address(address_orig)

        coordinates = store.find('.//{}coordinates'.format(ns))
        if coordinates is not None:
            coordinates = ','.join(coordinates.text.split(',')[:2])
        else:
            coordinates = ''

        if coordinates:
            store_record = [name,address_orig,address,place,coordinates]
            store_list_coordinates.append(store_record)
        else:        
            store_record = [name,address_orig,address,place]
            store_list.append(store_record)

        print('*', store_record)

with open('stores_coordinates.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['名前', 'address_orig', '住所', 'お店の場所', '経緯度'])
    writer.writerows(store_list_coordinates)

with open('stores.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['名前', 'address_orig', '住所', 'お店の場所'])
    writer.writerows(store_list)

