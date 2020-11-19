#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 20:21:38 2020

@author: stevenyuan
"""
import doctest
import vectors_utils
import similarity_measures

PUNCTUATION = ['.', '!', '?']
OTHER_PUNCTUATION = [',', '-', '--', ':', ';', '"', "'"]


def get_sentences(paragraph):
    '''
    given a string returns a list of strings each representing 
    one of the sentences from the input string.

    Parameters
    ----------
    paragraph : String

    Returns
    -------
    list
    
    >>> text = "No animal must ever kill any other animal. All animals are equal."
    >>> get_sentences(text)
    ['No animal must ever kill any other animal', 'All animals are equal']
    >>> t = "Are you insane? Of course I want to leave the Dursleys! Have you got a house? When can I move in?"
    >>> get_sentences(t)
    ['Are you insane', 'Of course I want to leave the Dursleys', 'Have you got a house', 'When can I move in']
    '''
    result = []
    tmp = ''
    i = 0
    while(i < len(paragraph)):
        if paragraph[i] not in PUNCTUATION:
            tmp += paragraph[i]
            i += 1
        else:
            result.append(tmp)
            tmp = ''
            i += 2
    return result

def get_word_breakdown(paragraph):
    '''
    given a string returns a 2D lists of strings. 
    Each sublist contains a strings representing words from each sentence.

    Parameters
    ----------
    paragraph : String

    Returns
    -------
    2D list

    >>> text = "All the habits of Man are evil. And, above all, no animal must ever tyrannise over his own kind. Weak or strong, clever or simple, we are all brothers. No animal must ever kill any other animal. All animals are equal."
    >>> s = [['all', 'the', 'habits', 'of', 'man', 'are', 'evil'], \
         ['and', 'above',  'all', 'no', 'animal', 'must', 'ever', 'tyrannise', 'over', 'his', 'own', 'kind'], \
         ['weak', 'or', 'strong', 'clever', 'or',  'simple', 'we', 'are', 'all', 'brothers'], \
         ['no', 'animal', 'must', 'ever', 'kill', 'any', 'other', 'animal'], \
         ['all', 'animals', 'are', 'equal']]
    >>> w = get_word_breakdown(text)
    >>> s == w
    True
    '''
    
    split = OTHER_PUNCTUATION + [' ']
    sentences = get_sentences(paragraph.lower())
    result = []
    for s in sentences:
        tmp = []
        word = ''
        i = 0
        while(i < len(s)):
            if s[i] not in split:
                word += s[i]
                i += 1
            elif s[i] in OTHER_PUNCTUATION:
                tmp.append(word)
                word = ''
                i += 2
            elif s[i] == ' ':
                tmp.append(word)
                word = ''
                i += 1
        tmp.append(word)
        result.append(tmp)
    return result
    
def build_semantic_descriptors_from_files(f_list):
    '''
    given a list of file names (strings) as input returns a dictionary 
    of the semantic descriptors of all the words in the files received 
    as input, with the files treated as a single text.

    Parameters
    ----------
    f_list : list

    Returns
    -------
    Dictionary
    
    >>> d = build_semantic_descriptors_from_files(['animal_farm.txt'])
    >>> d['animal']['must']
    3
    >>> d['evil'] ==  {'all': 1, 'the': 1, 'habits': 1, 'of': 1, 'man': 1, 'are': 1}
    True
    >>> d = build_semantic_descriptors_from_files(['animal_farm.txt', 'alice.txt'])
    >>> 'king' in d['clever']
    True
    >>> 'brothers' in d['clever']
    True
    >>> len(d['man'])
    21
    '''
    result = {}
    for f in f_list:
        file = open(f, "r", encoding="utf-8")
        content = file.read()
        words = get_word_breakdown(content)
        tmp = similarity_measures.get_all_semantic_descriptors(words)
        vectors_utils.merge_dicts_of_vectors(result, tmp)
    return result

if __name__ == '__main__':
    doctest.testmod()