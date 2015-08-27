__author__ = 'Piotr'

from text_processing.corpus import training
from nltk import word_tokenize
from nltk.collocations import BigramCollocationFinder, TrigramCollocationFinder
from nltk.metrics import BigramAssocMeasures, TrigramAssocMeasures
from nltk.corpus import stopwords
from nltk import bigrams, FreqDist, trigrams

def main():
    stopset = set(stopwords.words('english'))
    tv_set = ['fox', 'news', 'bbc', 'yahoo']
    filter_stops = lambda w: len(w) < 3 or w in stopset or w in tv_set
    for category in training.categories():
        for fileid in training.fileids(category):
            g = word_tokenize(training.open(fileid).read())
            g = [word.lower() for word in g if word.isalpha()]
            bcf = TrigramCollocationFinder.from_words(g)
            bcf.apply_word_filter(filter_stops)
            bcf.apply_freq_filter(2)
            kc = bcf.nbest(TrigramAssocMeasures.likelihood_ratio, 4)
            n = FreqDist(kc)

            print(n)

            break



if __name__ == '__main__':
    main()

