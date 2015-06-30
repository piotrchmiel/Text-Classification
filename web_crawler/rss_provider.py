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
    source_handler = open(source_file_name)
    feed_by_category = defaultdict(list)

    for line in source_handler:
        if line.strip()[0] == '#':
            continue
        else:
            temp = line.strip().split(" ")
            feed_by_category[temp[0]].append(temp[1])

    source_handler.close()

    return feed_by_category







