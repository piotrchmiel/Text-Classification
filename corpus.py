__author__ = 'Piotr'
from nltk.corpus.reader import CategorizedPlaintextCorpusReader

training = CategorizedPlaintextCorpusReader("Articles", r'.*\.txt',cat_pattern=r'(\w+)', encoding ="utf-8")