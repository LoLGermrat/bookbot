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

"""
This is current dictionary: {letter:count}

this is what I want to change sturcture of dictionary to {char:"letter", count:0}
"""

"""
Create a function that accepts a dictionary, sets it to a list of individual dictionaries, then in that list sorts via key:value retrurn that in a report 
where it shows the letter most counted is on top and least is at the bottom
"""
def book_report(book_dict):
    lst_dict = []
    for key , value in book_dict.items():
        temp_dict= {"char" : key, "count" : value}
        if key.isalpha():
            lst_dict.append(temp_dict)

    test_lst = sorted(lst_dict, reverse=True, key=sort_on)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(main())} words found in the document")
    print()
    for items in test_lst:
        print(f"The '{items['char']}' character was found {items['count']} times")
    print("--- End report ---")

    return
    

        

def sort_on(dict):
    return dict["count"]

book_report(count_char(main()))
