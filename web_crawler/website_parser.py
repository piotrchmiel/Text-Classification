__author__ = 'Piotr Chmiel'
import re
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

class DefaultParser(object):
    def __str__(self):
        return "Yahoo Parser"

    def __init__(self, url):
        self.url = url
        self.soup = BeautifulSoup(get_html_content(self.url))

    def get_title(self):
        return self.soup.title.string

    def get_related_articles(self):
        return []

    def get_article(self):
        subparagraphs_tags = self.soup.find_all("p")
        if subparagraphs_tags:
            return "\n".join([paragraph_tag.getText().strip() for paragraph_tag in subparagraphs_tags])
        else:
            return None


class YahooParser(DefaultParser):
    def __str__(self):
        return "Yahoo Parser"

    def __init__(self, url):
        super().__init__(url)

    def get_title(self):
        return re.sub("- Yahoo.+","",self.soup.title.string).strip()

    def get_article(self):
        article_body = self.soup.find("div", class_="body")
        if article_body != None:
            subparagraphs_tags = article_body.find_all("p")
            if subparagraphs_tags:
                return "\n".join([paragraph_tag.getText().strip() for paragraph_tag in subparagraphs_tags])
            else:
                return None
        else:
            return None

    def get_related_articles(self):

        browser = webdriver.Firefox()
        browser.get(self.url)
        html_source = self.browser.page_source
        browser.close()

        related_article_soup = BeautifulSoup(html_source)
        section = related_article_soup.find("section", id="mediacontentrelatedstory")
        if section is not None:
            return [self.url.split('/')[2] + tag['href'] for tag in section.findAll('a', href=True) if "http" not in tag]
        else:
            return []


class ReutersParser(DefaultParser):

    def __str__(self):
        return "ReutersParser"

    def __init__(self, url):
        super().__init__(url)

    def get_title(self):
        return self.soup.find("h1", class_="article-headline").getText()

    def get_article(self):
        article_body = self.soup.find("span", id="articleText")
        if article_body is not None:
            subparagraphs_tags = article_body.find_all("p")
            if subparagraphs_tags:
                return "\n".join([paragraph_tag.getText().strip() for paragraph_tag in subparagraphs_tags])
            else:
                return None
        else:
            return None
