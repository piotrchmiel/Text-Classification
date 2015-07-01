__author__ = 'Piotr Chmiel'

from web_crawler.website_parser import *
from urllib.parse import unquote

class WebsiteCriteria(object):

    def meet_website(self, url):
        return False

    def get_parser(self, url):
        return DefaultParser(url)

    def format_url(self, url):
        return url

class YahooCriteria(WebsiteCriteria):

    def meet_website(self, url):
        if 'yahoo' in url:
            return True
        else:
            return False

    def get_parser(self, url):
        return YahooParser(url)

    def format_url(self, url):
        if "sport" in url:
            return unquote(url.split('*')[1])
        else:
            return url

class ReutersCriteria(WebsiteCriteria):

    def meet_website(self, url):
        if 'feeds.reuters' in url:
            return True
        else:
            return False

    def get_parser(self, url):
        return ReutersParser(url)

class CriteriaManager(object):

    criteria = [YahooCriteria(), ReutersCriteria()]

    @staticmethod
    def get_parser(url):
        for criterium in CriteriaManager.criteria:
            if criterium.meet_website(url):
                return criterium.get_parser(url)

        return None

    @staticmethod
    def format_url(url):
        for criterium in CriteriaManager.criteria:
            if criterium.meet_website(url):
                return criterium.format_url(url)

        return None
