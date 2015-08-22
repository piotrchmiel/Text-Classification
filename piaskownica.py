__author__ = 'Piotr'

from nltk.stem import PorterStemmer, LancasterStemmer, WordNetLemmatizer

def main():
    stemmer = LancasterStemmer()
    lemmatizer = WordNetLemmatizer()
    print(lemmatizer.lemmatize(stemmer.stem("abandon")))
    print(stemmer.stem("abandoning"))
    print(stemmer.stem("abandons"))
    print(stemmer.stem("abandoned"))

if __name__ == '__main__':
    main()