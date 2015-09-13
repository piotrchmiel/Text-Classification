__author__ = 'Piotr Chmiel'
from collections import defaultdict
from feedparser import parse

from web_crawler.website_critera import CriteriaManager


class FeedProvider(object):

    def __init__(self, url):
        self.feed = parse(url)

    def get_article_urls(self):
        return [CriteriaManager.format_url(entry.link) for entry in self.feed.entries]


def get_source(source_file_name):
    feed_by_category = defaultdict(list)

    with open(source_file_name) as source_handler:
        for line in source_handler:
            if not line.strip()[0] == '#':
                temp = line.strip().split(" ")
                feed_by_category[temp[0]].append(temp[1])

    return feed_by_category







