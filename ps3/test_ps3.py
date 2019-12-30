#!/usr/bin/env python3
from ps3 import *

#
# Test code
#

def test_get_word_score():
    """
    Unit test for get_word_score
    """
    failure=False
    # dictionary of words and scores
    words = {("", 7):0, ("it", 7):2, ("was", 7):54, ("weed", 6):176,
             ("scored", 7):351, ("WaYbILl", 7):735, ("Outgnaw", 7):539,
             ("fork", 7):209, ("FORK", 4):308}
    for (word, n) in words.keys():
        score = get_word_score(word, n)
        if score != words[(word, n)]:
            print("FAILURE: test_get_word_score()")
            print("\tExpected", words[(word, n)], "points but got '" + \
                  str(score) + "' for word '" + word + "', n=" + str(n))
            failure=True
    if not failure:
        print("SUCCESS: test_get_word_score()")

# end of test_get_word_score


def test_update_hand():
    """
    Unit test for update_hand
    """
    # test 1
    handOrig = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
    handCopy = handOrig.copy()
    word = "quail"

    hand2 = update_hand(handCopy, word)
    expected_hand1 = {'l':1, 'm':1}
    expected_hand2 = {'a':0, 'q':0, 'l':1, 'm':1, 'u':0, 'i':0}
    if hand2 != expected_hand1 and hand2 != expected_hand2:
        print("FAILURE: test_update_hand('"+ word +"', " + str(handOrig) + ")")
        print("\tReturned: ", hand2, "\n\t-- but expected:", expected_hand1, "or", expected_hand2)

        return # exit function
        
    if handCopy != handOrig:
        print("FAILURE: test_update_hand('"+ word +"', " + str(handOrig) + ")")
        print("\tOriginal hand was", handOrig)
        print("\tbut implementation of update_hand mutated the original hand!")
        print("\tNow the hand looks like this:", handCopy)
        
        return # exit function
        
    # test 2
    handOrig = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    handCopy = handOrig.copy()
    word = "Evil"

    hand2 = update_hand(handCopy, word)
    expected_hand1 = {'v':1, 'n':1, 'l':1}
    expected_hand2 = {'e':0, 'v':1, 'n':1, 'i':0, 'l':1}
    if hand2 != expected_hand1 and hand2 != expected_hand2:
        print("FAILURE: test_update_hand('"+ word +"', " + str(handOrig) + ")")        
        print("\tReturned: ", hand2, "\n\t-- but expected:", expected_hand1, "or", expected_hand2)

        return # exit function

    if handCopy != handOrig:
        print("FAILURE: test_update_hand('"+ word +"', " + str(handOrig) + ")")
        print("\tOriginal hand was", handOrig)
        print("\tbut implementation of update_hand mutated the original hand!")
        print("\tNow the hand looks like this:", handCopy)
        
        return # exit function

    # test 3
    handOrig = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    handCopy = handOrig.copy()
    word = "HELLO"

    hand2 = update_hand(handCopy, word)
    expected_hand1 = {}
    expected_hand2 = {'h': 0, 'e': 0, 'l': 0, 'o': 0}
    if hand2 != expected_hand1 and hand2 != expected_hand2:
        print("FAILURE: test_update_hand('"+ word +"', " + str(handOrig) + ")")                
        print("\tReturned: ", hand2, "\n\t-- but expected:", expected_hand1, "or", expected_hand2)
        
        return # exit function

    if handCopy != handOrig:
        print("FAILURE: test_update_hand('"+ word +"', " + str(handOrig) + ")")
        print("\tOriginal hand was", handOrig)
        print("\tbut implementation of update_hand mutated the original hand!")
        print("\tNow the hand looks like this:", handCopy)
        
        return # exit function

    print("SUCCESS: test_update_hand()")

# end of test_update_hand

