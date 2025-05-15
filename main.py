#!/bin/python3
from stats import num_of_words
from stats import num_of_char
from stats import pretty_num_of_char

def sort_on(dict):
    return dict["num"]

def get_book_text(filepath):
    with open(filepath, encoding="utf8") as f:
        return f.read()

def main():
    num_words = num_of_words(get_book_text("books/frankenstein.txt"))
    print(f"{num_words} words found in the document")

    num_char = num_of_char(get_book_text("books/frankenstein.txt"))
    print(f"{num_char}")

    pretty_num_char = pretty_num_of_char(get_book_text("books/frankenstein.txt"))
    for char in pretty_num_char:
#        if char["char"].isalpha():
#        print(f"{char}")
        print(f'{char["char"]}: {char["num"]}')
#        pass

main()