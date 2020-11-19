#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 21:44:27 2020

@author: stevenyuan
"""
import doctest
from similarity_measures import *
from file_processing import *
import matplotlib.pyplot as plt
import numpy as np

def most_sim_word(word, choices, descriptors, sim_fn):
    '''
    This function takes in a string word, a list of strings choices, 
    and a dictionary semantic_descriptors which is built according to 
    the requirements for get_all_semantic_descriptors, and returns the 
    element of choices which has the largest semantic similarity to word, 
    with the se- mantic similarity computed using the data in semantic_descriptors 
    and the similarity function similarity_fn. The similarity function is a 
    function which takes in two sparse vectors stored as dictionaries and 
    returns a float. An example of such a function is get_cos_sim. 
    If the semantic similarity between two words cannot be computed, 
    it is considered to be −1. In case of a tie between several elements 
    in choices, the one with the smallest index in choices should be returned 

    Parameters
    ----------
    word : String
    choices : list
    descriptors : dictionary
    sim_fn : function

    Returns
    -------
    String
    
    >>> choices = ['dog', 'cat', 'horse']
    >>> c = {'furry' : 3, 'grumpy' : 5, 'nimble' : 4}
    >>> f = {'furry' : 2, 'nimble' : 5}
    >>> d = {'furry' : 3, 'bark' : 5, 'loyal' : 8}
    >>> h = {'race' : 4, 'queen' : 2}
    >>> sem_descs = {'cat' : c, 'feline' : f, 'dog' : d, 'horse' : h}
    >>> most_sim_word('feline', choices, sem_descs, get_cos_sim)
    'cat'
    '''
    key = ''
    max_num = 0
    for choice in choices:
        if choice in descriptors and word in descriptors:
            tmp = sim_fn(descriptors[word], descriptors[choice])
        else:
            tmp = -1
        if tmp > max_num:
            max_num = tmp
            key = choice
    return key

def run_sim_test(filename, descriptors, sim_fn):
    '''
    This function takes three inputs: a string filename, a dictionary 
    semantic_descriptors, and a function similarity_fn. The string is 
    the name of a file in the same format as test.txt.
    The function returns the percentage (i.e., float between 0.0 and 100.0) 
    of questions on which most_sim_word guesses the answer correctly using 
    the semantic descriptors stored in semantic_descriptors, and the similarity 
    function similarity_fn.

    Parameters
    ----------
    filename : String
    descriptors : Dictionary
    sim_fn : function

    Returns
    -------
    float

    '''
    num_questions = 0
    correct = 0
    
    file = open(filename, "r", encoding="utf-8")
    line = file.readline()
    while(line != ''):
        num_questions += 1
        options = line.split()
        word = options[0]
        answer = options[1]
        choices = []
        choices.append(options[2])
        choices.append(options[3])
        guess = most_sim_word(word, choices, descriptors, sim_fn)
        if guess == answer:
            correct += 1
        line = file.readline()
    return correct / num_questions
        
def generate_bar_graph(list_fun, filename):
    '''
    given a list of similarity functions and a string filename 
    (which is the name of a file in the same format as test.txt) 
    generates a bar graph (using matplotlib) where the performance 
    of each function on the given file test is plotted.

    Parameters
    ----------
    list_fun : list
    filename : String

    Returns
    -------
    None.

    '''
    descriptors = build_semantic_descriptors_from_files(["pg7178.txt", "pg2600.txt"])
    performance = []
    for fun in list_fun:
        percentage = run_sim_test(filename, descriptors, fun)
        performance.append(percentage)
    x = np.arange(len(list_fun))
    y = np.array(performance)
    plt.bar(x, y)
    plt.title("Performance of each function")
    plt.show()

if __name__ == '__main__':
    doctest.testmod()
    generate_bar_graph([get_cos_sim], 'test.txt')