"""
Unit tests for the hangman game functions.
(Test the small predictable parts)

update_display: 
- test that it correctly updates the display with the guessed letter
- test that it handles multiple occurrences of the guessed letter
- test that it does not update the display if the guessed letter is not in the word

get_random_word (Not yet added): 
- test that it returns a word from the list

get_valid_input (Not yet added):
- test that it only accepts valid input and handles duplicates

"""

import unittest
from hangman import update_display

class TestHangman(unittest.TestCase):
    '''If guessed letter is in word, replace the corresponding underscore with the correct guessed letter'''
    def test_update_display_single_letter(self):
        word = "superman"
        display = ["_", "_", "_", "_", "_", "_", "_", "_"]
        guess = "s"
        update_display(word, display, guess)
        self.assertEqual(display, ["s", "_", "_", "_", "_", "_", "_", "_"])
        # self.assertEqual(display, "s _ _ _ _ _ _ _")

    '''If guessed letter is in word, but same letter accures in more then one place, replace all the corresponding underscores with the correct guessed letter'''
    def test_update_display_multiple_letters(self):
        word = "apple"
        display = ["_", "_", "_", "_", "_"]
        guess = "p"
        update_display(word, display, guess)
        self.assertEqual(display, ["_", "p", "p", "_", "_"])
    
    def test_update_display_no_letter(self):
        word = "banana"
        display = ["_", "_", "_", "_", "_", "_"]
        guess = "x"
        update_display(word, display, guess)
        self.assertEqual(display, ["_", "_", "_", "_", "_", "_"])


if __name__ == '__main__':
    unittest.main()