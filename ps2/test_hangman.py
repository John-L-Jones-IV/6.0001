import unittest
from hangman import *
'''
This class is a unittest module for hangman.py
each method test_$function in hangman.py$ is designed
to verify the functionaly of each coresponding $function_in_hangman.py$

To use:
From the console in the project directory containing test_hangman.py, hangman.py, and words.txt
run:
python -m unittest test_hangman

The console output should tell you the result of each test
'''
class TestFindLetter(unittest.TestCase):

    def test_is_word_guessed(self):
        secret_word = 'apple'
        letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
        self.assertFalse(is_word_guessed(secret_word, letters_guessed))
        secret_word = 'apple'
        letters_guessed = ['a', 'p', 'l', 'e']
        self.assertTrue(is_word_guessed(secret_word, letters_guessed))

    def test_get_guessed_word(self):
        secret_word = 'apple'
        letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
        self.assertEqual(get_guessed_word(secret_word,letters_guessed),'_pp_e')

    def test_get_available_letters(self):
        letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
        expected_letters = 'abcdfghjlmnoqtuvwxyz'
        self.assertEqual(get_available_letters(letters_guessed),expected_letters)
        letters_guessed = ['a','b','c','d','e']
        expected_letters = 'fghijklmnopqrstuvwxyz'
        self.assertEqual(get_available_letters(letters_guessed),expected_letters)

    def test_match_with_gaps(self):
        self.assertFalse(match_with_gaps('te_t', 'tact'))
        self.assertFalse(match_with_gaps('a__le', 'banana'))
        self.assertTrue(match_with_gaps('a__le','apple'))
        self.assertFalse(match_with_gaps('a_ple', 'apple'))
        self.assertTrue(match_with_gaps('r_d', 'red'))
        self.assertTrue(match_with_gaps('r_d', 'rad'))
        self.assertFalse(match_with_gaps('s_x', 'twelve'))

    def test_show_possible_matches(self):
        self.assertEqual(show_possible_matches("t__t",'debug'),\
        "tact tart taut teat tent test text that tilt tint toot tort tout trot tuft twit")
        self.assertEqual(show_possible_matches("abbbb_",'debug'), "No matches found")
        self.assertEqual(show_possible_matches("a_pl_",'debug'), "ample amply")
	
    def test_num_unique_chars(self):
        self.assertEqual(num_unique_chars('aabbccdd'), 4)
        self.assertEqual(num_unique_chars('abcd'), 4)
        self.assertEqual(num_unique_chars('zyxw'), 4)
        self.assertEqual(num_unique_chars("xxrrdda"), 4)
        self.assertEqual(num_unique_chars('aAbBcC'),3)
