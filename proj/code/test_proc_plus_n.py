# helper function
from helper import process_plus_n, preprocess, lemmatize_token
# file system
import sys
import os
import json

index_folder_path = "/Users/ethancharn/Documents/GitHub/UNSW_INFO/proj/index"

with open(os.path.join(index_folder_path, "index.json"), 'r') as json_file:
    term_dict = json.load(json_file)


print(process_plus_n(term_dict, "company", "move", 5))
