__author__ = 'Piotr'
from nltk.corpus.reader import CategorizedPlaintextCorpusReader
from random import shuffle
import nltk

training = CategorizedPlaintextCorpusReader("Articles", r'.*\.txt',cat_pattern=r'(\w+)', encoding ="utf-8")

def print_corpus_info():
    print ("Training Corpus INFO")

    for category in training.categories():
        print("Number of documents in {0:8} category: {1}".format(category, len(training.fileids(category))))

    print("\n")

def get_training_documents(cut_off = 0.75):
    train_set = []
    test_set = []

    for category in training.categories():
        category_set = [(list(training.words(fileid)), category) for fileid in training.fileids(category)]
        shuffle(category_set)
        cut_set = int(len(category_set) * cut_off)
        train_set += category_set[:cut_set]
        test_set += category_set[cut_set:]

    return train_set, test_set

