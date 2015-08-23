__author__ = 'pchmiel'
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

class FeatrueExtractorPos(object):

    def __init__(self, words, tagger):
        self.words = words
        self.bag_of_words = []
        self.tagger = tagger
        self.stemmer = PorterStemmer()
        self.lemmatizer = WordNetLemmatizer()


    def pos_remove(self):
        self.bag_of_words = [word for word, tag in self.tagger.tag(self.words) if "NN" in tag or "VB" in tag or
                             "JJ" in tag or "RB" in tag]

    def extract_features(self):
         self.pos_remove()
         self.remove_stopwords()
         self.remove_sign()
         self.stem_and_lemmatize()
         self.remove_duplicats()
         return dict([(word, True) for word in self.bag_of_words])

    def remove_duplicats(self):
        self.bag_of_words = list(set([word.lower() for word in self.bag_of_words if word.isalpha()]))

    def remove_stopwords(self):
        english_stopwords = set(stopwords.words('english'))
        self.bag_of_words = [word for word in self.bag_of_words if word not in english_stopwords]

    def remove_sign(self):
        self.bag_of_words = [word for word in self.bag_of_words if len(word) != 1]

    def stem_and_lemmatize(self):
        self.bag_of_words = [self.lemmatizer.lemmatize(self.stemmer.stem(word)) for word in self.bag_of_words]