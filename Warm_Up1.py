#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 22:42:06 2020

@author: stevenyuan
"""
import doctest

def same_elements(input_ls):
    '''
    Write a function same_elements which takes as input a 
    two dimensional list and returns true if all the elements 
    in each sublist are the same, false otherwise.

    Parameters
    ----------
    input_ls : 2D list

    Returns
    -------
    Boolean

    >>> same_elements([[1, 1, 1], ['a', 'a'], [6]])
    True
    >>> same_elements([[1, 6, 1], [6, 6]])
    False
    '''
    for sub_ls in input_ls:
        tmp = sub_ls[0]
        for ele in sub_ls:
            if(ele != tmp):
                return False
    return True
    
    
if __name__ == '__main__':
    doctest.testmod()