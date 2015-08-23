__author__ = 'Piotr'

from nltk.stem import PorterStemmer, LancasterStemmer, WordNetLemmatizer
from nltk.corpus import words, wordnet

def main():
    stemmer = LancasterStemmer()
    lemmatizer = WordNetLemmatizer()
    kupa = lemmatizer.lemmatize(stemmer.stem("obama"), wordnet.ADJ)
    print(kupa)
    print(stemmer.stem("abandoning"))
    print(stemmer.stem("abandons"))
    print(stemmer.stem("abandoned"))

if __name__ == '__main__':
    main()