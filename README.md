pripara-map
===========

Codes for Pripara Maps (http://sakuramochi.mydns.jp/pripara/map).

## Code structure


### Main programs

* csvmaker.py - fetch data from the official site to make it into csv in the csv directory. 
* make_html.py - Combine csv and template to md files and convert them to html files.

### Other files

* google-map-link.csv - urls of Google Maps manually plotted places in the csv files.
* index-template, pref-header-template, pref-template - templates for html.
