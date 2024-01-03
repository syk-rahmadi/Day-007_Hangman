#Set up auto word list

import nltk
nltk.download('words')
word_list = nltk.corpus.words.words()

your_word = []
def my_word():
    for word in word_list:
        if len(word) >10:
            your_word.append(word)
    #print(your_word)

my_word()
