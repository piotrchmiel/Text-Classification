__author__ = 'pchmiel'
import os
from pickle import load

from nltk.classify import apply_features
from nltk.metrics.confusionmatrix import ConfusionMatrix

from classification_main import load_classificator
from text_processing.corpus import print_corpus_info
from feature_extractor.bag_of_words import binary_bag_of_words, counted_bag_of_words


def accurancy(test_feature_set, results):
    correct = [label == result_label for ((_, label), result_label) in zip(test_feature_set, results)]
    if correct:
        return float(sum(correct))/len(correct)
    else:
        return 0


def incompability(labeled_documents, results):
    for ((document, label), result_label) in zip(labeled_documents, results):
        if label != result_label:
            print("Document {0}: Label: {1} => Result{2}".format(document, label, result_label))


def statistics(classificator, bag_of_word, test_feature_set, test_documents):
    test_set = apply_features(bag_of_word, test_feature_set)
    reference = [label for (_, label) in test_set]

    classify_results = classificator.classify_many([feature_set for (feature_set, _) in test_set])

    print(ConfusionMatrix(reference, classify_results))
    print("\nAccurancy: ", accurancy(test_set, classify_results))

    incompability(test_documents, classify_results)


def load_pickle(name_pickle_file):
    with open(name_pickle_file, "rb") as file_handler:
        pickle_object = load(file_handler)

    return pickle_object


def main():

    print_corpus_info()

    classificators = (("LinearSVC_bool", binary_bag_of_words), ("LinearSVC_int", counted_bag_of_words),
                      ("LinearSVC_tfidf", counted_bag_of_words), ("BernoulliNB_bool", binary_bag_of_words),
                      ("BernoulliNB_int", counted_bag_of_words), ("BernoulliNB_tfidf", counted_bag_of_words))

    test_feature_set = load_pickle("Classificators/test_feature_set.pickle")
    test_documents = load_pickle("Classificators/test_documents.pickle")

    for name, bag_of_words in classificators:
        print("-----------------", name, "-----------------")

        classificator=load_classificator(os.path.join("Classificators", name + ".pickle"))

        statistics(classificator, bag_of_words, test_feature_set, test_documents)


if __name__ == '__main__':
    main()