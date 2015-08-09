import os
from nltk import word_tokenize
import nltk
from corpus import training
for root, dirs, files in os.walk("Articles"):
    utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)
    print (training.fileids()[1])
    fh = training.open(r"HEALTH/17-stone mother drank NINE cups of green tea a day and drop eight dress sizes  Daily Mail Online.txt")
    g = fh.read()
    print(g, file=utf8stdout)
    tokens = word_tokenize(g)
    print (tokens, file=utf8stdout)
    text = nltk.Text(tokens)
    print(text)
    text.collocations( )
    fh.close()
    break