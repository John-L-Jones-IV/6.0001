#!/usr/bin/env python3
# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : John L. Jones IV <John-L-Jones-IV>
# Collaborators : Compared solutions with: <tuthang102>, <iamwhill>, <jeremiahflaga>, & <razikhshaik>
#
# https://github.com/tuthang102/MIT-6.0001-Intro-to-CS/blob/master/ps3/ps3.py
# https://github.com/iamwhil/6.0001/blob/master/ps3/ps3.py
# https://github.com/jeremiahflaga/mit-ocw-6.0001/blob/master/ps3/ps3.py
# https://github.com/razikhshaik/MIT-6.0001-Introduction-to-computer-programming/blob/master/Assignments/Problem%20Set%203/ps3.py
#
# Time spent    : Started - 25AUG2019 10:00
# Completed Problem #1 - 25AUG2019 21:51
# Completed Problem #3 - 26AUG2019 22:34

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*':0
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
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
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

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

    The score for a word is the product of two components:

    The first component is the sum of the points for letters in the word.
    The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """

    letter_score = 0
    for char in word.lower():
        letter_score += SCRABBLE_LETTER_VALUES.get(char,0)

    word_score = max( 7*len(word) - 3*(n-len(word)), 1 )

    return letter_score*word_score



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
            print(letter, end = " ") # print all on the same line

    print() # print an empty line



#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n, with_wildcard = True):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    Wild card mod: always give one wildcard in each hand, replace one vowel with the '*' wildcard

    n: int >= 0
    returns: dictionary (string -> int)
    """

    hand={}
    num_vowels = int(math.ceil(n / 3))

    if with_wildcard:
        for i in range(num_vowels - 1):
            x = random.choice(VOWELS)
            hand[x] = hand.get(x, 0) + 1

        hand['*'] = hand.get('*',0) + 1

    else:
        for i in range(num_vowels):
            x = random.choice(VOWELS)
            hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    return hand



#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """

    cpy_hand = hand.copy()
    for c in word.lower():
        cpy_hand[c] = cpy_hand.get(c,0) - 1
        if cpy_hand.get(c,0) <= 0:
            del cpy_hand[c]

    return cpy_hand

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: bool
    """

    word = word.lower()
    cpy_hand = hand.copy()

    # if word is not in hand return false
    for char in word:
        if cpy_hand.get(char,0) > 0:
            cpy_hand[char] = cpy_hand.get(char,0) - 1
        elif cpy_hand.get(char,0) <= 0:
            return False

    if word in word_list:
        return True

    # if word is in a '*' variant of word list return true
    for w in word_list:
        if word in replace_vowels(w):
            return True

    # else word must not be in word list, return false
    return False



def find_vowels(word):
    """
    Find index of vowels all vowels in word.

    word : string
    return :  vowel_index, list of integer vowel indices in word 
    """

    word = word.lower()
    vowel_index = []
    i = 0
    for char in word:
        if char in VOWELS:
            vowel_index.append(i)
        i += 1

    return vowel_index



def replace_vowels(word):
    """
    Replace each vowels in word with '*' character and add modified word to list.
    Example: replace_vowels(ABACUS) returns [*bacus, ab*cus, abac*s]

    NOTE: converts all inputs to lowercase!

    word: string
    return: list of all versions of string with vowel characters replaced with '*'
    """

    word = word.lower()
    vowel_index = find_vowels(word)
    words = []
    for i in vowel_index:
        words.append(word[:i]+'*'+word[i+1:])

    return words 



#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of cards) in the current hand.

    hand: dictionary (string-> int)
    returns: sum of all cards in hand
    """

    return sum(hand.values())



def calculate_num_vowels(hand):
    """
    Returns the number of of VOWELS in hand including '*'.

    hand : dict (str -> int)
    return: int, sum of vowel cards in hand
    """

    num_vowels = 0
    for k in hand.keys():
        if k in VOWELS or k == '*':
            num_vowels += hand.get(k,0)

    return num_vowels



def calculate_num_consonant(hand):
    """
    Returns the number of of CONSONANTS in hand.

    hand : dict (str -> int)
    return int
    """

    num_consonants = 0
    for k in hand.keys():
        if (k in CONSONANTS):
            num_vowels += hand.get(k,0)

    return num_vowels



