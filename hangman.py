
# Startwith a word - for testing purposes
word = "superman"

# Create a list of letters in the word
letters = list(word)
# Create a list of underscores to represent the letters in the word
display = ["_" for _ in letters]

print(f"Your word contains {len(word)} letters. Here is the word: ")
print(display)


def hangman():
    # Get the user's guess
    guess = input("Guess a letter: ").lower()

    # Check if the guess is in the word
    if guess in letters:
        # If it is, replace the corresponding underscore with the letter
        for i in range(len(letters)):
            if letters[i] == guess:
                display[i] = guess
        print(f"Correct! The word now looks like this: \n{display}")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
        print(display)

hangman()