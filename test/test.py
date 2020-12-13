#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 15:14:58 2020

@author: sm.marouzigmail.com
"""

from tfidf import tf_idf
from similarity import cosine_similarity

import os
copyrighted_works='/Users/sm.marouzigmail.com/Documents/job/wattpad/library/'
user_text_file = '/Users/sm.marouzigmail.com/Documents/job/wattpad/test/test.txt'

# read the content of new uploaded text
try:
    with open(user_text_file, "r", encoding='iso-8859-1') as ifile:
        raw_text = ifile.read() # raw text of new uploaded file
except:
    with open(user_text_file, "r", encoding='utf-8') as ifile:
        raw_text = ifile.read() # raw text of new uploaded file
tfs_dict1 = tf_idf(raw_text)


library_path=os.listdir(copyrighted_works)

# list of text files
files = [file for file in library_path if file.endswith('.txt')]

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
    print(file, ":   ", similarity)
    ifile.close()


    
    
    
    