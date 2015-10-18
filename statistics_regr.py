from feature_extractor.bag_of_words import *
from statistics import statistics, load_pickle
from sklearn.naive_bayes import BernoulliNB
from classification_main import load_classifier
from trainer import trainer

def main():
    train_feature_set = load_pickle("Classifiers/train_feature_set.pickle")
    test_feature_set = load_pickle("Classifiers/test_feature_set.pickle")
    test_documents = load_pickle("Classifiers/test_documents.pickle")

    test_feature_extractors = [ test_all_words, test_one_sign, test_lower, test_alpha, test_stopwords,
                                test_tv_set, test_pos, test_stem, binary_bag_of_words ]

    for extractor in test_feature_extractors:
        trainer(train_feature_set, test_feature_set, extractor, BernoulliNB(), bool, "test_bool")
        classifier = load_classifier("Classifiers/test_bool.pickle")

        print("\n-----------------BernoulliNB " + extractor.__name__ + "-----------------\n")

        statistics(classifier, extractor, test_feature_set, test_documents)

if __name__ == '__main__':
    main()
