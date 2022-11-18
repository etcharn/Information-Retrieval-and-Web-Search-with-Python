
# helper function
from helper import find_pos_tag, lemmatize_token, add_key_to_term_dict, add_punctuation_to_term_dict
# file system
import sys
import os
import json
import ujson
# pre-processing
import re
import string
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)

lemmatizer = WordNetLemmatizer()


data_folder_path = sys.argv[1]
index_folder_path = sys.argv[2]
# data_folder_path = "/Users/ethancharn/Documents/GitHub/UNSW_INFO/proj/data"
# index_folder_path = "/Users/ethancharn/Documents/GitHub/UNSW_INFO/proj/index"
# the number of documents in data folder
file_count = 0
# dictionary to store
term_dict = {}
'''
    {
        "term" : {
            docID : pos_idx_list_for_docID, 
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

for docID in os.listdir(data_folder_path):
    with open(os.path.join(data_folder_path, docID), 'r') as f:
        # incerment the number of file read
        file_count += 1
        # reset index when read new file
        pos_idx = 0
        # read text file line by line
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            # split the line into tokens
            tokens = re.split(
                "[ *$&#/\t\n\f\"\\\,:;\[\](){}<>~\-_]", line.lower())
            # for each token, treat them as spec mentioned
            for token in tokens:
                if len(token):
                    # case token is number, ignore it
                    if token.isnumeric():
                        pass
                    # case the token has ', split with '
                    # then lemmatize the token and add to term_dict
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
                    # by separating . or ! or ? out of token
                    # and add both token and punctuation to term_dict
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
                        # case token consists of number followed with punctuation e.g. 123?
                        # still add ? to term_dict as the indicator for end of sentence
                        else:
                            add_punctuation_to_term_dict(
                                term_dict, punc, docID, pos_idx)
                            pos_idx += 1
                    # case the token is abbreviation having . as token divider
                    # get rid of . and lemmatize the token
                    # before add to term_dict
                    elif token.find(".") != -1:
                        token = token.replace(".", "")
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
                    # get rid of number, lemmatize the token
                    # and add to term_dict
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
                    # token is a verb-to-be
                    # hardcoded because wn.synsets not able to
                    # derive the right pos_tag to be used for lemmatizing it
                    elif token in ['is', 'am', 'are', 'was', 'were']:
                        token = "be"
                        if add_key_to_term_dict(term_dict, token, docID, pos_idx):
                            pos_idx += 1
                            term_count += 1
                            token_count += 1
                        else:
                            pos_idx += 1
                            token_count += 1
                    # for all other cases, just lemmatize the token
                    # and add to term_dict
                    else:
                        lemmatized_token = lemmatize_token(token)
                        if add_key_to_term_dict(term_dict, lemmatized_token, docID, pos_idx):
                            pos_idx += 1
                            term_count += 1
                            token_count += 1
                        else:
                            pos_idx += 1
                            token_count += 1

# save term_dict as json
with open(os.path.join(index_folder_path, "index.json"), 'w') as outfile:
    ujson.dump(term_dict, outfile)

    # print according to spec
print("Total number of documents:", file_count)
print("Total number of tokens:", token_count)
print("Total number of terms:", term_count)
