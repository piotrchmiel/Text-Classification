__author__ = 'Piotr'
from random import shuffle

from nltk import word_tokenize
from nltk.corpus.reader import CategorizedPlaintextCorpusReader

from text_processing.replacers import RegexpReplacer

training = CategorizedPlaintextCorpusReader("Articles", r'.*\.txt',cat_pattern=r'(\w+)', encoding ="utf-8")


def print_corpus_info():
    print ("Training Corpus INFO")

    for category in training.categories():
        print("Number of documents in {0:8} category: {1}".format(category, len(training.fileids(category))))

    print("\n")


def get_training_documents(cut_off = 0.75):
    train_set = []
    test_set = []
    replacer = RegexpReplacer()

    for category in training.categories():
        category_set = [(get_words(fileid, replacer), category) for fileid in training.fileids(category)]
        shuffle(category_set)
        cut_set = int(len(category_set) * cut_off)
        train_set.extend(category_set[:cut_set])
        test_set.extend(category_set[cut_set:])

    return train_set, test_set


def get_words(fileid, replacer):

    content =  training.open(fileid).read()

    return list(word_tokenize(replacer.replace(content)))
