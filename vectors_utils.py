#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 23:32:46 2020

@author: stevenyuan
"""

import doctest
import math

def add_vectors(v1, v2):
    '''
    given two dictionaries representing vectors, 
    it adds the second vector to the first one.
    This function is void, and it modifies only the first input dictionary.

    Parameters
    ----------
    v1 : Dictionary
    v2 : Dictionary

    Returns
    -------
    None.

    >>> v1 = {'a' : 1, 'b' : 3}
    >>> v2 = {'a' : 1, 'c' : 1}
    >>> add_vectors(v1, v2)
    >>> len(v1)
    3
    >>> v1['a']
    2
    >>> v1 == {'a' : 2, 'b' : 3, 'c' : 1}
    True
    >>> v2 == {'a' : 1, 'c' : 1}
    True
    '''
    for key in list(v1):
        if key in v2:
            v1[key] += v2[key]
    for key in list(v2):
        if key not in v1:
            v1[key] = v2[key]
            
def sub_vectors(v1, v2):
    '''
    given two dictionaries representing vectors, 
    it returns a dictionary which is the result of subtracting the 
    second vector from the first one. This function must not modify 
    any of the input dictionaries.

    Parameters
    ----------
    v1 : Dictionary
    v2 : Dictionary

    Returns
    -------
    Dictionary
    
    >>> d1 = {'a' : 3, 'b': 2}
    >>> d2 = {'a': 2, 'c': 1, 'b': 2}
    >>> d = sub_vectors(d1, d2)
    >>> d == {'a': 1, 'c' : -1}
    True
    >>> d1 == {'a' : 3, 'b': 2}
    True
    >>> d2 == {'a': 2, 'c': 1, 'b': 2}
    True
    '''
    result = {}
    
    for key in v1:
        if key in v2:
            if((v1[key] - v2[key]) != 0):
                result[key] = v1[key] - v2[key]
        else:
            result[key] = v1[key]
    for key in v2:
        if (key not in result) and (key not in v1):
            result[key] = 0 - v2[key]
    
    return result

def merge_dicts_of_vectors(d1, d2):
    '''
    given two dictionaries containing values which are 
    dictionaries represent- ing vectors, the function 
    modifies the first input by merging it with the second one. 
    This means that if both dictionaries contain the same key, 
    then in the merged dictionary that same key will map to the 
    sum of the two vectors. Note that this is a void function 
    and it modifies only the first input dictionary.

    Parameters
    ----------
    d1 : Dictionary
    d2 : Dictionary

    Returns
    -------
    None.
    
    >>> d1 = {'a' : {'apple': 2}, 'p' : {'pear': 1, 'plum': 3}}
    >>> d2 = {'p' : {'papaya' : 6}}
    >>> merge_dicts_of_vectors(d1, d2)
    >>> len(d1)
    2
    >>> len(d1['p'])
    3
    >>> d1['a'] == {'apple': 2}
    True
    >>> d1['p'] == {'pear': 1, 'plum': 3, 'papaya' : 6}
    True
    >>> d2 == {'p' : {'papaya' : 6}}
    True
    >>> merge_dicts_of_vectors(d2, d1)
    >>> d2['a']['apple']
    2
    >>> d2['p']['papaya']
    12
    '''

    for key in d2:
        if(key in d1):
            for k in d2[key]:
                if k in d1[key]:
                    d1[key][k] += d2[key][k]
                else:
                    d1[key][k] = d2[key][k]
        else:
            d1[key] = d2[key]
            
def get_dot_product(v1, v2):
    '''
    given two dictionaries representing vectors, 
    returns the dot product of the two vectors.

    Parameters
    ----------
    v1 : Dictionary
    v2 : Dictionary

    Returns
    -------
    int

    >>> v1 = {'a' : 3, 'b': 2}
    >>> v2 = {'a': 2, 'c': 1, 'b': 2}
    >>> get_dot_product(v1, v2)
    10
    >>> v3 = {'a' : 3, 'b': 2}
    >>> v4 = {'c': 1}
    >>> get_dot_product(v3, v4)
    0
    '''
    
    product = 0
    for key in v1:
        if(key in v2):
            product += v1[key] * v2[key]
    
    return product

def get_vector_norm(v):
    '''
    given a dictionary representing a vector, returns the norm of such vector.

    Parameters
    ----------
    v : Dictionary

    Returns
    -------
    float

    >>> v1 = {'a' : 3, 'b': 4}
    >>> get_vector_norm(v1)
    5.0
    >>> v2 = {'a': 2, 'c': 3, 'b': 2}
    >>> round(get_vector_norm(v2), 3)
    4.123
    '''

    product = get_dot_product(v, v)
    return math.sqrt(product)

def normalize_vector(v):
    '''
    given a dictionary representing a vector, 
    the function modifies the dictionary by 
    dividing each value by the norm of the vector. 
    Given a vector v = {v1, v2, . . . , vN } we can normalize 
    it by multiplying it by the inverse of its norm (i.e. 1/ ∥v∥). 
    Note that this function does not return any values.

    Parameters
    ----------
    v : Dictionary

    Returns
    -------
    None.

    >>> v1 = {'a' : 3, 'b': 4}
    >>> normalize_vector(v1)
    >>> v1['a']
    0.6
    >>> v1['b']
    0.8
    >>> v2 = {'a': 2, 'c': 3, 'b': 2}
    >>> normalize_vector(v2)
    >>> round(v2['c'], 3)
    0.728
    '''
    norm = get_vector_norm(v)
    if(norm == 0):
        return None
    for key in v:
        v[key] = v[key] / norm
        
if __name__ == '__main__':
    doctest.testmod()