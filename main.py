#!/bin/python3
from stats import num_of_words, pretty_num_of_char
import sys, os

def main():
    sanity_check()
    book_path = sys.argv[1]
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

def sanity_check():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    if not os.path.isfile(sys.argv[1]):
        print("Error: File does not exist or is not readable")
        sys.exit(1)

main()