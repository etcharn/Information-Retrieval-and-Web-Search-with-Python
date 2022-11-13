import sys
import os
import re
import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)

data_folder_path = sys.argv[1]
# the number of documents in data folder
file_count = 0
token_count = 0
term_count = 0
lemmatizer = WordNetLemmatizer()

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
                    if word.find(".") == len(word)-1 or word.find(".") != -1:
                        print(word.replace(".", ""))
                    elif word.find("'") != -1:
                        word.split("")
                    elif word.isnumeric():
                        continue
                    else:
                        print(lemmatizer.lemmatize(word))

# print according to spec
print("Total number of documents:", file_count)
print("Total number of tokens:", token_count)
print("Total number of terms:", term_count)
