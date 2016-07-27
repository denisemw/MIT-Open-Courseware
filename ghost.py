# Problem Set 5: Ghost
# Name: 
# Collaborators: 
# Time: 
#

import random
from string import *

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

#
# Problem #3: Test word validity
#
def is_valid_word(word, word_list):
    """
    Returns True if word is in the word_list.
    Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    word_list: list of lowercase strings
    """
    if len(word) <= 3:
        return False
    for w in word_list:
        if word.lower()==w.lower():
            return True
    return False


def is_valid_fragment(fragment,word_list):
    end = len(fragment)
    for word in word_list:
        if word[0:end].lower()==fragment.lower():
            return True
    return False
    
# (end of helper code)
# -----------------------------------

def play_game(wordlist):

    word = ""
    cnt=2
    print("Welcome to Ghost!\nPlayer 1 goes first")
    print("Current word fragment: ''")
    letter = raw_input("Player 1 says letter: ")
    word += letter.upper()
    
    while True:
        print("\nCurrent word fragment: " + word)
        if is_valid_word(word,wordlist):
            print("Player " + str(p) + " loses because " + word + " is a word!")
            break
        if not is_valid_fragment(word,wordlist):
            print("Player " + str(p) + " loses because no word starts with " + word)
            break

        if cnt%2==0:
            p = 2
        else:
            p = 1

        print("Player %d's turn." % p)
        while True:
            letter = raw_input("Player %d says letter: " % p)
            if letter in string.ascii_letters:
                break
            else:
                print("Input not a letter. Please try again.")
        letter = letter.upper()
        word += letter
        cnt+=1

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordlist = load_words()
    play_game(wordlist)


