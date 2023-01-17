from random import choice

words = []
# There will be multiple files, different word groups
filename = "words.txt"
correct_letters = []
wrong_letters = []
guessed_words = []

# Opens the words.txt and populates 'words' list.
with open(filename, "r") as f:
    word_list = f.readlines()
    for i in word_list:
        words.append(i.lower().strip("\n"))


def choose_word(word_group):
    """Chooses a random word for the game, that wasn't guessed correctly yet."""
    chosen_word = choice(words)
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


def set_difficulty():
    """Sets game difficulty, Easy, Normal, Hard"""
    while True:
        difficulty = input(
            "Choose game difficulty:\n1)Easy\n2)Normal\n3)Hard\n> "
        ).lower()
        if difficulty == "quit":
            exit()
        elif difficulty == "1":
            tries = 10
            return tries
        elif difficulty == "2":
            tries = 6
            return tries
        elif difficulty == "3":
            tries = 4
            return tries
        else:
            print("Enter a valid option.")
            continue


# Game starts
while True:
    print("Enter 'quit' at any time to end the game.")
    # Set difficulty level (amount of tries)
    tries = set_difficulty()
    # Reset tried letters
    wrong_letters.clear()
    correct_letters.clear()
    # Randomly selects a word from word_list
    chosen_word = choose_word(filename)

    # Start of round
    while tries > 0:
        # Checks if entire word had already been entered before tries ran out.
        if len(correct_letters) == len(chosen_word):
            print("\nYou win!\n")
            # guessed_words.append(chosen_word)
            words.remove(chosen_word)
            break
        elif not len(correct_letters) and not len(wrong_letters):
            check_guess(chosen_word, "")

        print(f"\nTries left: {tries}")
        # Assign user input to variable guess
        guess = input("Guess a letter: ").lower()
        if guess == "quit":
            exit()
        if len(guess) > 1 or guess.isalpha() != True:
            print("ONLY ONE LETTER IS ALLOWED!")
            continue

        if guess in correct_letters or guess in wrong_letters:
            print("You already used this letter.")
            check_guess(chosen_word, "")
            continue

        if guess not in chosen_word:
            wrong_letters.append(guess)
            tries -= 1
            if tries == 0:
                print(f"\nYou lose!\nit was {chosen_word}")
                break
            check_guess(chosen_word, guess)
            continue
        check_guess(chosen_word, guess)
