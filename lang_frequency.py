import collections
import re


def load_data(filepath):
    with open(filepath) as file:
        file_text = file.read()
    return file_text


def get_most_frequent_words(text):
    word_frequency = {}
    words = []
    words = re.findall('\w+', text.lower())
    word_frequency = collections.Counter(words).most_common(10)
    print ("10 наиболее часто встречающихся слов:")
    for word in word_frequency:
        print (("%s - %s повторений") % (word[0], word[1]))

if __name__ == '__main__':
    get_most_frequent_words(load_data('file.txt'))
