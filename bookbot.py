#!/usr/bin/env python3
import sys
from stats import *

chars = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
    'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', 
    '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', 
    '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', 
    '[', ']', '{', '}', ';', ':', '\'', '\"', ',', '.', 
    '<', '>', '/', '?', '\\', '|', '`', '~', ' '
]

def get_book_text(path):
    try:
        f = open(path)
    except FileNotFoundError:
        print("-------- File not found! --------")
        sys.exit(1)
    else:
        print(f"Analyzing book found at {path}")
        with open(path, 'r') as f:
            file_contents = f.read()
            return file_contents

def main():
    if len(sys.argv) > 1:
        text = get_book_text(sys.argv[1])
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(get_num_words(text))
    print(char_count(text, chars))
    print("============= END ===============")

main()