import string
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)

lemmatizer = WordNetLemmatizer()


def find_pos_tag(token):
    '''
    find pos_tag of the token
    '''
    pos_tag_list = wn.synsets(token)
    if len(pos_tag_list):
        return wn.synsets(token)[0].pos()
    else:
        return False


def lemmatize_token(token):
    '''
    lemmatize the token
    '''
    pos_tag = find_pos_tag(token)
    if find_pos_tag(token):
        lemmatized_token = lemmatizer.lemmatize(
            token, pos_tag)
        return lemmatized_token
    else:
        lemmatized_token = lemmatizer.lemmatize(
            token)
        return lemmatized_token


def add_key_to_term_dict(term_dict, term, docID, pos_idx):
    '''
    add a term to term_dict
    '''
    # token isn't in term_dict
    if term not in term_dict.keys():
        term_dict[term] = {}
        term_dict[term][docID] = []
        term_dict[term][docID].append(
            pos_idx)
        return 1
    # case the token is already in term_dict
    elif term in term_dict.keys():
        if docID in term_dict[term].keys():
            term_dict[term][docID].append(
                pos_idx)
        else:
            term_dict[term][docID] = []
            term_dict[term][docID].append(
                pos_idx
            )


def add_punctuation_to_term_dict(term_dict, punc, docID, pos_idx):
    '''
    add a punctuation to term_dict
    '''
    # the punctuation isn't in term_dict
    if punc not in term_dict.keys():
        term_dict[punc] = {}
        term_dict[punc][docID] = []
        term_dict[punc][docID].append(
            pos_idx)

    # case the token is already in term_dict
    elif punc in term_dict.keys():
        if docID in term_dict[punc].keys():
            term_dict[punc][docID].append(
                pos_idx)
        else:
            term_dict[punc][docID] = []
            term_dict[punc][docID].append(
                pos_idx
            )
