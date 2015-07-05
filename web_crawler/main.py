__author__ = 'Piotr Chmiel'

from web_crawler.rss_provider import FeedProvider, get_source
from web_crawler.website_critera import CriteriaManager
from multiprocessing import Process

import os

def valid_filename(filename):
    valid_chars = '-_.() abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(c for c in filename if c in valid_chars)

def create_file(path, url, article_title, article):
    with open(path, "w", encoding='utf-8') as fh:
                                    fh.write(url + "\n")
                                    fh.write(article_title + "\n\n")
                                    fh.write(article.decode(encoding='UTF-8', errors="replace"))
def get_articles(rss_link, category):
    feed_provider = FeedProvider(rss_link)
    urls = feed_provider.get_article_urls()
    print(urls)
    for url in urls:
        if url is not None:
            try:
                parser = CriteriaManager.get_parser(url)
            except:
                "Parser error"
            else:
                if parser is not None:
                    print(url)
                    article_title = parser.get_title()
                    if article_title is not None:
                        path = os.getcwd() + "/Articles/" + category + "/" + valid_filename(article_title) + ".txt"
                        if not os.path.exists(path):
                            article = parser.get_article()
                            if article is not None:
                                article = article.encode("utf-8")
                                print(article_title.encode("utf-8"))
                                print(article)
                                create_file(path, url, article_title, article)
                            else:
                                print("Article is None")
                        else:
                            print("Path exists")
                    else:
                        print("Title is none")

def main():
    processes = []

    print("Start Web Crawler")
    rss_link_by_category = get_source("rss_source.txt")
    print(rss_link_by_category)

    if not os.path.isdir(os.getcwd() + "/Articles"):
        os.mkdir("Articles")

    for category in rss_link_by_category.keys():
        if not os.path.isdir(os.getcwd() + "/Articles/" + category):
            os.mkdir("Articles/" + category)
        for rss_link in rss_link_by_category[category]:
            processes.append(Process(target=get_articles, args=(rss_link, category,)))

    for process in processes:
        process.start()

    for process in processes:
        process.join()

if __name__ == '__main__':
    main()