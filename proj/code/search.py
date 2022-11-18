# helper function
from helper import modify_phrase, process_phrase, modify_or
# file system
import sys
import os
import json

index_folder_path = sys.argv[1]

with open(os.path.join(index_folder_path, "index.json"), 'r') as json_file:
    term_dict = json.load(json_file)

# infinite loop input
while True:
    ans_lst = []
    query = input("")
    # make lower case
    query = query.lower()
    # inputs.append(inp)
    if query.find('"') != -1:
        modified_query = modify_phrase(query)
        modified_query = modify_or(modified_query)
        ans = process_phrase(modified_query)
        if len(ans) != 1:
            

            
      