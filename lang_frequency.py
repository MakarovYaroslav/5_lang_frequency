import collections
import re


def load_data(filepath):
    with open(filepath) as file:
        file_text = file.read()
    return file_text


def get_most_frequent_words(text, word_amount=10):
    word_frequency = {}
    words = []
    words = re.findall('\w+', text.lower())
    word_frequency = collections.Counter(words).most_common(word_amount)
    print ("%d наиболее часто встречающихся слов:" % word_amount)
    for word in word_frequency:
        print (("%s - %s повторений") % (word[0], word[1]))

if __name__ == '__main__':
    get_most_frequent_words(load_data('file.txt'))
