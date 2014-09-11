#!/usr/bin/env python3
# Make html pages from map list
# do following command: ./make_html.py && for i in *.md; do; md2html $i -h; done && mv *.html html/
import csv
import glob
import subprocess
import os

with open('google-map-link.csv') as f:
    f.readline() # skip header
    reader = csv.reader(f)
    
    links = []
    for pref, pref_name, mid in reader:
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
    html = template.format(links='\n'.join(links))
    with open('index.md', 'w') as f:
        f.write(html)

    # convert md to html by md2html
    for i in glob.glob('*.md'):
        basename = os.path.splitext(i)[0]
        commands = ['md2html', i, '-h', basename + '-header']
        subprocess.call(commands)

    # move html files to html/
    for i in glob.glob('*.html'):
        os.rename(i, 'html/' + i)

    # clean files
    # for i in glob.glob('*.md'):
    #     os.remove(i)
    # for i in glob.glob('*.html'):
    #     os.remove(i)
    # for i in glob.glob('*-header'):
    #     os.remove(i)
    
