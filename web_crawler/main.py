__author__ = 'Piotr Chmiel'

from web_crawler.rss_provider import FeedProvider, get_source
def main():
    print("Start Web Crawler")
    rss_link_by_category = get_source("rss_source.txt")
    print(rss_link_by_category)

    for category in rss_link_by_category.keys():
        for rss_link_by_category in rss_link_by_category[category]:
            feed_provider = FeedProvider(rss_link_by_category)
            print (feed_provider.get_article_urls())

if __name__ == '__main__':
    main()