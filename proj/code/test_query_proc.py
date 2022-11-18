# helper function
from helper import process_plus_one, modify_phrase, process_phrase, print_formatted_output
from helper import modify_or, process_or, process_plus_n, process_slash_n, find_previous_punctuation_index
from helper import process_plus_s
# file system
import sys
import os
import json

index_folder_path = "/Users/ethancharn/Documents/GitHub/UNSW_INFO/proj/index"

with open(os.path.join(index_folder_path, "index.json"), 'r') as json_file:
    term_dict = json.load(json_file)

query = '"cumulative total" +s "last year"'

query = query.lower()

modified_query = modify_phrase(query)

print(modified_query)

modified_query = modify_or(modified_query)

print(modified_query)

ans_lst = process_phrase(term_dict, modified_query)

print(ans_lst)

ans_lst = process_or(term_dict, ans_lst)

print(ans_lst)

ans_lst = process_plus_n(term_dict, ans_lst)

print(ans_lst)

ans_lst = process_slash_n(term_dict, ans_lst)

print(ans_lst)

ans_lst = process_plus_s(term_dict, ans_lst)

print(ans_lst)

print_formatted_output(ans_lst)
