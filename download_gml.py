#!/usr/bin/env python3
import re
from bs4 import BeautifulSoup; import requests
from selenium import webdriver

br = webdriver.Chrome()

# login to google
br.get('http://google.com')
br.find_element_by_link_text('ログイン').click()
br.find_element_by_id('Email').send_keys('sakuramochi.mochi.0\t***REMOVED***\n')

# get map links
br.get('http://sakuramochi.mydns.jp/pripara/map/')
soup = BeautifulSoup(br.page_source)
soup.select('li a')[1:]
links = [i['href'] for i in soup.select('li a')[1:]]

# download gml
for link in links:
    br.get('http://sakuramochi.mydns.jp/pripara/map/' + link)
    soup = BeautifulSoup(br.page_source)
    url = soup.select('a')[1]['href'].replace('viewer', 'edit')
    br.get(url)

    br.find_element_by_id('map-action-menu').click()
    br.find_element_by_id('mapmenu-kmlexport').click()
    br.find_element_by_name('download').click()
