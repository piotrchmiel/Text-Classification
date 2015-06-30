__author__ = 'Piotr Chmiel'

from web_crawler.rss_provider import FeedProvider, get_source
import os
def main():
    print("Start Web Crawler")
    rss_link_by_category = get_source("rss_source.txt")
    print(rss_link_by_category)

    if not os.path.isdir(os.getcwd() + "/Articles"):
        os.mkdir("Articles")

    for category in rss_link_by_category.keys():
        if not os.path.isdir(os.getcwd() + "/Articles/" + category):
            os.mkdir("Articles/" + category)

        for rss_link_by_category in rss_link_by_category[category]:
            feed_provider = FeedProvider(rss_link_by_category)
            print (feed_provider.get_article_urls())

if __name__ == '__main__':
    main()