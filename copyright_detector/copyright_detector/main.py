#!/usr/bin/env python

import os
import sys, getopt

from tfidf import tf_idf
from similarity import cosine_similarity

def arg_getter():
    copyright_folder_path = ""
    user_text_path = ""
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hc:u:",["copyright_folder_path=","user_text_path="])
    except getopt.GetoptError:
        print('test.py -c <enter path to the folder of copyrighted works> -u <enter full path to new uploaded text file>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('test.py -c <enter path to the folder of copyrighted works> -u <enter full path to new uploaded text file>')
            sys.exit()
        elif opt in ("-c", "--copyright_folder_path"):
            copyright_folder_path = arg
        elif opt in ("-u", "--user_text_path"):
            user_text_path = arg
    return (copyright_folder_path,user_text_path)

if __name__ == "__main__":

    copyrighted_works,user_text_file=arg_getter() # get path to copyrighted works and the name of new uploaded text

    # read the content of new uploaded text
    try:
        with open(user_text_file, "r", encoding='iso-8859-1') as ifile:
            raw_text = ifile.read() # raw text of new uploaded file
    except:
        with open(user_text_file, "r", encoding='utf-8') as ifile:
            raw_text = ifile.read() # raw text of new uploaded file
    tfs_dict1 = tf_idf(raw_text)

    library_path=os.listdir(copyrighted_works)

    files = []
    for file in library_path:
        if file.endswith('.txt'):
            files.append(file)

    for file in files:
        # read text data for each copyrighted content
        # extract TF_IDF terms and values
        # calculate the similarity between this vector and uploaded text file vector

        full_path_file = os.path.join(copyrighted_works, file)
        # read raw texts one by one from copyright library path
        try:
            with open(full_path_file, "r", encoding='iso-8859-1') as ifile:
                raw_text = ifile.read() # raw text of one of copyrighted works
        except:
            with open(full_path_file, "r", encoding='utf-8') as ifile:
                raw_text = ifile.read() # raw text of one of copyrighted works

        tfs_dict2 = tf_idf(raw_text) # dictionary of tfidf terms and values {'tfs_values':tfs_values, 'tfs_term':tfs_term}

        # calculate cosine similarity between this copyrighted work and new uploaded text
        similarity = cosine_similarity(tfs_dict1["tfs_term"], tfs_dict1["tfs_values"], tfs_dict2["tfs_term"], tfs_dict2["tfs_values"])
        print(file, ":          ", similarity)
        ifile.close()
