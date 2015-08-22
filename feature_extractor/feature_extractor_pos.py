__author__ = 'pchmiel'
from nltk import pos_tag
from nltk.corpus import stopwords


class FeatrueExtractorPos(object):

    def __init__(self, words, tagger):
        self.words = words
        self.bag_of_words = []
        self.tagger = tagger


    def pos_remove(self):
        self.bag_of_words = [word for word, tag in self.tagger.tag(self.words) if "NN" in tag or "VB" in tag or
                             "JJ" in tag or "RB" in tag]

    def extract_features(self):
         self.pos_remove()
         self.remove_stopwords(self.bag_of_words)
         self.remove_sign(self.bag_of_words)
         self.remove_duplicats(self.bag_of_words)
         return dict([(word, True) for word in self.bag_of_words])

    def remove_duplicats(self, words):
        self.bag_of_words = list(set([word.lower() for word in words if word.isalpha()]))

    def remove_stopwords(self, words):
        english_stopwords = set(stopwords.words('english'))
        self.bag_of_words = [word for word in words if word not in english_stopwords]

    def remove_sign(self, words):
        self.bag_of_words = [word for word in words if len(word) != 1]