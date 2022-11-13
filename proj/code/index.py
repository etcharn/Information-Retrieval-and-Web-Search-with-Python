import sys
import os
import re
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)


data_folder_path = sys.argv[1]
# the number of documents in data folder
file_count = 0
token_count = 0
term_count = 0
lemmatizer = WordNetLemmatizer()
verb_to_be_list = ['is', 'am', 'are', 'was', 'were']
adjective_list = ['worst', 'better']

# for path in os.listdir(data_folder_path):
with open(os.path.join(data_folder_path, "6.txt"), 'r') as f:
    file_count += 1
    line_count = 0
    lines = f.readlines()
    for line in lines:
        if line:
            line = line.strip()
            words = re.split(
                "[ *$&#/\t\n\f\"\\\,:;?!\[\](){}<>~\-_]", line.lower())
            for word in words:
                if len(word):
                    pos_tag_list = wn.synsets(word)
                    if len(pos_tag_list):
                        pos_tag = wn.synsets(word)[0].pos()
                    if word.find(".") == len(word) - 1 or word.find(".") != -1:
                        word = word.replace(".", "")
                        print(lemmatizer.lemmatize(word))
                    elif word.find("'") == len(word) - 1:
                        word_split = word.split("'")
                        for word in word_split:
                            if len(word):
                                print(lemmatizer.lemmatize(word, pos_tag))
                    elif word.find("'") != -1:
                        word_split = word.split("'")
                        for word in word_split:
                            print(word)
                    # case word is number, ignore it
                    elif word.isnumeric():
                        continue
                    # case word having number
                    elif re.search(r'\d', word):
                        word_split = re.split(r'(\d+)', word)
                        for word in word_split:
                            if word.isnumeric() == False and len(word):
                                print(word)
                    elif word in verb_to_be_list:
                        word = "be"
                        print(word)
                    elif word in adjective_list:
                        print(lemmatizer.lemmatize(word, 'a'))
                    else:
                        if len(pos_tag_list):
                            print(lemmatizer.lemmatize(word, pos_tag))
                        else:
                            print(lemmatizer.lemmatize(word))

# print according to spec
print("Total number of documents:", file_count)
print("Total number of tokens:", token_count)
print("Total number of terms:", term_count)
