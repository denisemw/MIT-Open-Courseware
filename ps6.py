# Problem Set 6: 6.00 Word Games 2
# Name: 
# Collaborators: 
# Time: 
#

import random
import string
import time

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
points_dict = {}
all_perms = []
rearranged_dict = {}

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters
    in the word, plus 50 points if all n letters are used on
    the first go.

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    freq = get_frequency_dict(word)
    score = 0
    for i in freq:
        score += SCRABBLE_LETTER_VALUES[i]*freq[i]
    if len(word)==n:
        score+=50
    return score

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print letter,              # print all on the same line
    print                              # print an empty line

def convert_hand_to_string(hand):
    s = ''
    for letter in hand.keys():
        for j in range(hand[letter]):
            s += letter
    return s

#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = n / 3
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not mutate hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ...
    word_freqs = get_frequency_dict(word)
    hand_freqs = get_frequency_dict(hand)
    score = 0
    new_hand = {}
    for w in hand:
        if w in word_freqs:
            if hand[w]!=word_freqs[w]:
                new_hand[w] = hand[w] - word_freqs[w]
        else:
            new_hand[w] = hand[w]
    return new_hand
        
        

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    for w in word:
        if w not in hand:
            return False
        if word.count(w) > hand[w]:
            return False
    try:
        points_dict[word]
    except:
        return False
    return True


    
def get_hand_size(hand):
    l = []
    for i in hand.values():
        if not type(i) == list:
            l += [i]
        else:
            l += i
    return len(l)


def play_hand(hand, word_list, rtime, is_computer):
    """
    Allows the user to play the given hand, as follows:
    * The hand is displayed.    
    * The user may input a word.
    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word and the total
      score so far are displayed, the remaining letters in the hand 
      are displayed, and the user is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.
    * The final score is displayed.
      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """
    score = 0
    remaining_time = rtime
    while True:
        display_hand(hand)
        start_time = time.time()
        if is_computer:
            word = pick_best_word_faster(hand, points_dict)
            print 'word = ', word
        else:
            word = raw_input("Enter a valid word (or '.' to end turn): ")
        end_time = time.time()
        total_time = end_time - start_time
        remaining_time = remaining_time - total_time
        print("It took %.2f to provide an answer" % total_time)
        
        if word==".":
            break

        # if time is over the time limit, then the game is over
        elif remaining_time <= 0:
            print("Total time exceeds %.2f. Total score is %.2f" % (rtime, score))
            break

        # if within time limmit, check if valid word, and if so, get score
        elif is_valid_word(word,hand):
            word_score = get_word_score(word, HAND_SIZE)
            score += word_score
            hand = update_hand(hand, word)

            # print current word score, total score, and remaining time
            print ("Score for %s is %.2f" % (word, word_score))
            print ("Total score is " + str(score))
            print("There are %.2f seconds remaining" % remaining_time)

        # if it is not a valid word, instruct user to try again
        else:
            print ("Not a valid word. Please try again.")

        if get_hand_size(hand)==0:
            break
            
    print ("End of game! \nFinal score: %d" % score)



def get_words_to_points(word_list):
    """
    Return a dict that maps every word in word_list to its point value.
    """
    for word in word_list:
        points_dict[word] = get_word_score(word, HAND_SIZE)


# complexity = O(n), where n = length of points dict
# O(j), where j = length of hand
def pick_best_word(hand, points_dict):
    """ Return the highest scoring word from points_dict that can be made with the
    given hand. Return '.' if no words can be made with the given hand. """

    possible_words = {}
    for key in points_dict:
        if is_valid_word(key, hand):
            possible_words[key] = get_word_score(key, HAND_SIZE)
    
    best_word = '.'
    max_score = 0    
    for word in possible_words:
        if possible_words[word] > max_score:
            best_word = word
            max_score = possible_words[word]
            
    return best_word
        

def get_time_limit(points_dict, k):
    """
    Return the time limit for the computer player as a function of the
    multiplier k.
    points_dict should be the same dictionary that is created by
    get_words_to_points.
    """
    
    start_time = time.time()
    # Do some computation. The only purpose of the computation is so we can
    # figure out how long your computer takes to perform a known task.
    for word in points_dict:
        get_frequency_dict(word)
        get_word_score(word, HAND_SIZE)
    end_time = time.time()
    return (end_time - start_time) * k

def get_rearranged_dict():
    for word in points_dict:
        rearranged_word = ''.join(sorted(word))
        rearranged_dict[rearranged_word] = word
    


# O(n^2), where n = length of hand
def pick_best_word_faster(hand, points_dict):
    best_word = '.'
    max_word = 0
    letters = convert_hand_to_string(hand)
    letters = ''.join(sorted(letters))
    subs = get_subsets(letters, subs)
    for word in subs:
        if word in rearranged_dict:
            rearranged_word = rearranged_dict[word]
            if points_dict[rearranged_word] > max_word:
                max_word = points_dict[rearranged_word]
                best_word = rearranged_word
    return best_word

    

def get_subsets(word, subset_list):
    for i in range(len(word)):
        subset_helper('', i, word, subset_list)
    return subset_list


def subset_helper(substr, index, word, subset_list):
    s = word[index]
    s = substr + s
    subset_list.append(s)
    for i in range(index+1, len(word)):
        subset_helper(s,i, word, subset_list)
    return subset_list

#
# Problem #5: Playing a game
# Make sure you understand how this code works!
# 
def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.
    * Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.
    * If the user inputs 'r', let the user play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.
    """
    hand = deal_hand(HAND_SIZE) # random init
    get_words_to_points(word_list)
    get_rearranged_dict()

    while True:
        cmp_player = False        
        while True:
            player_type = raw_input("Computer player? y/n: ")
            if player_type[0].lower() == 'y':
                cmp_player = True
                break
            elif player_type[0].lower() == 'n':
                cmp_player = False
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'")
                
        cmd = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')

        if cmd=='e':
            break
        
        while True:
            if cmp_player:
                rtime = get_time_limit(points_dict, 5)
                break
            try:
                rtime = float(raw_input('Enter time limit, in seconds, for players: '))
                break
            except:
                print("Invalid input. Please enter a number.")

        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand.copy(), word_list, rtime, cmp_player)
            print
        elif cmd == 'r':
            play_hand(hand.copy(), word_list, rtime, cmp_player)
            print
        else:
            print "Invalid command."

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    
    play_game(word_list)
