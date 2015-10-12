from pickle import dump
from copy import deepcopy
import os

from nltk.classify import apply_features, accuracy
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from statistics import load_pickle
from text_processing.corpus import print_corpus_info, get_training_documents
from feature_extractor.bag_of_words import binary_bag_of_words, counted_bag_of_words


def trainer(train_documents, test_documents, bag_of_words, classifier_object, type, name):
    print("Training {0} ...".format(name))
    train_set = apply_features(bag_of_words, train_documents)
    test_set = apply_features(bag_of_words, test_documents)

    classifier = SklearnClassifier(classifier_object, type)
    classifier.train(train_set)

    with open("Classifiers/" + name + ".pickle", 'wb') as file_handler:
        dump(classifier, file_handler)
    print("Done")
    print("Accurancy {0}".format(accuracy(classifier, test_set)))
    print("Done")


def main():
    print ("Welcome to trainer ! \n")
    print_corpus_info()
    if not os.path.isdir(os.getcwd() + "/Classifiers"):
        os.mkdir("Classifiers")

    #train_documents, test_documents = get_training_documents(cut_off=0.75, save=True)

    train_documents = load_pickle("Classifiers/train_feature_set.pickle")
    test_documents = load_pickle("Classifiers/test_feature_set.pickle")

    algorithms = [LinearSVC(), LogisticRegression(), BernoulliNB()]

    for algorithm in algorithms:
        class_name = algorithm.__class__.__name__
        trainer(train_documents, test_documents, binary_bag_of_words, deepcopy(algorithm), bool, class_name + "_bool")
        trainer(train_documents, test_documents, counted_bag_of_words, deepcopy(algorithm), int, class_name + "_int")
        trainer(train_documents, test_documents, counted_bag_of_words, Pipeline([('tfidf', TfidfTransformer()),
                ('nb', deepcopy(algorithm))]), float, class_name + "_tfidf")

if __name__ == '__main__':
    main()