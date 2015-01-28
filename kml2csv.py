#!/usr/bin/env python3
import csv
import xml.etree.ElementTree as etree
from glob import glob

store_list = []
for f in glob('kml/*.kml'):
    tree = etree.parse(f)
    ns = '{http://www.opengis.net/kml/2.2}'
    stores = tree.findall('//{}Placemark'.format(ns))
    for store in stores:
        name = store.find('{}name'.format(ns)).text
        values = [value.text for value in store.findall('.//{}value'.format(ns))][:2]

        if not values[1]:
            values[1] = ''

        coordinates = store.find('.//{}coordinates'.format(ns))
        if coordinates is not None:
            coordinates = coordinates.text.split(',')[:2]
        else:
            coordinates = []

        store_record = [name] + values + coordinates
        store_list.append(store_record)

        print('*', store_record)

with open('stores.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['名前', '住所', 'お店の場所', '経度', '緯度'])
    writer.writerows(store_list)
    print('Wrote {} stores.'.format(len(store_list)))


