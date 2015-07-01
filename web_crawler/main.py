__author__ = 'Piotr Chmiel'

from web_crawler.rss_provider import FeedProvider, get_source
from web_crawler.website_critera import CriteriaManager
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
        print(category)
        for rss_link in rss_link_by_category[category]:
            feed_provider = FeedProvider(rss_link)
            urls = feed_provider.get_article_urls()
            print (urls)
            for url in urls:
                if url != None:
                    parser = CriteriaManager.get_parser(url)
                    if parser != None:
                        article_title = parser.get_title()
                        article = parser.get_article()
                        print(article_title)
                        print (article)
                        break


if __name__ == '__main__':
    main()