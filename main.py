#!/bin/python3
from stats import num_of_words, num_of_char, pretty_num_of_char

def main():
    num_words = num_of_words(get_book_text("books/frankenstein.txt"))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    num_char = num_of_char(get_book_text("books/frankenstein.txt"))
#    print(f"{num_char}")

    print("--------- Character Count -------")
    pretty_num_char = pretty_num_of_char(get_book_text("books/frankenstein.txt"))
    for char in pretty_num_char:
        print(f'{char["char"]}: {char["num"]}')
    print("============= END ===============") 

def get_book_text(filepath):
    with open(filepath, encoding="utf8") as f:
        return f.read()

main()