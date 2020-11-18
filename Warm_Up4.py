#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 22:54:20 2020

@author: stevenyuan
"""

import doctest

def get_most_valuable_key(input_dict):
    '''
    Write a function get_most_valuable_key which takes as input 
    a dictionary mapping strings to integers. The function returns 
    the key which is mapped to the largest value.

    Parameters
    ----------
    input_dict : Dictionary

    Returns
    -------
    int

    >>> get_most_valuable_key({'a' : 3, 'b': 6, 'g': 0, 'q': 9})
    'q'
    '''
    result = list(input_dict)[0]
    for key in list(input_dict):
        if input_dict[key] > input_dict[result]:
            result = key
            
    return result
    
    
    
if __name__ == '__main__':
    doctest.testmod()