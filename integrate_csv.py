#!/usr/bin/env python3
from glob import glob
import csv
from kml2csv import generalize_name, generalize_address

stores_2014 = []
with open('csv/stores_2014.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        name = row[0]
        stores_2014.append(name)

stores_2014_coordinates = []
with open('csv/stores_2014_coordinates.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        name = row[0]
        stores_2014_coordinates.append(name)
    
new_stores_names = []
new_stores = []
for file in glob('csv/*-*.csv'):
    with open(file) as f:
        reader = csv.reader(f)
        for row in reader:
            name = generalize_name(row[0])
            address, place = generalize_address(row[1])
            if (name not in stores_2014) and (name not in stores_2014_coordinates) and (name not in new_stores_names) and (name != 'place'):
                print('! new:', name)
                new_stores_names.append(name)
                new_stores.append([name, address, place])
            else:
                print('# old:', name)

print(len(new_stores))

with open('csv/stores_2015_01.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['名前', '住所', 'お店の場所'])
    writer.writerows(new_stores)
