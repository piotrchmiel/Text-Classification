__author__ = 'pchmiel'
import nltk
from feature_extractor.feature_extractor_pos import FeatrueExtractorPos
tagger = nltk.data.load(nltk.tag._POS_TAGGER)
i = 0

def bag_of_words(words, extractor=FeatrueExtractorPos, tagger=tagger):
    global i
    extractor = extractor(words, tagger)
    i = i + 1
    print(i, end='\r')


    return extractor.extract_features()
