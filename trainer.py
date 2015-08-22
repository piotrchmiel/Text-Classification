from corpus import print_corpus_info, get_training_documents
from feature_extractor.bag_of_words import bag_of_words
from nltk.classify import apply_features, accuracy
from nltk import NaiveBayesClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import LabelEncoder
from nltk import compat
from progress.bar import Bar
import pickle

def main():

    print_corpus_info()
    print ("Extracting features: ")
    train_documents, test_documents = get_training_documents(cut_off=0.75)

    train_set = apply_features(bag_of_words, train_documents)
    test_set = apply_features(bag_of_words, test_documents)
    """
    _encoder = LabelEncoder()
    _vectorizer = DictVectorizer(dtype=float, sparse=True)
    X, y = list(compat.izip(*train_set))

    X = _vectorizer.fit_transform(X)
    y = _encoder.fit_transform(y)

    print (_vectorizer.get_feature_names()[:100])
    print (len(X.toarray()))
    print (list(_encoder.classes_))
    """
    classifier = NaiveBayesClassifier.train(train_set)
    with open('naive_bayes_classifier.pickle', 'wb') as file_handler:
        pickle.dump(classifier, file_handler)

    classifier.show_most_informative_features(10)
    print(accuracy(classifier,test_set))


if __name__ == '__main__':
    main()