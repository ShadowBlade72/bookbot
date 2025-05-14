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

def pretty_num_of_char(file_contents):
    counts = num_of_char(file_contents)
    result = sorted([{"char": char, "num": num} for char, num in counts.items() if char.isalpha()], key=lambda dict: dict["num"], reverse=True)
#    result = []
#    for char, num in counts.items():
#        result.append({"char": char, "num": num})
#    result.sort(key=lambda dict: dict["num"], reverse=True)
    return result