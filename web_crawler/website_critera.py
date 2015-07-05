__author__ = 'Piotr Chmiel'

from web_crawler.website_parser import YahooParser, ReutersParser, BBCParser, \
                                       DailyMailParser, WebMedParser, FoxNewsParser, \
                                       TelegraphParser, DefaultParser
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
        return 'yahoo' in url

    def get_parser(self, url):
        return YahooParser(url)

    def format_url(self, url):
        if "sport" in url and "*" in url:
            return unquote(url.split('*')[1])
        else:
            return url

class ReutersCriteria(WebsiteCriteria):

    def meet_website(self, url):
        return 'feeds.reuters' in url

    def get_parser(self, url):
        return ReutersParser(url)

class BBCCriteria(WebsiteCriteria):

    def meet_website(self, url):
        return 'bbc' in url

    def get_parser(self, url):
        return BBCParser(url)

class DailyMail(WebsiteCriteria):
    def meet_website(self, url):
        return 'dailymail' in url

    def get_parser(self, url):
        return DailyMailParser(url)

class WebMed(WebsiteCriteria):
    def meet_website(self, url):
        return 'webmd' in url

    def get_parser(self, url):
        return WebMedParser(url)

class FoxNews(WebsiteCriteria):
    def meet_website(self, url):
        return 'fox' in url

    def get_parser(self, url):
        return FoxNewsParser(url)

class Telegraph(WebsiteCriteria):
    def meet_website(self, url):
        return 'telegraph' in url

    def get_parser(self, url):
        return TelegraphParser(url)

class CriteriaManager(object):

    criteria = [YahooCriteria(), ReutersCriteria(), BBCCriteria(), DailyMail(), WebMed(), FoxNews(), Telegraph()]

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

        return url
