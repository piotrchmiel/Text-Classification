__author__ = 'Piotr'

import feedparser
import urllib
from bs4 import BeautifulSoup

d = feedparser.parse('http://sports.yahoo.com/mlb/rss.xml')

url = urllib.parse.unquote(d.entries[0]['link'].split('*')[1])

print(url)

try:
    page = urllib.request.urlopen(url)
except:
    print(url)
else:
    from selenium import webdriver
    soup = BeautifulSoup(page.read().decode('utf8'))
    print (soup.title.string)
    body = soup.find("div", class_="body")
    for tag in body.find_all("p"):
        print(tag.getText())

    browser = webdriver.Firefox()
    browser.get(url)
    html_source = browser.page_source
    browser.close()
    soup = BeautifulSoup(html_source)
    section = soup.find("section", id="mediacontentrelatedstory")

    for tag in soup.find("section", id="mediacontentrelatedstory").findAll('a', href=True):
        print((url.split('/'))[2] + tag['href'])



