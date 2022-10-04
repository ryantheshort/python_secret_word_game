import wordlist

# Take a random word from the word list.
def get_word(): 
    word = wordlist.get_random_word()
    return word.upper()
