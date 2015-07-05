__author__ = 'Piotr Chmiel'

from bs4 import BeautifulSoup
from re import sub
from selenium import webdriver
from urllib.request import urlopen

def get_html_content(url):
    try:
        webpage = urlopen(url, timeout=60)
    except Exception as err:
        print("Connection error " + url + "\n" + err)
        return ""
    else:
        try:
            return webpage.read().decode(encoding='UTF-8', errors="replace")
        except:
            return ""


class IParser(object):

    def get_title(self):
        if self.soup.title is not None:
            return self.soup.title.string
        else:
            return None

    def get_related_articles(self):
        return []

    def get_article(self):
        subparagraphs_tags = self.soup.find_all("p")
        if subparagraphs_tags:
            return "\n".join([paragraph_tag.getText().strip()
                              for paragraph_tag in subparagraphs_tags])
        else:
            return None

class DefaultParser(IParser):
    def __str__(self):
        return "Default Parser"

    def __init__(self, url):
        self.url = url
        self.soup = BeautifulSoup(get_html_content(self.url))

class DefaultSeleniumParser(IParser):
    def __str__(self):
        return "DefaultSeleniumParser"

    def __init__(self, url):
        self.url = url
        self.browser = webdriver.Firefox()
        self.browser.get(self.url)
        html_source = self.browser.page_source
        self.browser.close()
        self.soup = BeautifulSoup(html_source)

class YahooParser(DefaultParser):
    def __str__(self):
        return "Yahoo Parser"

    def __init__(self, url):
        super().__init__(url)

    def get_title(self):
        header = self.soup.title
        if self.soup.title is not None:
            return sub("- Yahoo.+", "", header.string).strip()
        else:
            return None

    def get_article(self):
        article_body = self.soup.find("div", class_="body")
        if article_body is not None:
            subparagraphs_tags = article_body.find_all("p")
            if subparagraphs_tags:
                return "\n".join([paragraph_tag.getText().strip()
                                  for paragraph_tag in subparagraphs_tags])
            else:
                return None
        else:
            return None

    def get_related_articles(self):

        browser = webdriver.Firefox()
        browser.get(self.url)
        html_source = browser.page_source
        browser.close()

        related_article_soup = BeautifulSoup(html_source)
        section = related_article_soup.find("section", id="mediacontentrelatedstory")
        if section is not None:
            return [self.url.split('/')[2] + tag['href']
                    for tag in section.findAll('a', href=True) if "http" not in tag]
        else:
            return []


class ReutersParser(DefaultParser):

    def __str__(self):
        return "ReutersParser"

    def __init__(self, url):
        super().__init__(url)

    def get_title(self):
        header = self.soup.find("h1", class_="article-headline")
        if header is not None:
            return header.getText()
        else:
            return None

    def get_article(self):
        article_body = self.soup.find("span", id="articleText")
        if article_body is not None:
            subparagraphs_tags = article_body.find_all("p")
            if subparagraphs_tags:
                return "\n".join([paragraph_tag.getText().strip()
                                  for paragraph_tag in subparagraphs_tags])
            else:
                return None
        else:
            return None

class BBCParser(DefaultParser):

    def __str__(self):
        return "BBCParser"

    def __init__(self, url):
        super().__init__(url)

    def get_article(self):

        if "sport" in self.url:
            article_body = self.soup.find("div", class_="article")
        else:
            article_body = self.soup.find("div", class_="story-body")

        if article_body is not None:
            subparagraphs_tags = article_body.find_all("p")
            if subparagraphs_tags:
                return "\n".join([paragraph_tag.getText().strip()
                                  for paragraph_tag in subparagraphs_tags
                                  if not "Media playback is unsupported on your device"
                                  in paragraph_tag.getText()])
            else:
                return None
        else:
            return None


class DailyMailParser(DefaultParser):

    def __str__(self):
        return "DailyMailParser"

    def __init__(self, url):
        super().__init__(url)

    def get_article(self):

        article_body = self.soup.find("div", class_="article-text")

        if article_body is not None:
            subparagraphs_tags = article_body.find_all("p", class_="mol-para-with-font")
            if subparagraphs_tags:
                return "\n".join([paragraph_tag.getText().strip()
                                  for paragraph_tag in subparagraphs_tags])
            else:
                return None
        else:
            return None


class WebMedParser(DefaultSeleniumParser):

    def __str__(self):
        return "WebMedParser"

    def __init__(self, url):
        super().__init__(url)

    def get_article(self):
        article_body = self.soup.find("div", id="textArea")
        article_content = self.soup.find("div", class_="article-content")

        if article_body is not None:
            subparagraphs_tags = article_body.find_all("p", class_="node")
            if subparagraphs_tags:
                return "\n".join([paragraph_tag.getText().strip()
                                  for paragraph_tag in subparagraphs_tags])
            else:
                return None
        elif article_content is not None:
            subparagraphs_tags = article_content.find_all("p")
            if subparagraphs_tags:
                return "\n".join([paragraph_tag.getText().strip()
                                  for paragraph_tag in subparagraphs_tags])
            else:
                return None
        else:
            return None


class FoxNewsParser(DefaultSeleniumParser):

    def __str__(self):
        return "FoxNewsParser"

    def __init__(self, url):
        super().__init__(url)

    def get_article(self):
        article_body = self.soup.find("article")

        if article_body is not None:
            subparagraphs_tags = article_body.find_all("p")
            if subparagraphs_tags:
                return "\n".join([paragraph_tag.getText().strip()
                                  for paragraph_tag in subparagraphs_tags])
            else:
                return None
        else:
            return None

class TelegraphParser(DefaultParser):

    def __str__(self):
        return "TelegraphParser"

    def __init__(self, url):
        super().__init__(url)

    def get_article(self):
        article_body = self.soup.find("div", class_="story")

        if article_body is not None:
            subparagraphs_tags = article_body.find_all("p")
            if subparagraphs_tags:
                return "\n".join([paragraph_tag.getText().strip()
                                  for paragraph_tag in subparagraphs_tags
                                  if "embedPlayer" not in paragraph_tag.getText()])
            else:
                return None
        else:
            return None
