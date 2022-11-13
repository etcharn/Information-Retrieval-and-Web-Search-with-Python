import sys
import os
import re
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn


lemmatizer = WordNetLemmatizer()

word_list = ['tom', "can", 'I', 'shoe', 'it', 'he', 'she', 'there', 'here']

for word in word_list:
    pos_tag = nltk.pos_tag(list(word))[0]
    print(f"{word} is {pos_tag}")

# print(lemmatizer.lemmatize(word, pos_tag))
