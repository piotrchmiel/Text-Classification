__author__ = 'Piotr Chmiel'

from web_crawler.website_parser import YahooParser
from urllib.parse import unquote
class IWebsiteCriteria(object):

    def meet_website(self, url):
        pass

    def get_parser(self, url):
        pass

class YahooCriteria(IWebsiteCriteria):

    def meet_website(self, url):
        if 'yahoo' in url:
            return True
        else:
            return False

    def get_parser(self, url):
        return YahooParser(url)

    def format_url(self, url):
        return unquote(url.split('*')[1])

class CriteriaManager(object):

    criteria = [YahooCriteria()]

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