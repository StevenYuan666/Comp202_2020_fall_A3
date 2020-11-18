#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 22:59:36 2020

@author: stevenyuan
"""

import doctest

def add_dicts(d1, d2):
    '''
    Write a function add_dicts which takes as input two dictionaries 
    mapping strings to integers. The function returns a dictionary 
    which is a result of merging the two input dictionary, that is if 
    a key is in both dictionaries then add the two values.

    Parameters
    ----------
    d1 : Dictionary
    d2 : Dictionary

    Returns
    -------
    Dictionary

     >>> d1 = {'a':5, 'b':2, 'd':-1}
    >>> d2 = {'a':7, 'b':1, 'c':5}
    >>> add_dicts(d1, d2) == {'a': 12, 'b': 3, 'c': 5, 'd': -1}
    True
    '''
    result = {}
    for key in list(d1):
        if key in list(d2):
            result[key] = d1[key] + d2[key]
        else:
            result[key] = d1[key]
            
    for key in list(d2):
        if(key) not in result:
            result[key] = d2[key]
    
    return result

if __name__ == '__main__':
    doctest.testmod()