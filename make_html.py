#!/usr/bin/env python3
# Make html pages from map list
# do following command: ./make_html.py && for i in htmls/*.md; do; md2html $i -h; done && mv *.html html/
import csv

with open('google-map-link.csv') as f:
    f.readline() # skip header
    reader = csv.reader(f)
    
    links = []
    pre_region = ''
    for pref, pref_name, region, mid, ll, z in reader:
        if region != pre_region:
            links.append('\n### {}'.format(region))
            pre_region = region
        links.append('* [{}]({})'.format(pref, pref_name))

        # make pref pages
        with open('html-templates/pref-template') as f:
            template = f.read()
        html = template.format(pref=pref, pref_name=pref_name, mid=mid, ll=ll, z=z)
        filename = 'html-templates/' + pref_name + '.md'
        with open(filename, 'w') as f:
            f.write(html)

        # header
        with open('html-templates/pref-header-template') as f:
            template = f.read()
        html = template.format(pref=pref)
        filename = 'html-templates/' + pref_name + '-header'
        with open(filename, 'w') as f:
            f.write(html)

with open('html-templates/index-template') as f:
    template = f.read()
with open('store_num.txt') as f:
    store_num = f.read()
html = template.format(links='\n'.join(links), store_num=store_num)
with open('html-templates/index.md', 'w') as f:
    f.write(html)

with open('google-map-link-old.csv') as f:
    reader = csv.reader(f)
    
    for prefs, pref_names in reader:
        
        links = []

        for pref, en in zip(prefs.split('/'), pref_names.split('-')):

            links.append('* [{}]({})'.format(pref, en))

            # make pref pages
            with open('html-templates/pref-template-old') as f:
                template = f.read()
            html = template.format(pref=prefs, pref_name=pref_names, links='\n'.join(links))
            filename = 'html-templates/' + pref_names + '.md'
            with open(filename, 'w') as f:
                f.write(html)

            # header
            with open('html-templates/pref-header-template') as f:
                template = f.read()
            html = template.format(pref=prefs)
            filename = 'html-templates/' + pref_names + '-header'
            with open(filename, 'w') as f:
                f.write(html)

