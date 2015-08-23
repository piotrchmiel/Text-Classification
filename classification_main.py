from pickle import load
from os import system, name
from os.path import isfile, basename
from feature_extractor.bag_of_words import bag_of_words
from nltk import word_tokenize

def load_classificator(name_pickle_file):
    with open(name_pickle_file, "rb") as file_handler:
        naive_bayes_classificator = load(file_handler)

    return naive_bayes_classificator

def cls():
    system('cls' if name=='nt' else 'clear')

def menu():
    menu = "Menu\n\n" \
           "Choose classificator: \n" \
           "a) Naive Bayes Classificator: \n" \
           "q) Quit\n"

    print(menu)

def main():

    print("Loading classificators ...")
    naive_bayes_classificator = load_classificator("naive_bayes_classifier.pickle")
    cls()
    while True:
        menu()
        user_input = input("Choose option: ")

        if user_input.lower() not in ['a', 'q']:
            print("Unknown option. Try again !")
        elif user_input.lower() == 'a':
            path = input("Please enter file path: ")
            print("Entered path {0}".format(path))
            if isfile(path):
                try:
                    with open(path, 'rt', encoding="utf-8") as file_handler:
                        content = file_handler.read()
                except Exception as e:
                    print ("File exception: ", e)
                else:
                    label = naive_bayes_classificator.classify(bag_of_words(word_tokenize(content)))
                    print("Text: {0} \nClassifier result: {1}\n".format(basename(path), label))
            else:
                print ("There is no such file. Try again !")
        elif user_input.lower() == 'q':
            break

        input("Press any key ...")
        cls()

    input("Press any key ...")
    cls()

if __name__ == '__main__':
    main()
