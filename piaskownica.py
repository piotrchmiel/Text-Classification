__author__ = 'Piotr'
from corpus import training
import random
from nltk.classify import apply_features
import nltk

def bag_of_words(words):
    return dict([(word, True) for word in words])

def main():

    documents = [(list(training.words(fileid)), category)
                 for category in training.categories()
                 for fileid in training.fileids(category)]

    random.shuffle(documents)
    cut_off = int(len(documents) * 0.75)
    print (cut_off)
    train_set = apply_features(bag_of_words, documents[:cut_off])
    test_set = apply_features(bag_of_words, documents[cut_off:])

    classifier = nltk.NaiveBayesClassifier.train(train_set)
    classifier.show_most_informative_features()
    print(nltk.classify.accuracy(classifier,test_set))

    classifier = classifier.classify(bag_of_words(nltk.word_tokenize("Trump")))
    print (classifier)

if __name__ == '__main__':
    main()