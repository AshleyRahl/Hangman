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

'''Play the game'''
def hangman():
    # Get a random word from random function
    word = get_random_word()
    # Create a list of letters in the word
    letters_in_word = list(word)

    # Create a list of underscores to represent the letters in the word
    display = ["_" for _ in letters_in_word]

    # Keep track of what user already tried
    guessed_letters = [] # create an empty list to store guessed letters
    guessed_letters.sort() # sort the guessed letters alphabetically for better readability
    
    # User life attempts
    lives = 6

    print(f"Your word contains {len(word)} letters.")
    print(f"Here is the word: {' '.join(display)}\n")
    
    # Keep game in a loop as long as they have lives AND missing words ("_")
    while "_" in display and lives > 0:
        print(f"Lives left: {lives}")
        print(f"Your guesses so far: {' '.join(guessed_letters)}\n")
        # Get the user's guess
        guess = input("Guess a letter: ").lower()


        # Check if the user has already guessed the letter
        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try a different letter.\n")
            continue # skip the rest of the loop and prompt for another guess

        # Check if the input is a single letter
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.\n")
            continue

        # Add the guessed letter to the list of guessed letters
        guessed_letters.append(guess) # add the guessed letter to the list of already guessed letters


        # Check if the guess is in the word
        if guess in letters_in_word:
            # If it is, replace the corresponding underscore with the letter
            for i in range(len(letters_in_word)):
                if letters_in_word[i] == guess:
                    display[i] = guess
            print(f"Correct! The word updated: {' '.join(display)}\n")
        else:
            lives -= 1 # deduct a life 
            print(f"Sorry! Try again. The word: {' '.join(display)}\n")
            # print(f"")

    # Check if the user has guessed the word correctly, congratulate them
    if "_" not in display:
        print("\nCongratulations! You've guessed the word correctly!")
    else:
        print(f"\nGame over! You've run out of lives. \nThe word was: {word}")
    
        
''''Main function to run the game'''
welcome_message()
hangman()
