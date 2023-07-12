# from data_structures.hashtable import Hashtable

def first_repeated_word(string):
    words = string.lower().split()  # Convert string to lowercase and split into words
    word_count = {}

    for word in words:
        if word in word_count:
            return word  # Return the first repeated word
        else:
            word_count[word] = 1

    return None  # Return None if no repeated word is found
