from stats import get_num_words, get_letter_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file = f.read()
        return file


def main():
    print(get_num_words(get_book_text("./books/frankenstein.txt")))
    print(get_letter_dict(get_book_text("./books/frankenstein.txt")))
    
main()