__author__ = 'pchmiel'
from feature_extractor.feature_extractor_pos import FeatrueExtractorPos


class TestExtractorAll(FeatrueExtractorPos):

    def __init__(self, words, tagger, binary=True):
        super().__init__(words,tagger,binary)

    def filter_words_and_remove_duplicats(self):
        self.bag_of_words = list(set(self.words))


class TestExtractorOneSign(FeatrueExtractorPos):

    def __init__(self, words, tagger, binary=True):
        super().__init__(words,tagger,binary)

    def pos_generator(self):
        for word in self.words:
            if not self.is_one_sign(word):
                yield word


class TestExtractorLower(FeatrueExtractorPos):

    def __init__(self, words, tagger, binary=True):
        super().__init__(words,tagger,binary)

    def pos_generator(self):
        for word in self.words:
            if not self.is_one_sign(word):
                yield word.lower()


class TestExtractorAlpha(FeatrueExtractorPos):

    def __init__(self, words, tagger, binary=True):
        super().__init__(words,tagger,binary)

    def pos_generator(self):
        for word in self.words:
            if not self.is_one_sign(word) and word.isalpha():
                yield word.lower()


class TestExtractorStopwords(FeatrueExtractorPos):

    def __init__(self, words, tagger, binary=True):
        super().__init__(words,tagger,binary)

    def pos_generator(self):
        for word in self.words:
            if not self.is_one_sign(word) and word.isalpha() and not self.is_in_stopwords(word):
                yield word.lower()


class TestExtractorTVSet(FeatrueExtractorPos):

    def __init__(self, words, tagger, binary=True):
        super().__init__(words,tagger,binary)

    def pos_generator(self):
        for word in self.words:
            if not self.is_one_sign(word) and word.isalpha() and not self.is_in_stopwords(word) and \
               not self.is_in_tv_set(word):
                yield word.lower()


class TestExtractorPos(FeatrueExtractorPos):

    def __init__(self, words, tagger, binary=True):
        super().__init__(words,tagger,binary)

    def pos_generator(self):
        tagged_words = self.tagger.tag(self.words)

        for (word, tag) in tagged_words:
            if any(tag.startswith(prefix) for prefix in ["NN", "VB", "JJ", "RB"]) and not self.is_one_sign(word) and \
               not self.is_in_stopwords(word) and word.isalpha() and not self.is_in_tv_set(word):
                yield word.lower()


class TestExtractorStem(FeatrueExtractorPos):

    def __init__(self, words, tagger, binary=True):
        super().__init__(words,tagger,binary)

    def stem_and_lemmatize(self, word, tag):
        return self.stemmer.stem(word)

    def pos_generator(self):
        tagged_words = self.tagger.tag(self.words)

        for (word, tag) in tagged_words:
            if any(tag.startswith(prefix) for prefix in ["NN", "VB", "JJ", "RB"]) and not self.is_one_sign(word) and \
               not self.is_in_stopwords(word) and word.isalpha() and not self.is_in_tv_set(word):
                processed_word = self.stem_and_lemmatize(word, tag)
                yield processed_word.lower()
