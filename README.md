pripara-map
===========

Codes for Pripara Maps (http://sakuramochi.mydns.jp/pripara/map).

## Code structure

### Main programs

* csvmaker.py - fetch data from the official site to make it into csv in the csv directory. 
* make_html.py - combine csv and template to md files and convert them to html files.

### Other files

* google-map-link.csv - consists of urls of Google Maps in which places of the csv files are manually plotted.
* index-template, pref-header-template, pref-template - are templates for html.
