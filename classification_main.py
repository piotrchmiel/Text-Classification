from pickle import load
from os import system, name
from os.path import isfile, basename
from feature_extractor.bag_of_words import binary_bag_of_words, counted_bag_of_words
from nltk import word_tokenize

def load_classificator(name_pickle_file):
    with open(name_pickle_file, "rb") as file_handler:
        classificator = load(file_handler)

    return classificator

def cls():
    system('cls' if name=='nt' else 'clear')

def menu():
    menu = "Menu\n\n" \
           "Choose classificator: \n" \
           "a) Naive Bayes Classificator Bool\n" \
           "b) Naive Bayes Classificator Int\n" \
           "c) Naive Bayes Classificator tfidf\n" \
           "d) LinearSVC Classificator Bool\n" \
           "e) LinearSVC Classificator Int\n" \
           "f) LinearSVC Classificator tfidf\n" \
           "q) Quit\n"

    print(menu)

def classify(path, classificator, bag_of_words_feature_extractor):
        try:
            with open(path, 'rt', encoding="utf-8") as file_handler:
                content = file_handler.read()
        except Exception as e:
            print ("File exception: ", e)
        else:
            label = classificator.classify(bag_of_words_feature_extractor(word_tokenize(content)))
            print("Text: {0} \nClassifier result: {1}\n".format(basename(path), label))

def main():

    print("Loading classificators ...")
    linear_svc_bool = load_classificator("Classificators/LinearSVC_bool.pickle")
    linear_svc_int = load_classificator("Classificators/LinearSVC_int.pickle")
    linear_svc_tfidf = load_classificator("Classificators/LinearSVC_tfidf.pickle")
    bernulli_nb_bool = load_classificator("Classificators/BernoulliNB_bool.pickle")
    bernulli_nb_int = load_classificator("Classificators/BernoulliNB_int.pickle")
    bernulli_nb_tfidf = load_classificator("Classificators/BernoulliNB_tfidf.pickle")
    cls()

    while True:
        menu()
        user_input = input("Choose option: ")

        if user_input.lower() in ['a', 'b', 'c', 'd', 'e', 'f']:
            path = input("Please enter file path: ")
            print("Entered path {0}".format(path))
            if isfile(path):
                if user_input.lower() == 'a':
                    classify(path, bernulli_nb_bool, binary_bag_of_words)
                elif user_input.lower() == 'b':
                    classify(path, bernulli_nb_int, counted_bag_of_words)
                elif user_input.lower() == 'c':
                    classify(path, bernulli_nb_tfidf, counted_bag_of_words)
                elif user_input.lower() == 'd':
                    classify(path, linear_svc_bool, binary_bag_of_words)
                elif user_input.lower() == 'e':
                    classify(path, linear_svc_int, counted_bag_of_words)
                elif user_input.lower() == 'f':
                    classify(path, linear_svc_tfidf, counted_bag_of_words)
            else:
                print ("There is no such file. Try again !")
        elif user_input.lower() == 'q':
            break
        else:
            print("Unknown option. Try again !")

        input("Press any key ...")
        cls()

    input("Press any key ...")
    cls()

if __name__ == '__main__':
    main()
