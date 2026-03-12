from stats import get_num_words, get_letter_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file = f.read()
        return file


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    get_num_words(book_text)
    get_letter_dict(book_text)
    
main()