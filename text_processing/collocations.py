__author__ = 'pchmiel'

from nltk.collocations import BigramCollocationFinder, TrigramCollocationFinder
from nltk.corpus import stopwords
from nltk.metrics import BigramAssocMeasures, TrigramAssocMeasures


class CollocationsFinder(object):

    def __init__(self):
        self.stopset = set(stopwords.words('english'))
        self.tv_set = ('fox', 'news', 'bbc', 'yahoo', 'telegraph', 'reuters')
        self.filter_stops = lambda w: len(w) < 3 or w in self.stopset or w in self.tv_set

    def filter_numbers(self, words):
        return [word.lower() for word in words if word.isalpha()]

    def bigram_finder(self, words):
        tcf = BigramCollocationFinder.from_words(self.filter_numbers(words))
        tcf.apply_word_filter(self.filter_stops)
        tcf.apply_freq_filter(2)
        return tcf.nbest(BigramAssocMeasures.likelihood_ratio, 4)

    def trigram_finder(self, words):
        tcf = TrigramCollocationFinder.from_words(self.filter_numbers(words))
        tcf.apply_word_filter(self.filter_stops)
        tcf.apply_freq_filter(2)
        return tcf.nbest(TrigramAssocMeasures.likelihood_ratio, 4)

class SklearnClassifier(ClassifierI):

    def __init__(self, estimator, dtype=float, sparse=True):

        self._clf = estimator
        self._encoder = LabelEncoder()
        self._vectorizer = DictVectorizer(dtype=dtype, sparse=sparse)

    def train(self, labeled_featuresets):

        X, y = list(compat.izip(*labeled_featuresets))
        X = self._vectorizer.fit_transform(X)
        y = self._encoder.fit_transform(y)
        self._clf.fit(X, y)

        return self