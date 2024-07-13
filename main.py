def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def count_words(book):
    words = len(book.split())
    return words

def count_char(this_book):
    letter_dict = {}
    # want to lower case the string as we want to count individual characters and since we are using a dict we dont want to have capital letters 
    lower_char =  this_book.lower()
    for i in lower_char:
        if i in letter_dict:
            letter_dict[i] += 1
        else:
            letter_dict.setdefault(i, 1)
    
    return letter_dict


#print(count_words(main()))

count_char(main())

