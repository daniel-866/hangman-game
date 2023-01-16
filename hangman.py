from random import choice

tries = 6
filename = "words.txt"
correct_letters = []
wrong_letters = []
separator = "|"


def choose_word(filename):
    """Opens the words.txt and chooses a random word for the game."""
    with open(filename, "r") as f:
        word_list = f.readlines()
        chosen_word = choice(word_list).lower()
    return chosen_word


def check_guess(chosen_word, guess):
    """Displays the word with blanks and or correct guessed letters"""
    for letter in chosen_word:
        if guess == letter:
            print(guess, end="|")
            correct_letters.append(guess)
        elif letter in correct_letters:
            print(letter, end="|")
        else:
            print("_", end="|")


# TODO
# 1: refactor code into functions
# 3: add a list of used words, to not repeat
# 4: print the _|_|_|_| per word before tries

# Randomly selects a word from word_list

chosen_word = choose_word(filename)
word_blanks = "_" * len(chosen_word)
word_blanks = separator.join(word_blanks)

print(word_blanks)


# Game loop
while tries > 0:
    print(f"\nTries left: {tries}")
    # Checks if entire word has been entered before tries ran out.
    if len(correct_letters) == len(chosen_word):
        print("You win!")
        break
    # Assign user input to variable guess
    guess = input("Guess a letter: ").lower()
    if len(guess) > 1 or guess.isalpha() != True:
        print("ONLY ONE LETTER IS ALLOWED!")
        continue

    if guess in correct_letters or guess in wrong_letters:
        print("You already used this letter.")
        check_guess(chosen_word, guess)
        continue

    if guess not in chosen_word:
        wrong_letters.append(guess)
        tries -= 1
        if tries == 0:
            print(f"You lose!\nit was {chosen_word}")
            break
        check_guess(chosen_word, guess)
        continue
    check_guess(chosen_word, guess)
    print(" ")
