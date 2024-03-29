__author__ = 'Piotr'
from random import shuffle
from pickle import dump
import os

from nltk import word_tokenize
from nltk.corpus.reader import CategorizedPlaintextCorpusReader

from text_processing.replacers import RegexpReplacer

training = CategorizedPlaintextCorpusReader("Articles", r'.*\.txt', cat_pattern=r'(\w+)', encoding="utf-8")


def print_corpus_info():
    print("Training Corpus INFO")

    for category in training.categories():
        print("Number of documents in {0:8} category: {1}".format(category, len(training.fileids(category))))

    print("\n")


def save_documents(documents, name):
     with open(os.path.join("Classifiers", name + ".pickle"), 'wb') as file_handler:
        dump(documents, file_handler)


def get_training_documents(cut_off=0.75, save=False):
    train_set = []
    test_set = []

    for category in training.categories():
        category_set = [(fileid, category) for fileid in training.fileids(category)]
        shuffle(category_set)
        cut_set = int(len(category_set) * cut_off)
        train_set.extend(category_set[:cut_set])
        test_set.extend(category_set[cut_set:])

    if save:
        save_documents(train_set, "train_documents")
        save_documents(test_set, "test_documents")

    train_set = [(get_words_and_replace(fileid), category) for fileid, category in train_set]
    test_set = [(get_words_and_replace(fileid), category) for fileid, category in test_set]

    if save:
        save_documents(train_set, "train_feature_set")
        save_documents(test_set, "test_feature_set")

    return train_set, test_set


def get_words_and_replace(fileid):

    content = training.open(fileid).read()
    replacer = RegexpReplacer()

    return list(word_tokenize(replacer.replace(content)))
