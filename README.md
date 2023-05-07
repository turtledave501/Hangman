# Hangman

This code is a simple implementation of a hangman game where a player has to guess a hidden word by guessing its letters one by one. The code randomly chooses a word from a list of words given in a file named 'Wordlist.txt'. The player has to guess a letter or the entire word. The game ends when the player has correctly guessed all the letters of the word or runs out of lives.

## Usage
To use this code, you need to have Python installed on your system. You can run the code by opening a terminal or command prompt in the folder containing the Python file and typing the following command:
```
python hangman.py
```
This will start the game and prompt the player to enter a letter or word to guess. The player can keep guessing until they win or lose the game. The player has 6 lives.

## Code Structure
The code starts by reading a list of words from a file named 'Wordlist.txt' and randomly chooses a word from it. It then creates a list of underscores to represent the word, initializes the number of lives and game state, and creates an empty list to store the guessed letters.

The `check_letter` function takes a letter as input and checks if it is in the word. If the letter has already been guessed, it informs the player. If the letter is in the word, it updates the display and the number of blanks left. If the letter is not in the word, it decrements the number of lives and informs the player. If the player runs out of lives, the game ends.

The `check_win_or_lose` function checks if the player has won or lost the game by checking the number of blanks left and the number of lives remaining.

The `while` loop runs until the game is over. The player is prompted to enter a letter or word, and the corresponding function is called to check the guess. If the guess is a letter, the `check_letter` function is called, and if the guess is a word, the `check_win_or_lose` function is called to check if it matches the hidden word.

## Modification
You can modify the code by changing the list of words in the 'Wordlist.txt' file or adding your own words. You can also modify the number of lives the player has or add a feature to display the hanging man.

Wordlist: https://www.mit.edu/~ecprice/wordlist.10000

## Future updates
- [ ]  Add a better UI
- [ ]  Add the actual "Hanging man"
- [ ]  Hint implementation