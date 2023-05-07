import random

# List of words to choose from
with open('Wordlist.txt') as word_file:
    word_list = [word.strip() for word in word_file.readlines()]

# Randomly choose a word from the list
word = random.choice(word_list)

# Create a list of underscores to represent the word
word_length = len(word)
display = []
for _ in range(word_length):
    display += "_"

# Create a list to store the letters guessed
guessed_letters = []

# Create a variable to store the number of lives
lives = 6

# Create a variable to store the game state
game_over = False

# Create a variable to store the number of blanks left
blanks_left = word_length

# Create a function to check if the letter is in the word
def check_letter(letter):
    global lives
    global blanks_left
    global game_over
    global guessed_letters
    global display
    if letter in guessed_letters:
        print(f"You have already guessed {letter}")
    elif letter in word:
        guessed_letters.append(letter)
        for position in range(word_length):
            if word[position] == letter:
                display[position] = letter
                blanks_left -= 1
    else:
        guessed_letters.append(letter)
        lives -= 1
        print(f"{letter} is not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print("You lose.")
    print(display)

# Create a function to check if the player has won or lost
def check_win_or_lose():
    global game_over
    global blanks_left
    global lives
    if blanks_left == 0:
        game_over = True
        print("You win!")
    elif lives == 0:
        game_over = True
        print("You lose.")
        print(f"The word was {word}")

# Play the game
while not game_over:
    guess = input("Guess a letter or word: ").lower()
    if len(guess) == 1:
        check_letter(guess)
        check_win_or_lose()
    elif len(guess) == word_length:
        if guess == word:
            game_over = True
            print("You win!")
        else:
            print("That is not the correct word.")
            lives -= 1
            check_win_or_lose()
    else:
        print("Please enter a letter or word of the correct length.")