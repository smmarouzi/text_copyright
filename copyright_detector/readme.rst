# TFIDF and Cosine similarity

after searching around different methods to find the similarity between two texts,
I decided to continue with this method.
I did not have much time to experiment with more complicated methods so I found
"TF_IDF + Cosine Similarity" good enough as an answer for this assignment.
I tried with Levenshtein_distance metric as well. The function is provided but I did not continue with it.

## Overview
The steps to implement similarity detection between two separate texts are:
    - Preprocessing and cleaning text data (word tokenizing, convert to lower case, remove punctuations, remove stop words, Lemmatization)
    - Apply TF-IDF to find important words in corpus
    - Apply vectorization
    - Calculate pairwise Cosine similarity between each two texts

## How to use
In command window go to the path which new uploaded text is saved
then type this command:
    - make your virtual env and go to this environment
    - go to this path "~/text_copyright/copyright_detector"
    - run $ pip install -r requirements.txt
    - go to this path "~/text_copyright/copyright_detector/copyright_detector"
    - define two environment variables:
        - copyrighted_works = <path to folder of saved copyrighted works> (~/copyrighted_works)
        - new_text_file = <path to new uploaded file> (~/user_input_1.txt)
    - run $ chmod +x main.py in command window
    - run $ ./main.py -c $copyrighted_works -u $new_text_file

for example run:
                $ copyrighted_works="~/copyrighted_works"
                $ new_text_file="~/user_input_1.txt"
                $ ./main.py -c $copyrighted_works -u $new_text_file

you can install copyright_detector as a package
    - go to this path "~/text_copyright/copyright_detector"
    - run $ pip install .
