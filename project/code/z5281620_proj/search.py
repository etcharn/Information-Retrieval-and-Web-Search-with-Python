# helper function
from helper import modify_phrase, modify_or, print_formatted_output
from helper import process_phrase, process_or, process_plus_n, process_slash_n
from helper import process_plus_s, process_slash_s, process_and
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
    # case there's only one word in the query
    if len(query.split(" ")) == 1:
        term = query.split(" ")[0]
        if term in term_dict.keys():
            res_dict = term_dict[term]
            for docID in term_dict[term].keys():
                term_pos_lst = term_dict[term][docID]
                res = [docID, term_pos_lst]
                ans_lst.append(res)   
        print_formatted_output(term_dict, [ans_lst])
    # case complex query
    elif query.find("(") != -1:
        pass
    # case not a complex query
    else:
        # modify "term_1 term_2 ... term_n"
        # into (term1 +1 term_2 +1 ... +1 term_n)
        modified_query = modify_phrase(query)
        # add | for all or operation
        modified_query = modify_or(modified_query)
        # query processing for " "
        ans_lst = process_phrase(term_dict, modified_query)
        # query processing for | (or)
        ans_lst = process_or(term_dict, ans_lst)
        # query processing for +n
        ans_lst = process_plus_n(term_dict, ans_lst)
        # query processing for /n
        ans_lst = process_slash_n(term_dict, ans_lst)
        # query processing for +s
        ans_lst = process_plus_s(term_dict, ans_lst)
        # query processing for /s
        ans_lst = process_slash_s(term_dict, ans_lst)
        # query processing for & (and)
        ans_lst = process_and(term_dict, ans_lst)
        # print the output as the given format
        print_formatted_output(term_dict, ans_lst)
        

            

            
      