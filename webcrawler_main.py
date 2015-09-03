__author__ = 'Piotr Chmiel'

from web_crawler.rss_provider import FeedProvider, get_source
from web_crawler.website_critera import CriteriaManager
from multiprocessing import Process, Lock
from json import load, dump
import os

def valid_filename(filename):
    valid_chars = '-_.() abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(c for c in filename if c in valid_chars)

def create_file(path, article):
    with open(path, "w", encoding='utf-8') as file_handler:
        file_handler.write(article.decode(encoding='UTF-8', errors="replace"))

def write_index(url, filename):
    with open("index.txt", encoding="utf-8") as index_fh:
        data = load(index_fh)
        if filename not in data:
            data[filename] = url

    with open("index.txt", "w", encoding="utf-8") as index_fh:
        dump(data, index_fh)

def get_articles(rss_link, category, lock):
    feed_provider = FeedProvider(rss_link)
    urls = feed_provider.get_article_urls()
    print(urls)
    for url in urls:
        if url is not None:
            try:
                parser = CriteriaManager.get_parser(url)
            except Exception as err:
                print("Parser error\n" + str(err))
            else:
                if parser is not None:
                    print(url)
                    article_title = parser.get_title()
                    if article_title is not None:
                        path = os.getcwd() + "/Articles/" + category + \
                               "/" + valid_filename(article_title) + ".txt"
                        if not os.path.exists(path):
                            article = parser.get_article()
                            if article is not None:
                                article = article.encode("utf-8")
                                print(article_title.encode("utf-8"))
                                print(article)
                                create_file(path, article)
                                lock.acquire()
                                write_index(url, valid_filename(article_title) + ".txt")
                                lock.release()
                            else:
                                print("Article is None")
                        else:
                            print("Path exists")
                    else:
                        print("Title is none")
                else:
                    print("Parser is none")

def main():
    processes = []
    lock = Lock()
    print("Start Web Crawler")
    rss_link_by_category = get_source("rss_source.txt")
    print(rss_link_by_category)

    if not os.path.isdir(os.getcwd() + "/Articles"):
        os.mkdir("Articles")

    if not os.path.isfile(os.getcwd() + "/index.txt"):
        with open(os.getcwd() + "/index.txt", 'w') as fh:
            fh.write("{}")

    for category in rss_link_by_category.keys():
        if not os.path.isdir(os.getcwd() + "/Articles/" + category):
            os.mkdir("Articles/" + category)
        for rss_link in rss_link_by_category[category]:
            #processes.append(Process(target=get_articles, args=(rss_link, category, lock)))
            get_articles(rss_link,category,lock)
    """
    for process in processes:
        process.start()

    for process in processes:
        process.join()
    """

if __name__ == '__main__':
    main()