def test_is_valid_word(word_list):
    """
    Unit test for is_valid_word
    """
    failure=False

    # test 1
    word = "hello"
    handOrig = get_frequency_dict(word)
    handCopy = handOrig.copy()

    if not is_valid_word(word, handCopy, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected True, but got False for word: '" + word + "' and hand:", handOrig)

        failure = True

    # Test a second time to see if word_list or hand has been modified
    if not is_valid_word(word, handCopy, word_list):
        print("FAILURE: test_is_valid_word()")

        if handCopy != handOrig:
            print("\tTesting word", word, "for a second time - be sure you're not modifying hand.")
            print("\tAt this point, hand ought to be", handOrig, "but it is", handCopy)

        else:
            print("\tTesting word", word, "for a second time - have you modified word_list?")
            wordInWL = word in word_list
            print("The word", word, "should be in word_list - is it?", wordInWL)

        print("\tExpected True, but got False for word: '" + word + "' and hand:", handCopy)

        failure = True


    # test 2
    hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u':1}
    word = "Rapture"

    if  is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)

        failure = True        

    # test 3
    hand = {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
    word = "honey"

    if  not is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected True, but got False for word: '"+ word +"' and hand:", hand)

        failure = True                        

    # test 4
    hand = {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u':2}
    word = "honey"

    if  is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)
        
        failure = True

    # test 5
    hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    word = "EVIL"
    
    if  not is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected True, but got False for word: '" + word + "' and hand:", hand)
        
        failure = True
        
    # test 6
    word = "Even"

    if  is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)
        print("\t(If this is the only failure, make sure is_valid_word() isn't mutating its inputs)")        
        
        failure = True        

    if not failure:
        print("SUCCESS: test_is_valid_word()")

# end of test_is_valid_word

