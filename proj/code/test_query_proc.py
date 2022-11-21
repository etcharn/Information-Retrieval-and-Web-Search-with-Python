# helper function
from helper import process_plus_one, modify_phrase, process_phrase, print_formatted_output
from helper import modify_or, process_or, process_plus_n, process_slash_n, find_previous_punctuation_index
from helper import process_plus_s, find_next_punctuation_index, process_slash_s, process_and
# file system
import sys
import os
import json

index_folder_path = "/Users/ethancharn/Documents/GitHub/UNSW_INFO/proj/index"

with open(os.path.join(index_folder_path, "index.json"), 'r') as json_file:
    term_dict = json.load(json_file)

query = 'bahia'

query = query.lower()

print(query.split(" "))

modified_query = modify_phrase(query)
print(f"after mod phrase      {modified_query}")

modified_query = modify_or(modified_query)
print(f"after mod or          {modified_query}")

ans_lst = process_phrase(term_dict, modified_query)
print(f"after proc phrase     {ans_lst}")

ans_lst = process_or(term_dict, ans_lst)
print(f"after proc or         {ans_lst}")


ans_lst = process_plus_n(term_dict, ans_lst)
print(f"after proc +n         {ans_lst}")

ans_lst = process_slash_n(term_dict, ans_lst)
print(f"after proc /n         {ans_lst}")


ans_lst = process_plus_s(term_dict, ans_lst)
print(f"after proc +s         {ans_lst}")

ans_lst = process_slash_s(term_dict, ans_lst)
print(f"after proc /s         {ans_lst}")

ans_lst = process_and(term_dict, ans_lst)
print(f"after proc and        {ans_lst}")

print_formatted_output(term_dict, ans_lst)
