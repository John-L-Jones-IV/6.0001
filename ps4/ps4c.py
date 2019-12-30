#!/usr/bin/env python3
# Problem Set 4C
# Name: <John-L-Jones-IV>
# Collaborators:
# Time Spent: x:xx

import string
import random
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words.copy()
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        from string import punctuation, whitespace, digits

        const_chars = CONSONANTS_LOWER + CONSONANTS_UPPER + punctuation + whitespace + digits
        d = {char: char for char in const_chars}
        for i in range(5):
            d[VOWELS_LOWER[i]] = permutation[i]
            d[VOWELS_UPPER[i]] = permutation[i].upper()

        return d


    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        message_transpose  = ''
        for char in self.message_text:
            message_transpose += transpose_dict[char]

        return message_transpose
        
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self,text)


    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        from string import punctuation, whitespace, digits

        max_valid_words = 0
        best_message = self.message_text
        
        fixed_chars = CONSONANTS_UPPER + CONSONANTS_LOWER + punctuation + whitespace + digits
        d = {char:char for char in fixed_chars}
 
        for perm in get_permutations(VOWELS_LOWER):
            valid_word_cnt = 0

            for i in range(5):
                d[VOWELS_LOWER[i]] = perm[i]
                d[VOWELS_UPPER[i]] = perm[i].upper()

            decrypt_message = ''
            for char in self.message_text:
                decrypt_message += d[char]

            for word in decrypt_message.split():
                if is_word(self.valid_words, word):
                    valid_word_cnt += 1

            if valid_word_cnt > max_valid_words:
                max_valid_words = valid_word_cnt
                best_message = decrypt_message 

        return best_message



if __name__ == '__main__':
    # Example test case
    message = SubMessage("Hello World!") 
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:  ", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())

    # TEST CASE 1
    # FIXME does not encrpyt as expected...
    message = SubMessage("I'm a ramblin' wreck from Georgia Tech and a helleva engineer!")
    permutation = "euoai"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "O'm e remblon' wruck frem Guargoe Tuch end e hulluve ungonuur!")
    print("Actual encryption:  ", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())

    # TEST CASE 2
    message = SubMessage("Hey Jude, don't make it bad Take a sad song and make it better Remember to let her into your heart Then you can start to make it better")
    permutation = "eioua"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hiy Jadi, dun't meki ot bed Teki e sed sung end meki ot bittir Rimimbir tu lit hir ontu yuar hiert Thin yua cen stert tu meki ot bittir")
    print("Actual encryption:  ", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())

    # TEST CASE 3
    message = SubMessage("Saying that your home is powered by a wireless Nuclear fussion reactor that is 93 Million miles away sounds way cooler than just saying you have solar panels on your roof.")
    permutation = 'iaeuo'
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Siyeng thit yuor huma es puwarad by i weralass Noclair fosseun raictur thit es 93 Melleun melas iwiy suonds wiy cuular thin jost siyeng yuo hiva sulir pinals un \
yuor ruuf.")
    print("Actual encryption:  ", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
