#!/usr/bin/env python3
# Make html pages from map list
# do following command: ./make_html.py && for i in *.md; do; md2html $i -h; done && mv *.html html/
import csv

with open('google-map-link.csv') as f:
    f.readline() # skip header
    reader = csv.reader(f)
    
    links = []
    pre_region = ''
    for pref, pref_name, region, mid in reader:
        if region != pre_region:
            links.append('\n### {}'.format(region))
            pre_region = region
        links.append('* [{}]({})'.format(pref, pref_name))

        # make pref pages
        with open('pref-template') as f:
            template = f.read()
        html = template.format(pref=pref, pref_name=pref_name, mid=mid)
        filename = pref_name + '.md'
        with open(filename, 'w') as f:
            f.write(html)

        # header
        with open('pref-header-template') as f:
            template = f.read()
        html = template.format(pref=pref)
        filename = pref_name + '-header'
        with open(filename, 'w') as f:
            f.write(html)

    with open('index-template') as f:
        template = f.read()
    with open('store_num.txt') as f:
        store_num = f.read()
    html = template.format(links='\n'.join(links), store_num=store_num)
    with open('index.md', 'w') as f:
        f.write(html)

