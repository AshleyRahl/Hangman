# Hangman Game

Hangman is a word-guessing game.
Where a player needs to guess the secret word - one letter at a time.

This command-line Hangman game pulls from a library of over 200+ words. This project focuses on **clean code principles** and **functional decomposition**.

## Project Structure
- `hangman.py`: The main game engine containing the logic and user interface.
- `wordsList.py`: A dedicated data module containing the word bank.

## Technical Features
- **Data Sanitization:** Implements a cleaning loop that filters out complex words (containing spaces or hyphens) from the imported list to ensure a fair user experience.
- **Modular Architecture:** - `get_valid_input()`: A standalone validator that ensures only new, alphabetical characters are processed.
    - `update_display()`: A pure logic function dedicated to state updates.
- **Dynamic Feedback:** Real-time tracking of remaining lives and an alphabetically sorted list of previous guesses.
- **Spaced UI Layout:** Utilized `.join()` string formatting to alter the display, improving readability and player focus during gameplay.

## How to Play
1. Ensure both `hangman.py` and `wordsList.py` are in the same folder.
2. Run the game:
   ```bash
   python hangman.py
   ```
3. Guess one letter at a time to reveal the hidden word before you run out of lives!

