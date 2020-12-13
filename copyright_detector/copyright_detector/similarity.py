
import numpy as np

def cosine_similarity(tfs_term1,tfs_values1, tfs_term2, tfs_values2):
    """
    this function receives tfidf terms and values for two texts
    calculate cosine similarity for those two texts
    Args:
        tfs_term1 (list): list of tfidf names for first text
        tfs_values1 (ndarray): (1,len(tf_terms) array with tfidf values for each term
        tfs_term2 (list): list of tfidf names for second text
        tfs_values2 (ndarray): (1,len(tf_terms) array with tfidf values for each term
    returns:
        cosine_similarity (float): similarity metric for two selected texts
    """
    # create a dictionary of term:value for tfidf1 and tfidf2
    tfs1 = {tfs_term1[i]: tfs_values1[0][i] for i in range(len(tfs_term1))}
    tfs2 = {tfs_term2[i]: tfs_values2[0][i] for i in range(len(tfs_term2))}

    cosine_dot = 0

    tfs1Set = set(tfs1)
    tfs2Set = set(tfs2)
    
    for key in tfs1Set.intersection(tfs2Set):
        cosine_dot+= tfs1[key] * tfs2[key]
    # cosine norms
    tfs_values1_norm = np.sqrt(sum(sum(tfs_values1**2)))
    tfs_values2_norm = np.sqrt(sum(sum(tfs_values2**2)))

    # cosine similarity
    cosine_similarity = cosine_dot/(tfs_values1_norm*tfs_values2_norm)

    return cosine_similarity
