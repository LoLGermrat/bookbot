def get_num_words(text):
    words = len(text.split())
    return f"Found {words} total words"

def get_letter_dict(text):
    letter_dict = {}
    formatted = text.lower()
    for l in formatted:
        if l not in letter_dict:
            letter_dict[l] = 0
        letter_dict[l] += 1
    
    for char , count in letter_dict.items():
       print(f"{char}: {count}")
    
    return letter_dict