import nltk
import string


# nltk.download('stopwords')

# Tokenize
def tokenize(raw_text):
    """
    This function takes raw text and tokenize it to its words
    Args:
        raw_text (string): the complete text
    return:
        tokenized_text (list): list of all words in input text
    """
    tokenized_text = nltk.tokenize.word_tokenize(raw_text)
    return tokenized_text

# convert to losercase
def lowercase(raw_text):
    """
    This function convert all input text characters to lowercase
    Args:
        raw_text (string): the complete text
    return:
        lowercase_text (string): lowercased text
    """
    lowercase_text = [text.lower() for text in raw_text]
    return lowercase_text

# remove stop words
def remove_stop_words(tokenized_word_list):
    """
    This function takes the list of tokenized words and returns list without stopwords.
    Args:
        tokenized_word_list (list): list of tokenized words
    return:
        filtered_tokens (list): list of words minus stop words
    """
    stop_words = set(nltk.corpus.stopwords.words("english"))
    filtered_tokens = [word for word in tokenized_word_list if word not in stop_words]
    return filtered_tokens

# remove punctuations
def remove_punctuations(tokenized_word_list):
    """
    This function removes punctuations from the list of tokenized words
    Args:
        tokenized_word_list (list): list of tokenized words
    return:
        filtered_tokens (list): list of words minus punctuations
    """
    puncuations = set(string.punctuation)

    double_quote = '\'\''
    double_sign = '``'

    puncuations.add(double_quote)
    puncuations.add(double_sign)

    filtered_tokens = [word for word in tokenized_word_list if word not in puncuations]
    return filtered_tokens

# Lemmatization
def lemmatization(tokenized_word_list):
    """
    Stemming and Lemmatization helps us to achieve the root forms
    (sometimes called synonyms in search context) of inflected (derived) words.
    ref: https://www.datacamp.com/community/tutorials/stemming-lemmatization-python
    Args:
        tokenized_word_list (list): list of tokenized words
    return:
        filtered_tokens (list): list of words as the root of words
    """
    porter=nltk.stem.PorterStemmer()
    filtered_tokens = [porter.stem(word) for word in tokenized_word_list]
    return filtered_tokens

def preprocessing(raw_text):
    """
    do all preprocessing steps at this section.
    """
    words_list = tokenize(raw_text)
    words_list = remove_stop_words(words_list)
    words_list = remove_punctuations(words_list)
    words_list = lemmatization(words_list)
    return words_list
