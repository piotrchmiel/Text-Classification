__author__ = 'Piotr Chmiel'

from bs4 import BeautifulSoup
from selenium import webdriver
import urllib

def get_html_content(url):
    try:
        webpage = urllib.request.urlopen(url)
    except:
        print("Connection error " + url)
        return ""
    else:
        return webpage.read().decode('utf8')

class YahooParser():
    def __str__(self):
        return "Yahoo Parser"

    def __init__(self, url):
        self.url = url
        self.soup = BeautifulSoup(get_html_content(self.url))

    def get_title(self):
        return self.soup.title.string

    def get_article(self):
        article_body = self.soup.find("div", class_="body")
        if article_body != None:
            subparagraphs_tags = article_body.find_all("p")
            if subparagraphs_tags != []:
                return "\n".join([paragraph_tag.getText() for paragraph_tag in subparagraphs_tags])
            else:
                return None
        else:
            return None

    def get_related_articles(self, browser):

        browser = webdriver.Firefox()
        browser.get(self.url)
        html_source = self.browser.page_source
        browser.close()

        related_article_soup = BeautifulSoup(html_source)
        section = related_article_soup.find("section", id="mediacontentrelatedstory")
        if section != None:
            return [self.url.split('/')[2] + tag['href'] for tag in section.findAll('a', href=True) if "http" not in tag]
        else:
            return []