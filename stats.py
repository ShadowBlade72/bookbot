#!/bin/python3

def num_of_words(file_contents):
    word = file_contents.split()
    return len(word)

def num_of_char(file_contents):
    dict = {}
    for c in list(file_contents.lower()):
        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1
    return dict