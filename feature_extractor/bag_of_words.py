__author__ = 'pchmiel'
import nltk

from feature_extractor.feature_extractor_pos import FeatrueExtractorPos
tagger = nltk.data.load(nltk.tag._POS_TAGGER)

def binary_bag_of_words(words, extractor=FeatrueExtractorPos, tagger=tagger):
    extractor = extractor(words, tagger, binary=True)
    return extractor.extract_features()

def counted_bag_of_words(words, extractor=FeatrueExtractorPos, tagger=tagger):
    extractor = extractor(words, tagger, binary=False)
    return extractor.extract_features()



