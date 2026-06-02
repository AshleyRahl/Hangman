import random

'''Get a random word from the list'''
def get_random_word():
    # List of words to choose from
    # word_list = ["superman", "batman", "wonderwoman", "flash", "aquaman", "cyborg"]

    # Startwith a word - for testing purposes
    word = "superman"

    # Randomly select a word from the list
    # return random.choice(word_list)
    return word

'''Welcome message and rules of the game'''
def welcome_message():
    print("\n---- Welcome to the Hangman Game ----\n")
    print("The Rules: \n1. You have 6 lives to guess the word. \n2. Each time you guess a letter that is not in the word, you lose a life. \n3. The game ends when you either guess the word correctly or run out of lives. \n4. Good luck and have fun playing! \n")
    print()

'''Handles getting a guess - a letter from user.
Checking if it's a single letter, a valid letter and a new letter (not guessed before)'''
def get_valid_input(guessed_letters):
    # Loop until the user provides a valid input
    while True:
        # Get the user's guess
        guess = input("Guess a letter: ").lower()
        
        # Validate the input
        if len(guess) != 1 or not guess.isalpha(): # Check if the input is a single letter and is an alphabet
            print("Invalid input. Please enter a single letter.\n")
            continue
        
        if guess in guessed_letters: # Check if the user has already guessed the letter before
            print(f"You've alreasdy guessed {guess}. Try a different letter.\n")
            continue

        return guess

'''If guessed letter is in word, replace the corresponding underscore with the correctly guessed letter'''
def update_display(word, display, guess):
    for i in range(len(word)):
        if word[i] == guess:
            display[i] = guess

'''
Play the game
Create a loop to keep the game running until the user either wins (guesses the word) or loses (runs out of lives)
'''
def hangman():
    word = get_random_word() # Get a random word from random function

    letters_in_word = list(word) # Create a list of letters of the word

    # Create a list of underscores to represent the letters in the word
    display = ["_" for _ in letters_in_word]

    guessed_letters = [] # Keep track of what user already tried

    lives = 6 # User life attempts

    # Initial game status - this gives the user idea of possible word
    print(f"Your word contains {len(word)} letters.")
    print(f"Here is the word: {' '.join(display)}\n")
    
    # Keep game in a loop as long as they have lives AND missing words
    while "_" in display and lives > 0:
        print(f"Lives left: {lives}") # tell user how many lives they have left
        print(f"Your guesses so far: {' '.join(guessed_letters)}\n") # tell user what they already tried
        
        # Get a valid guess from the user
        guess = get_valid_input(guessed_letters) # passing the list of guessed letters to check for duplicates
        guessed_letters.append(guess) # add the guessed letter to the list of already guessed letters
        guessed_letters.sort() # sort the guessed letters alphabetically for better readability

        # Check if the guess letter is in word
        if guess in letters_in_word:
            # function to replace the corresponding underscore with the letter
            update_display(word, display, guess)
            print(f"Correct! The word updated: {' '.join(display)}\n")
        else:
            lives -= 1 # deduct a life 
            print(f"Sorry! Try again. The word: {' '.join(display)}\n")

    # Final Win/Loss Check
    if "_" not in display:
        print("\nCongratulations! You've guessed the word correctly!")
    else:
        print(f"\nGame over! You've run out of lives. \nThe word was: {word}")
    
        
''''Main function to run the game'''
welcome_message()
hangman()
