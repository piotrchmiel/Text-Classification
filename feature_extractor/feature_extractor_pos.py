__author__ = 'pchmiel'
from nltk.corpus import stopwords, wordnet
from nltk.stem import PorterStemmer, WordNetLemmatizer
from text_processing.collocations import CollocationsFinder


class FeatrueExtractorPos(object):

    def __init__(self, words, tagger, binary=True):
        self.words = words
        self.bag_of_words = []
        self.tagger = tagger
        self.stemmer = PorterStemmer()
        self.lemmatizer = WordNetLemmatizer()
        self.binary = binary
        self.english_stopwords = set(stopwords.words('english'))
        self.collocations_finder = CollocationsFinder()
        self.tv_set = ('fox', 'news', 'bbc', 'yahoo', 'telegraph', 'reuters')

    def extract_features(self):
        if self.binary:
            self.remove_duplicats()
            return self.binary_feature_set()
        else:
            return self.count_feature_set()

    def binary_feature_set(self):
        feature_set = dict([(word, True) for word in self.bag_of_words])

        for bigram in self.collocations_finder.bigram_finder(self.words):
            feature_set[' '.join(bigram)] = True
        for trigram in self.collocations_finder.trigram_finder(self.words):
            feature_set[' '.join(trigram)] = True

        return feature_set

    def count_feature_set(self):

        feature_set = {}
        for word in self.pos_generator():
            if word in feature_set:
                feature_set[word] += 1
            else:
                feature_set[word] = 1
        for bigram in self.collocations_finder.bigram_finder(self.words):
            feature_set[' '.join(bigram)] = 2
        for trigram in self.collocations_finder.trigram_finder(self.words):
            feature_set[' '.join(trigram)] = 2

        return feature_set

    def remove_duplicats(self):
        self.bag_of_words = list(set(self.pos_generator()))

    def is_in_stopwords(self, word):
        if word in self.english_stopwords:
            return True
        else:
            return False

    def is_one_sign(self, word):
        if len(word) == 1:
            return True
        else:
            return False

    def get_wordnet_pos(self, tag):

        if tag.startswith('J'):
            return wordnet.ADJ
        elif tag.startswith('V'):
            return wordnet.VERB
        elif tag.startswith('N'):
            return wordnet.NOUN
        elif tag.startswith('R'):
            return wordnet.ADV
        else:
            return ''

    def stem_and_lemmatize(self, word, tag):
        return self.lemmatizer.lemmatize(self.stemmer.stem(word), pos=self.get_wordnet_pos(tag))

    def pos_generator(self):
        tagged_words = self.tagger.tag(self.words)

        for (word, tag) in tagged_words:
            if any(tag.startswith(prefix) for prefix in ["NN", "VB", "JJ", "RB"]) and not self.is_one_sign(word) and \
               not self.is_in_stopwords(word) and word.isalpha() and word not in self.tv_set:
                processed_word = self.stem_and_lemmatize(word, tag)
                yield processed_word.lower()
