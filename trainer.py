from pickle import dump
import os

from nltk.classify import apply_features, accuracy
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline

from text_processing.corpus import print_corpus_info, get_training_documents
from feature_extractor.bag_of_words import binary_bag_of_words, counted_bag_of_words


def trainer(train_documents, test_documents, bag_of_words, classifier_object, type, name):
    print("Training {0} ...".format(name))
    train_set = apply_features(bag_of_words, train_documents)
    test_set = apply_features(bag_of_words, test_documents)

    classifier = SklearnClassifier(classifier_object, type)
    classifier.train(train_set)

    with open("Classificators/" + name + ".pickle", 'wb') as file_handler:
        dump(classifier, file_handler)
    print("Done")
    print("Accurancy {0}".format(accuracy(classifier, test_set)))
    print("Done")


def main():
    print ("Welcome to trainer ! \n")
    print_corpus_info()
    if not os.path.isdir(os.getcwd() + "/Classificators"):
        os.mkdir("Classificators")

    train_documents, test_documents = get_training_documents(cut_off=0.75)

    trainer(train_documents, test_documents, binary_bag_of_words, LinearSVC(), bool, "LinearSVC_bool")
    trainer(train_documents, test_documents, counted_bag_of_words, LinearSVC(), int, "LinearSVC_int")
    trainer(train_documents, test_documents, counted_bag_of_words, Pipeline([('tfidf', TfidfTransformer()),
            ('lsc', LinearSVC())]), float, "LinearSVC_tfidf")
    trainer(train_documents, test_documents, binary_bag_of_words, BernoulliNB(), bool, "BernoulliNB_bool")
    trainer(train_documents, test_documents, counted_bag_of_words, BernoulliNB(), int, "BernoulliNB_int")
    trainer(train_documents, test_documents, counted_bag_of_words, Pipeline([('tfidf', TfidfTransformer()),
            ('nb', BernoulliNB())]), float, "BernoulliNB_tfidf")

if __name__ == '__main__':
    main()