import os

from nltk import word_tokenize
import nltk
for root, dirs, files in os.walk("Articles"):
    utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

    with open(r"Articles\HEALTH\32st teenager Bethany Churcher has gastric band surgery to become a model  Daily Mail Online.txt", encoding="utf8") as fh:
        g = fh.read()
        print(g, file=utf8stdout)
        tokens = word_tokenize(g)
        print (tokens, file=utf8stdout)
        text = nltk.Text(tokens)
        print(text)
        text.collocations( )
        break