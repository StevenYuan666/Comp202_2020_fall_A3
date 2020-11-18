#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 23:07:11 2020

@author: stevenyuan
"""

import doctest

def reverse_dict(dic):
    '''
    Create a function reverse_dict which takes as input a dictionary 
    d and returns a dictionary where the values in d are now keys mapping 
    to a list containing all the keys in d which mapped to them.

    Parameters
    ----------
    dic : Dictionary

    Returns
    -------
    Dictionary

    >>> a = reverse_dict({'a': 3, 'b': 2, 'c': 3, 'd': 5, 'e': 2, 'f': 3})
    >>> a == {3 : ['a', 'c', 'f'], 2 : ['b', 'e'], 5 : ['d']}
    True
    '''
    new_keys = []
    result = {}
    
    for key in dic:
        if(dic[key] not in new_keys):
            new_keys.append(dic[key])
            
    for k in new_keys:
        tmp = []
        for key in dic:
            if(dic[key] == k):
                tmp.append(key)
        result[k] = tmp
    
    return result
    
if __name__ == '__main__':
    doctest.testmod()