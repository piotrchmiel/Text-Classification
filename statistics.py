__author__ = 'pchmiel'
import os
from pickle import load
from collections import defaultdict
from pprint import pprint

from nltk import compat
from nltk.classify import apply_features
from nltk.metrics.confusionmatrix import ConfusionMatrix
from nltk.metrics import precision, recall, f_measure

from classification_main import load_classifier
from text_processing.corpus import print_corpus_info
from feature_extractor.bag_of_words import *

try:
    from sklearn.feature_extraction import DictVectorizer
except ImportError:
    pass

def matrix_dimension(feature_set):
    vectorizer = DictVectorizer(dtype=float, sparse=True)
    X, _ = list(compat.izip(*feature_set))
    X = vectorizer.fit_transform(X)

    return X.toarray().shape


def vector_size():
    train_feature_set = load_pickle("Classifiers/train_feature_set.pickle")
    print("Train set: " + str(len(train_feature_set)))

    print("All words " + str(matrix_dimension(apply_features(test_all_words, train_feature_set))))
    print("One sign " + str(matrix_dimension(apply_features(test_one_sign, train_feature_set))))
    print("Lower " + str(matrix_dimension(apply_features(test_lower, train_feature_set))))
    print("Alpha " + str(matrix_dimension(apply_features(test_alpha, train_feature_set))))
    print("Stopwords " + str(matrix_dimension(apply_features(test_stopwords, train_feature_set))))
    print("TV Set " + str(matrix_dimension(apply_features(test_tv_set, train_feature_set))))
    print("POS " + str(matrix_dimension(apply_features(test_pos, train_feature_set))))
    print("STEM" + str(matrix_dimension(apply_features(test_stem, train_feature_set))))
    print(matrix_dimension(apply_features(binary_bag_of_words, train_feature_set)))


def accurancy(test_feature_set, results):
    correct = [label == result_label for ((_, label), result_label) in zip(test_feature_set, results)]
    if correct:
        return float(sum(correct))/len(correct)
    else:
        return 0


def incompability(labeled_documents, results):
    for ((document, label), result_label) in zip(labeled_documents, results):
        if label != result_label:
            print("Document {0}: Label: {1} => Result: {2}".format(document, label, result_label))


def precision_recall_f_measure(classifier, test_feats):
    refsets = defaultdict(set)
    testsets = defaultdict(set)

    for i, (feats, label) in enumerate(test_feats):
        refsets[label].add(i)
        observed = classifier.classify(feats)
        testsets[observed].add(i)

    precisions = {}
    recalls = {}
    f_measures = {}

    for label in classifier.labels():
        precisions[label] = precision(refsets[label], testsets[label])
        recalls[label] = recall(refsets[label], testsets[label])
        f_measures[label] = f_measure(refsets[label], testsets[label])

    print("\nPrecision:")
    pprint(precisions, width=1)
    print("\nRecall")
    pprint(recalls, width=1)
    print("\nF Measure")
    pprint(f_measures, width=1)


def statistics(classifier, bag_of_word, test_feature_set, test_documents):

    test_set = apply_features(bag_of_word, test_feature_set)
    reference = [label for (_, label) in test_set]

    classify_results = classifier.classify_many([feature_set for (feature_set, _) in test_set])

    print(ConfusionMatrix(reference, classify_results))
    print("\nAccurancy: ", accurancy(test_set, classify_results))

    incompability(test_documents, classify_results)
    precision_recall_f_measure(classifier, test_set)


def load_pickle(name_pickle_file):
    with open(name_pickle_file, "rb") as file_handler:
        pickle_object = load(file_handler)

    return pickle_object


def main():
    print_corpus_info()
    vector_size()

    test_feature_set = load_pickle("Classifiers/test_feature_set.pickle")
    test_documents = load_pickle("Classifiers/test_documents.pickle")

    for content in os.listdir("Classifiers"):
        path = os.path.abspath(os.path.join('Classifiers', content))
        if os.path.isfile(path) and any(suffix in content for suffix in ['_bool', '_int', '_tfidf']) and \
           content[content.rfind('.'):] == ".pickle":
            print("\n-----------------", content[:content.rfind('.')], "-----------------\n")

            classifier=load_classifier(path)
            if "_bool" in content:
                bag_of_words = binary_bag_of_words
            else:
                bag_of_words = counted_bag_of_words

            statistics(classifier, bag_of_words, test_feature_set, test_documents)


if __name__ == '__main__':
    main()
