from sklearn.feature_extraction.text import TfidfVectorizer
from preprocessing import preprocessing

def tf_idf(raw_text):
    # calculate tfidf
    tfidf = TfidfVectorizer(tokenizer=preprocessing)
    tfs = tfidf.fit_transform([raw_text])
    tfs_values = tfs.toarray()
    tfs_term = tfidf.get_feature_names()
    return {'tfs_values':tfs_values, 'tfs_term':tfs_term}
