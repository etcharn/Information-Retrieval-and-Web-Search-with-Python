import sys
import os
import re
import string
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn


lemmatizer = WordNetLemmatizer()

word = 'cats'

pos_tag_list = wn.synsets(word)
if len(pos_tag_list):
    pos_tag = wn.synsets(word)[0].pos()
    print(pos_tag)
    print(lemmatizer.lemmatize(word, pos_tag))
else:
    print(lemmatizer.lemmatize(word))
