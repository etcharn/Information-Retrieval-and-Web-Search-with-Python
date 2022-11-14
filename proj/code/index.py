from helper import find_pos_tag, lemmatize_token, add_key_to_term_dict, add_punctuation_to_term_dict
import sys
import os
import re
import string
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)

lemmatizer = WordNetLemmatizer()

# helper function

data_folder_path = sys.argv[1]
# data_folder_path = "/Users/ethancharn/Documents/GitHub/UNSW_INFO/proj/small_D"
# the number of documents in data folder
file_count = 0
# dictionary to store
term_dict = {}
'''
    {
        "hello" : {
            3 : [120, 125, 278], 
            5 : [28], 
            10 : [132, 182], 
            23 : [0, 12, 28], 
            27 : [2] 
        } 
    }
'''
# increase everytime a token is added to term_dict
term_count = 0
# increase everytime a string is considered a token
token_count = 0
# to track index in a file
pos_idx = 0
# verb to be has to be hardcoded as
verb_to_be_list = ['is', 'am', 'are', 'was', 'were']

for docID in os.listdir(data_folder_path):
    with open(os.path.join(data_folder_path, docID), 'r') as f:
        file_count += 1
        pos_idx = 0
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            tokens = re.split(
                "[ *$&#/\t\n\f\"\\\,:;\[\](){}<>~\-_]", line.lower())
            for token in tokens:
                if len(token):
                    # case word is number, ignore it
                    if token.isnumeric():
                        continue
                    # case ' at the end of the word
                    elif token.find("'") != -1:
                        token_split = token.split("'")
                        for token in token_split:
                            # token is a word and not space
                            if len(token):
                                # able to derive pos_tag
                                lemmatized_token = lemmatize_token(token)
                                if add_key_to_term_dict(
                                        term_dict, lemmatized_token, docID, pos_idx):
                                    pos_idx += 1
                                    term_count += 1
                                    token_count += 1
                                else:
                                    pos_idx += 1
                                    token_count += 1
                    # case token is the end of a sentence (having . or ! or ?)
                    # has to be treated specially
                    # separate . or ! or ? out of token first
                    # derive pos_tag to use for lemmatize
                    elif token.find(".") == len(token) - 1 or token.find("!") == len(token) - 1 or token.find("?") == len(token) - 1:
                        # slice out token from the whole token (token + punctuation)
                        token_slice = token[0:len(token)-1]
                        # punctuation is the last index of the token
                        punc = token[len(token)-1]
                        if not token_slice.isnumeric() and token_slice not in string.punctuation:
                            lemmatized_token = lemmatize_token(token_slice)
                            if add_key_to_term_dict(
                                    term_dict, lemmatized_token, docID, pos_idx):
                                pos_idx += 1
                                term_count += 1
                                token_count += 1
                            else:
                                pos_idx += 1
                                token_count += 1
                            add_punctuation_to_term_dict(
                                term_dict, punc, docID, pos_idx)
                            pos_idx += 1
                        # case number followed with punctuation e.g. 123?
                        # still print ? as a mark for end of sentence
                        else:
                            add_punctuation_to_term_dict(
                                term_dict, punc, docID, pos_idx)
                            pos_idx += 1
                    # case . as token divider
                    elif token.find(".") != -1:
                        # remove .
                        token = token.replace(".", "")
                        # lemmatize
                        if not token.isnumeric():
                            lemmatized_token = lemmatize_token(token)
                            if add_key_to_term_dict(term_dict, lemmatize_token, docID, pos_idx):
                                pos_idx += 1
                                term_count += 1
                                token_count += 1
                            else:
                                pos_idx += 1
                                token_count += 1
                    # case token consists of number
                    elif re.search(r'\d', token):
                        token_split = re.split(r'(\d+)', token)
                        for token in token_split:
                            if not token.isnumeric() and len(token):
                                lemmatized_token = lemmatize_token(token)
                                if add_key_to_term_dict(term_dict, lemmatize_token, docID, pos_idx):
                                    pos_idx += 1
                                    term_count += 1
                                    token_count += 1
                                else:
                                    pos_idx += 1
                                    token_count += 1
                    elif token in verb_to_be_list:
                        token = "be"
                        if add_key_to_term_dict(term_dict, token, docID, pos_idx):
                            pos_idx += 1
                            term_count += 1
                            token_count += 1
                        else:
                            pos_idx += 1
                            token_count += 1
                    else:
                        lemmatized_token = lemmatize_token(token)
                        if add_key_to_term_dict(term_dict, lemmatized_token, docID, pos_idx):
                            pos_idx += 1
                            term_count += 1
                            token_count += 1
                        else:
                            pos_idx += 1
                            token_count += 1

# print according to spec
print("Total number of documents:", file_count)
print("Total number of tokens:", token_count)
print("Total number of terms:", term_count)