# helper function
def play_hand(hand, word_list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.

    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
    from the hand.

    * An invalid word is rejected, and a message is displayed asking
    the user to choose another word.

    * After every valid word: the score for that word is displayed,
    the remaining letters in the hand are displayed, and the user
    is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
    The user can also finish playing the hand by inputing two 
    exclamation points (the string '!!') instead of a word.

    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: the total score for the hand
    """

    # Keep track of the total score
    score = 0

    # As long as there are still letters left in the hand:
    while calculate_handlen(hand) > 0:  

        # Display the hand
        print('Current Hand: ', end='')
        display_hand(hand)

        # Ask user for input
        word = input('Enter word, or "!!" to indicate that you are done: ')

        # If the input is two exclamation points:
        if word == '!!':
            # End the game (break out of the loop)
            break

        # Otherwise (the input is not two exclamation points):
        else:
            # If the word is valid:
            if is_valid_word(word, hand, word_list):

                # Tell the user how many points the word earned,
                word_score = get_word_score(word,calculate_handlen(hand))
                print('"'+str(word)+'" earned', word_score, 'points. ', end='')
                # and the updated total score
                score += word_score
                print('Total:', score, 'points \n')
            
            # Otherwise (the word is not valid):
            else:
                # Reject invalid word
                print('That is not a valid word. Please choose another word.\n')

            # update the user's hand by removing the letters of their inputted word
            hand = update_hand(hand,word)  



    # Game is over (user entered '!!' or ran out of letters),
    if calculate_handlen(hand) == 0:
        print('Ran out of letters ')

    print('Total score for this hand: ', score)

    # Return the total score as result of function
    return score



#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """

    cpy_hand = hand.copy()

    # make a list of all letters not currently in hand
    avalible_letters = '' 
    for c in string.ascii_lowercase:
        if not is_in_hand(c,cpy_hand):
            avalible_letters += c 

    # replace all instances of letter with these avalible_letter 
    if is_in_hand(letter,hand):
        for i in range(hand.get(letter,0)):
            cpy_hand[letter] -= 1
            new_card = random.choice(avalible_letters)
            cpy_hand[new_card] = cpy_hand.get(new_card,0) + 1 
            
    # remove keys with value 0 or less
    clean_hand = cpy_hand.copy()
    for k in cpy_hand.keys():
        if clean_hand.get(k,0) <= 0:
            del clean_hand[k]
        
    return cpy_hand



def is_in_hand(letter, hand):
    """
    if key is in hand and has a value greater than zero return True
    else return False

    letter: string
    hand: dictionary (string-> int)
    return: True if letter is in hand, otherwise return False
    """
    if letter not in hand:
        return False

    if hand.get(letter,0) < 1:
        return False

    return True



def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

    * Note: if you replay a hand, you do not get the option to substitute
            a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    return : the total score for the series of hands
    """

    # Ask the user to input a total number of hands
    num_of_hand = int(input('Enter total number of hands: '))

    # Initialize the score for total accumulation
    series_score = 0

    # Allow the player to replay hands during the game
    hand_replays = 1
    letter_subs = 1

    for i in range(num_of_hand): # for each hand
        hand = deal_hand(HAND_SIZE)
        print('Current Hand:', end=' ')
        display_hand(hand)

        if letter_subs > 0:
            s_sub_letter = str(input('Would you like to substitue a letter? ')).lower()
            if s_sub_letter == 'y' or s_sub_letter == 'yes':
                letter_subs -= 1
                replaced_letter = str(input('Which letter would you like to replace: ')).lower()
                print() 
                hand = substitute_hand(hand, replaced_letter)
                
            else:
                print() # print new line

        saved_hand = hand.copy()
        hand_score = play_hand(hand, word_list)
        print('----------')

        if hand_replays > 0:
            s_replay = str(input('Would you like to replay the hand? ')).lower()
            if s_replay == 'y' or s_replay =='yes':
                hand_replays -= 1
                hand = saved_hand.copy()
#                print('Current Hand:', end=' ') 
#                display_hand(hand)
                hand_score = play_hand(hand, word_list)
                print('----------')
                

        series_score += hand_score

    print('Total score over all hands:', series_score)    
    return series_score
#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

