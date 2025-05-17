#!/bin/python3
from stats import num_of_words, num_of_char, pretty_num_of_char

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = num_of_words(text)
    pretty_num_char = pretty_num_of_char(text)
    print_report(book_path, num_words, pretty_num_char)

def get_book_text(filepath):
    with open(filepath, encoding="utf8") as f:
        return f.read()

def print_report(book_path, num_words, pretty_num_char):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in pretty_num_char:
        print(f'{char["char"]}: {char["num"]}')
    print("============= END ===============") 

main()