
import profile


def remove_duplicates(in_list):

    return list(set(in_list))


def list_unique_words(text):
    words = text.lower().split()
    unique = remove_duplicates(words)
    return unique


def extract_and_get_unique_words(filename):

    unique_words = []
    with open(filename) as f:
        text = f.read()
        unique_words = list_unique_words(text)
    return unique_words


FILENAME = "./testing_files/Anne-Frank-The-Diary-Of-A-Young-Girl.txt"
profile.run('extract_and_get_unique_words(FILENAME)', sort='tottime')
