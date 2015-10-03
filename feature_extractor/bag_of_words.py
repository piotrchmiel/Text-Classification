__author__ = 'pchmiel'
import nltk
from feature_extractor.feature_extractor_pos import FeatrueExtractorPos
from feature_extractor.test_extractor import *

tagger = nltk.data.load(nltk.tag._POS_TAGGER)


def binary_bag_of_words(words, extractor=FeatrueExtractorPos, tagger=tagger):
    extractor = extractor(words, tagger, binary=True)
    return extractor.extract_features()


def counted_bag_of_words(words, extractor=FeatrueExtractorPos, tagger=tagger):
    extractor = extractor(words, tagger, binary=False)
    return extractor.extract_features()


def test_all_words(words):
    return binary_bag_of_words(words, extractor=TestExtractorAll, tagger=tagger)


def test_one_sign(words):
    return binary_bag_of_words(words, extractor=TestExtractorOneSign, tagger=tagger)


def test_lower(words):
    return binary_bag_of_words(words, extractor=TestExtractorLower, tagger=tagger)


def test_alpha(words):
    return binary_bag_of_words(words, extractor=TestExtractorAlpha, tagger=tagger)


def test_stopwords(words):
    return binary_bag_of_words(words, extractor=TestExtractorStopwords, tagger=tagger)


def test_tv_set(words):
    return binary_bag_of_words(words, extractor=TestExtractorTVSet, tagger=tagger)


def test_pos(words):
    return binary_bag_of_words(words, extractor=TestExtractorPos, tagger=tagger)


def test_stem(words):
    return binary_bag_of_words(words, extractor=TestExtractorStem, tagger=tagger)