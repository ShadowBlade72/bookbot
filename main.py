#!/bin/python3

def get_book_text(filepath):
    with open(filepath, encoding="utf8") as f:
        return f.read()

def num_of_words(file_contents):
    word = file_contents.split()
    return len(word)

def main():
    num_words = num_of_words(get_book_text("books/frankenstein.txt"))
    print(f"{num_words} words found in the document")

main()
