import random

# Get a random word from the list
def get_random_word():
    # List of words to choose from
    # word_list = ["superman", "batman", "wonderwoman", "flash", "aquaman", "cyborg"]

    # Startwith a word - for testing purposes
    word = "superman"

    # Randomly select a word from the list
    # return random.choice(word_list)
    return word

# Play the game
def hangman():
    word = get_random_word()
    # Create a list of letters in the word
    letters_in_word = list(word)

    # Create a list of underscores to represent the letters in the word
    display = ["_" for _ in letters_in_word]

    # Keep track of what user already tried
    guessed_letters = []
    # User life attempts
    lives = 6

    print(f"Your word contains {len(word)} letters. Here is the word: ")
    print(display)
    
    # Keep game in a loop as long as they have lives AND missing words ("_")
    while "_" in display and lives >= 0:
        print(f"\nLives left: {lives}")
        print(f"Your guesses so far: {guessed_letters}\n")
        # Get the user's guess
        guess = input("Guess a letter: ").lower()

        guessed_letters.append(guess) # add the guessed letter to the list of already guessed letters
        # Check if the guess is in the word
        if guess in letters_in_word:
            # If it is, replace the corresponding underscore with the letter
            for i in range(len(letters_in_word)):
                if letters_in_word[i] == guess:
                    display[i] = guess
            print(f"Correct! The word now looks like this: \n{display}")
        else:
            lives -= 1 # deduct a life 
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(display)

    if "_" not in display:
        print("\nCongratulations! You've guessed the word correctly!")
    else:
        print(f"\nGame over! You've run out of lives. \nThe word was: {word}")
    
        

hangman()
