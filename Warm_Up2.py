#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 22:46:09 2020

@author: stevenyuan
"""

import doctest

def flatten_list(input_ls):
    '''
    Write a function flatten_list which takes as input a two 
    dimensional list and returns a one dimensional list containing 
    all the elements of the sublists.

    Parameters
    ----------
    input_ls : 2D list

    Returns
    -------
    list

    >>> flatten_list([[1, 2], [3], ['a', 'b', 'c']])
    [1, 2, 3, 'a', 'b', 'c']
    >>> flatten_list([[]])
    []
    '''
    result = []
    for sub_ls in  input_ls:
        for ele in sub_ls:
            result.append(ele)
    return result
    
    
if __name__ == '__main__':
    doctest.testmod()