def test_wildcard(word_list):
    """
    Unit test for is_valid_word
    """
    failure=False

    # test 1
    hand = {'a': 1, 'r': 1, 'e': 1, 'j': 2, 'm': 1, '*': 1}
    word = "e*m"

    if is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word() with wildcards")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)

        failure = True

    # test 2
    hand = {'n': 1, 'h': 1, '*': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
    word = "honey"

    if is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word() with wildcards")
        print("\tExpected False, but got True for word: '"+ word +"' and hand:", hand)

        failure = True

    # test 3
    hand = {'n': 1, 'h': 1, '*': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
    word = "h*ney"

    if not is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word() with wildcards")
        print("\tExpected True, but got False for word: '"+ word +"' and hand:", hand)

        failure = True

    # test 4
    hand = {'c': 1, 'o': 1, '*': 1, 'w': 1, 's':1, 'z':1, 'y': 2}
    word = "c*wz"

    if is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word() with wildcards")
        print("\tExpected False, but got True for word: '"+ word +"' and hand:", hand)

        failure = True    

    # dictionary of words and scores WITH wildcards
    words = {("h*ney", 7):290, ("c*ws", 6):176, ("wa*ls", 7):203}
    for (word, n) in words.keys():
        score = get_word_score(word, n)
        if score != words[(word, n)]:
            print("FAILURE: test_get_word_score() with wildcards")
            print("\tExpected", words[(word, n)], "points but got '" + \
                  str(score) + "' for word '" + word + "', n=" + str(n))
            failure=True      

    if not failure:
        print("SUCCESS: test_wildcard()")


def test_find_vowels():
    failure = False
    # test 1
    word = 'abc'
    index = find_vowels(word)
    expected = [0]
    if index != expected:
        print("FAILURE: test_find_vowels()\nExpected", expected, "but got", index)
        failue = True
    
    # test 2
    word = 'zebra'
    index = find_vowels(word)
    expected = [1,4]
    if index != expected:
        print("FAILURE: test_find_vowels()\nExpected", expected, "but got", index)
        failue = True
 

    # test 3
    word = 'reddit'
    index = find_vowels(word)
    expected = [1,4]
    if index != expected:
        print("FAILURE: test_find_vowels()\nExpected", expected, "but got", index)
        failue = True

    # test 4
    word = 'aeioyu'
    index = find_vowels(word)
    expected = [0,1,2,3,5]
    if index != expected:
        print("FAILURE: test_find_vowels()\nExpected", expected, "but got", index)
        failue = True

    # test 5
    word = 'bzrtv'
    index = find_vowels(word)
    expected = []
    if index != expected:
        print("FAILURE: test_find_vowels()\nExpected", expected, "but got", index)
        failue = True

    if not failure:
        print('SUCCESS: test_find_vowels()')

def test_replace_vowels():
    failure = False

    # test 1
    word = 'apple'
    words = replace_vowels(word)
    expected = ['*pple', 'appl*']
    if words != expected:
        print("FAILURE: test_replace_vowels()\nExpected", expected, "but got", words)
        failue = True

    # test 2
    word = 'reddit'
    words = replace_vowels(word)
    expected = ['r*ddit', 'redd*t']
    if words != expected:
        print("FAILURE: test_replace_vowels()\nExpected", expected, "but got", words)
        failue = True

    # test 3
    word = 'foo'
    words = replace_vowels(word)
    expected = ['f*o', 'fo*']
    if words != expected:
        print("FAILURE: test_replace_vowels()\nExpected", expected, "but got", words)
        failue = True

    # test 4 
    word = 'bar'
    words = replace_vowels(word)
    expected = ['b*r']
    if words != expected:
        print("FAILURE: test_replace_vowels()\nExpected", expected, "but got", words)
        failue = True

    # test 5 
    word = 'baz'
    words = replace_vowels(word)
    expected = ['b*z']
    if words != expected:
        print("FAILURE: test_replace_vowels()\nExpected", expected, "but got", words)
        failue = True

    if not failure:
        print('SUCCESS: test_replace_vowels()')

def test_calculate_handlen():
    failure = False
    
    # test 1
    hand = {'a':1, 'p':2, 'l':1, 'e':1, 'f':1 , 'r':1, 'x':0 ,'y':0}
    N = calculate_handlen(hand)
    expected = 1+2+1+1+1+1
    if N != expected:
        print("FAILURE: test_calculate_handlen()\nExpected", expected, "but got", N)
        failue = True

    # test 2 
    hand = {'a':61, 'p':2, 'l':1, 'e':1, 'f':1 , 'r':1, 'x':0 ,'y':0}
    N = calculate_handlen(hand)
    expected = 61+2+1+1+1+1
    if N != expected:
        print("FAILURE: test_calculate_handlen()\nExpected", expected, "but got", N)
        failue = True

    # test 3 
    hand = {'a':0, 'p':0, 'l':0, 'e':0, 'f':0, 'r':0, 'x':0 ,'y':0}
    N = calculate_handlen(hand)
    expected = 0
    if N != expected:
        print("FAILURE: test_calculate_handlen()\nExpected", expected, "but got", N)
        failue = True

    # test 4 
    hand = {'f':1, 'o':2, 'b':2, 'a':2, 'r':1, 'z':1 ,'y':0}
    N = calculate_handlen(hand)
    expected = 1+2+2+2+1+1
    if N != expected:
        print("FAILURE: test_calculate_handlen()\nExpected", expected, "but got", N)
        failue = True

    # test 5 
    hand = {'f':1, 'o':2, 'b':2, 'a':2, 'r':1, 'z':1}
    N = calculate_handlen(hand)
    expected = 1+2+2+2+1+1
    if N != expected:
        print("FAILURE: test_calculate_handlen()\nExpected", expected, "but got", N)
        failue = True

    if not failure:
        print('SUCCESS: test_calculate_handlen()')

def test_substitute_hand():
    failure = False
    
    # test 1
    hand = {'a':1, 'p':2, 'l':1, 'e':1, 'f':1 , 'r':1, 'x':0 ,'y':0}
    N = calculate_handlen(hand)
    expected = 1+2+1+1+1+1
    if N != expected:
        print("FAILURE: test_calculate_handlen()\nExpected", expected, "but got", N)
        failue = True

    # test 2
    hand = {'a':1, 'p':2, 'l':1, 'e':1}
    N = calculate_handlen(hand)
    expected = 1+2+1+1
    if N != expected:
        print("FAILURE: test_calculate_handlen()\nExpected", expected, "but got", N)
        failue = True

    if not failure:
        print('SUCCESS: test_substitue_hand()')

def test_is_in_hand():
    failue = False

    # test 1
    hand = {'f':1, 'o':2}
    letter = 'f'
    b_result = is_in_hand(letter,hand)
    expected = True
    if expected != b_result:
        print('FAILURE: test_is_in_hand()\nExpected', expected, 'but got', b_result)
        failure = True

    # test 2 
    hand = {'f':1, 'o':2}
    letter = 'b'
    b_result = is_in_hand(letter,hand)
    expected = False
    if expected != b_result:
        print('FAILURE: test_is_in_hand()\nExpected', expected, 'but got', b_result)
        failure = True

    # test 3 
    hand = {'g':1, 'o':2, 's':1, 'x':1, 'y':0, 'a':0, 'n':0, 'k':0}
    letter = 'n'
    b_result = is_in_hand(letter,hand)
    expected = False
    if expected != b_result:
        print('FAILURE: test_is_in_hand()\nExpected', expected, 'but got', b_result)
        failure = True

    # test 4 
    hand = {'g':1, 'o':2, 's':1, 'x':1, 'y':0, 'a':0, 'n':0, 'k':0}
    letter = 'x'
    b_result = is_in_hand(letter,hand)
    expected = True
    if expected != b_result:
        print('FAILURE: test_is_in_hand()\nExpected', expected, 'but got', b_result)
        failure = True

    if not failue:
        print('SUCCESS: test_is_in_hand()') 


def test_calculate_num_vowels():
    failure = False
    
    # test 1
    hand = {'a':1, 'b':1, 'c':1, 'd':1, 'e': 1, 'f':1 }
    n = 2
    output = calculate_num_vowels(hand)
    if output != n:
        print('FAILURE: test_calculate_vowels()\nExpected', n,'but got',output) 
        display_hand(hand)
        failure = True

    # test 2
    hand = {'a':1, 'b':1, 'c':1, 'd':1, 'e': 1, 'f':1, 'i': 2 }
    n = 4
    output = calculate_num_vowels(hand)
    if output != n:
        print('FAILURE: test_calculate_vowels()\nExpected', n,'but got',output) 
        display_hand(hand)
        failure = True

    # test 3
    hand = {'b': 0, 'c':1, 'd':1, 'e': 1, 'f':1, 'i': 2, 'a':1, 'z':0, 'u':4 }
    n = 8
    output = calculate_num_vowels(hand)
    if output != n:
        print('FAILURE: test_calculate_vowels()\nExpected', n,'but got',output) 
        display_hand(hand)
        failure = True

    if not failure:
        print('SUCCESS: test_calculate_num_vowels')

def test_deal_hand():
    failure = False
    fails = 0

    # test 1 - test size of hand
    N = 7
    K = 100
    for i in range(K):
        hand = deal_hand(7)
        if N != calculate_handlen(hand):
            print('FAILURE: test_deal_hand()\nExpected', N, 'but got', calculate_handlen(hand))
            failure = True
            fails += 1
        elif calculate_num_vowels(hand) != int(math.ceil(N/3)): 
            print('FAILURE: test_deal_hand()\nExpected', int(math.ceil(N/3)), 'vowels but got ', calculate_num_vowels(hand))
            failure = True
            fails += 1 
    if not failure:
        print('SUCCESS: test_deal_hand()')
    elif failure:
        print('test_deal_hand() percent failue:', fails/K)

word_list = load_words()
print("----------------------------------------------------------------------")
print("Testing get_word_score...")
test_get_word_score()
print("----------------------------------------------------------------------")
print("Testing update_hand...")
test_update_hand()
print("----------------------------------------------------------------------")
print("Testing is_valid_word...")
test_is_valid_word(word_list)
print("----------------------------------------------------------------------")
print("Testing wildcards...")
test_wildcard(word_list)
print("----------------------------------------------------------------------")
print("Testing find_vowels...")
test_find_vowels()
print("----------------------------------------------------------------------")
print("Testing replace_vowels...")
test_replace_vowels()
print("----------------------------------------------------------------------")
print("Testing calculate_handlen...")
test_calculate_handlen()
print("----------------------------------------------------------------------")
print("Testing substitute_hand...")
test_substitute_hand()
print("----------------------------------------------------------------------")
print("Testing calculate_num_vowels...")
test_calculate_num_vowels()
print("----------------------------------------------------------------------")
print("Testing is_in_hand...")
test_is_in_hand()
print("----------------------------------------------------------------------")
print("Testing deal_hand...")
test_deal_hand()
print("----------------------------------------------------------------------")
print("All done!")
