from pickle import load
from os import system, name
from os.path import isfile, basename
from nltk import word_tokenize
from feature_extractor.bag_of_words import binary_bag_of_words, counted_bag_of_words


def load_classifier(name_pickle_file):
    with open(name_pickle_file, "rb") as file_handler:
        classificator = load(file_handler)

    return classificator


def cls():
    system('cls' if name=='nt' else 'clear')


def menu():
    menu = "Menu\n\n" \
           "Choose classifier: \n" \
           "a) Naive Bayes Classifier bool\n" \
           "b) Naive Bayes Classifier int\n" \
           "c) Naive Bayes Classifier tfidf\n" \
           "d) LinearSVC Classifier bool\n" \
           "e) LinearSVC Classifier int\n" \
           "f) LinearSVC Classifier tfidf\n" \
           "g) KNeighborsClassifier bool\n" \
           "h) KNeighbors Classifier int\n" \
           "i) KNeighbors Classifier tfidf\n" \
           "j) DecisionTreeClassifier bool\n" \
           "k) DecisionTreeClassifier int\n" \
           "l) DecisionTreeClassifier tfidf\n" \
           "m) LogisticRegression bool\n" \
           "n) LogisticRegression int\n" \
           "o) LogisticRegression tfidf\n" \
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

    print("Loading classifiers ...")
    linear_svc_bool = load_classifier("Classifiers/LinearSVC_bool.pickle")
    linear_svc_int = load_classifier("Classifiers/LinearSVC_int.pickle")
    linear_svc_tfidf = load_classifier("Classifiers/LinearSVC_tfidf.pickle")
    bernulli_nb_bool = load_classifier("Classifiers/BernoulliNB_bool.pickle")
    bernulli_nb_int = load_classifier("Classifiers/BernoulliNB_int.pickle")
    bernulli_nb_tfidf = load_classifier("Classifiers/BernoulliNB_tfidf.pickle")
    decision_trees_bool = load_classifier("Classifiers/DecisionTreeClassifier_bool.pickle")
    decision_trees_int = load_classifier("Classifiers/DecisionTreeClassifier_int.pickle")
    decision_trees_tfidf = load_classifier("Classifiers/DecisionTreeClassifier_tfidf.pickle")
    k_nearest_bool = load_classifier("Classifiers/KNeighborsClassifier_bool.pickle")
    k_nearest_int = load_classifier("Classifiers/KNeighborsClassifier_int.pickle")
    k_nearest_tfidf = load_classifier("Classifiers/KNeighborsClassifier_tfidf.pickle")
    logistic_regression_bool = load_classifier("Classifiers/LogisticRegression_bool.pickle")
    logistic_regression_int = load_classifier("Classifiers/LogisticRegression_int.pickle")
    logistic_regression_tfidf = load_classifier("Classifiers/LogisticRegression_tfidf.pickle")
    cls()

    while True:
        menu()
        user_input = input("Choose option: ")

        if user_input.lower() in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']:
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
                elif user_input.lower() == 'g':
                    classify(path, k_nearest_bool, binary_bag_of_words)
                elif user_input.lower() == 'h':
                    classify(path, k_nearest_int, counted_bag_of_words)
                elif user_input.lower() == 'i':
                    classify(path, k_nearest_tfidf, counted_bag_of_words)
                elif user_input.lower() == 'j':
                    classify(path, decision_trees_bool, binary_bag_of_words)
                elif user_input.lower() == 'k':
                    classify(path, decision_trees_int, counted_bag_of_words)
                elif user_input.lower() == 'l':
                    classify(path, decision_trees_tfidf, counted_bag_of_words)
                elif user_input.lower() == 'm':
                    classify(path, logistic_regression_bool, binary_bag_of_words)
                elif user_input.lower() == 'n':
                    classify(path, logistic_regression_int, counted_bag_of_words)
                elif user_input.lower() == 'o':
                    classify(path, logistic_regression_tfidf, counted_bag_of_words)
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
