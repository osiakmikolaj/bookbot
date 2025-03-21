from stats import get_num_words

def get_book_text(path):
    with open(path, 'r') as f:
        file_contents = f.read()
        return file_contents

def main():
    print(get_num_words(get_book_text('./books/frankenstein.txt')))

main()