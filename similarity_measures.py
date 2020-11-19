#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 14:16:05 2020

@author: stevenyuan
"""
import doctest
import vectors_utils

def get_semantic_descriptor(word, sentence):
    '''
    given a string w representing a single word and a list 
    s representing all the words in a sentence, returns a 
    dictionary representing the semantic descriptor vector 
    of the word w computed from the sentence s.

    Parameters
    ----------
    word : String
    sentence : list

    Returns
    -------
    Dictionary
    
    >>> s1 = ['all', 'the', 'habits', 'of', 'man', 'are', 'evil']
    >>> s2 = ['no', 'animal', 'must', 'ever', 'kill', 'any', 'other', 'animal']
    >>> desc1 = get_semantic_descriptor('evil', s1)
    >>> desc1['all']
    1
    >>> len(desc1)
    6
    >>> 'animal' in desc1
    False
    >>> desc2 = get_semantic_descriptor('animal', s2)
    >>> desc2 == {'no': 1, 'must': 1, 'ever': 1, 'kill': 1, 'any': 1, 'other': 1}
    True
    >>> get_semantic_descriptor('animal', s1)
    {}
    '''
    result = {}
    if word in sentence:
        for w in sentence:
            if(w != word):
                if w in result:
                    result[w] += 1
                else:
                    result[w] = 1
    return result
    
def get_all_semantic_descriptors(sentences):
    '''
    takes as input a list of lists representing the words 
    in a text, where each sentence in a text is represented 
    by a sublist of the input list. The function returns a 
    dictionary d such that for every word w that appears in 
    at least one of the sentences, d[w] is itself a dictionary 
    which represents the semantic descriptor vector of w

    Parameters
    ----------
    sentences : 2D list

    Returns
    -------
    Dictionary
    
    >>> s = [['all', 'the', 'habits', 'of', 'man', 'are', 'evil'], \
         ['and', 'above',  'all', 'no', 'animal', 'must', 'ever', 'tyrannise', 'over', 'his', 'own', 'kind'], \
         ['weak', 'or', 'strong', 'clever', 'or',  'simple', 'we', 'are', 'all', 'brothers'], \
         ['no', 'animal', 'must', 'ever', 'kill', 'any', 'other', 'animal'], \
         ['all', 'animals', 'are', 'equal']]
    >>> d = get_all_semantic_descriptors(s)
    >>> d['animal']['must']
    3
    >>> d['evil'] ==  {'all': 1, 'the': 1, 'habits': 1, 'of': 1, 'man': 1, 'are': 1}
    True

    '''
    result = {}
    for s in sentences:
        for w in s:
            if w not in result:
                result[w] = get_semantic_descriptor(w, s)
            else:
                tmp = get_semantic_descriptor(w, s)
                vectors_utils.add_vectors(result[w], tmp)
    return result
    
def get_cos_sim(d1, d2):
    '''
    given two dictionaries representing similarity descriptor 
    vectors, returns the co- sine similarity between the two.

    Parameters
    ----------
    d1 : Dictionary
    d2 : Dictionary

    Returns
    -------
    int
    
    >>> round(get_cos_sim({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6}), 2)
    0.7
    >>> s = [['all', 'the', 'habits', 'of', 'man', 'are', 'evil'], \
       ['and', 'above',  'all', 'no', 'animal', 'must', 'ever', 'tyrannise', 'over', 'his', 'own', 'kind'], \
       ['weak', 'or', 'strong', 'clever', 'or',  'simple', 'we', 'are', 'all', 'brothers'], \
       ['no', 'animal', 'must', 'ever', 'kill', 'any', 'other', 'animal'], \
       ['all', 'animals', 'are', 'equal']]
    >>> d = get_all_semantic_descriptors(s)
    >>> v1 = d['evil']
    >>> v2 = d['animal']
    >>> round(get_cos_sim(v1, v2), 4)
    0.0595
    '''
    dot_product = vectors_utils.get_dot_product(d1, d2)
    norm = vectors_utils.get_vector_norm(d1) * vectors_utils.get_vector_norm(d2)
    result = dot_product / norm
    return result

def get_euc_sim(v1, v2):
    '''
    given two dictionaries representing similarity descriptor 
    vectors, returns the similarity between the two using the 
    negative euclidean distance.

    Parameters
    ----------
    v1 : Dictionary
    v2 : Dictionary

    Returns
    -------
    int
    
    >>> round(get_euc_sim({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6}), 2)
    -6.71
    >>> s = [['all', 'the', 'habits', 'of', 'man', 'are', 'evil'], \
       ['and', 'above',  'all', 'no', 'animal', 'must', 'ever', 'tyrannise', 'over', 'his', 'own', 'kind'], \
       ['weak', 'or', 'strong', 'clever', 'or',  'simple', 'we', 'are', 'all', 'brothers'], \
       ['no', 'animal', 'must', 'ever', 'kill', 'any', 'other', 'animal'], \
       ['all', 'animals', 'are', 'equal']]
    >>> d = get_all_semantic_descriptors(s)
    >>> v1 = d['evil']
    >>> v2 = d['animal']
    >>> round(get_euc_sim(v1, v2), 4)
    -7.1414

    '''
    diff = vectors_utils.sub_vectors(v1, v2)
    norm = vectors_utils.get_vector_norm(diff)
    result = - norm
    return result

def get_norm_euc_sim(v1,v2):
    '''
    given two dictionaries representing similarity descriptor 
    vectors, returns the similarity between the two using 
    the negative euclidean distance between the normalized vectors.

    Parameters
    ----------
    v1 : Dictionary
    v2 : Dictionary

    Returns
    -------
    int
    
    >>> round(get_norm_euc_sim({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6}), 2)
    -0.77
    >>> s = [['all', 'the', 'habits', 'of', 'man', 'are', 'evil'], \
       ['and', 'above',  'all', 'no', 'animal', 'must', 'ever', 'tyrannise', 'over', 'his', 'own', 'kind'], \
       ['weak', 'or', 'strong', 'clever', 'or',  'simple', 'we', 'are', 'all', 'brothers'], \
       ['no', 'animal', 'must', 'ever', 'kill', 'any', 'other', 'animal'], \
       ['all', 'animals', 'are', 'equal']]
    >>> d = get_all_semantic_descriptors(s)
    >>> v1 = d['evil']
    >>> v2 = d['animal']
    >>> round(get_norm_euc_sim(v1, v2), 4)
    -1.3715
    '''
    vectors_utils.normalize_vector(v1)
    vectors_utils.normalize_vector(v2)
    result = get_euc_sim(v1, v2)
    return result

if __name__ == '__main__':
    doctest.testmod()