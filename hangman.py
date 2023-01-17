from random import choice

# TODO add counter of correct words

animals_set = []
countries_set = []
food_set = []
correct_letters = []
wrong_letters = []
wins = 0


def get_wordset(filename, word_set):
    """Opens the wordset .txt and imports data to a list of words"""
    with open(filename, "r") as f:
        word_list = f.readlines()
        for i in word_list:
            word_set.append(i.lower().strip("\n"))
    return word_set


def choose_word(word_set):
    """Chooses a random word for the game, that wasn't guessed correctly yet."""
    chosen_word = choice(word_set)
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


def set_word_group():
    """Sets word group to play with"""
    while True:
        choice = input("Choose word group:\n1)Animals\n2)Countries\n3)Food\n> ")
        if choice == "quit":
            exit()
        elif choice == "1":
            return get_wordset("animals.txt", animals_set)
        elif choice == "2":
            return get_wordset("countries.txt", countries_set)
        elif choice == "3":
            return get_wordset("food.txt", food_set)
        else:
            print("Enter a valid option.")
            continue


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
    if wins > 0:
        print(f"You have {wins} correct words!")
    # Set word group to play with
    chosen_set = set_word_group()
    # Set difficulty level (amount of tries)
    tries = set_difficulty()
    # Reset tried letters
    wrong_letters.clear()
    correct_letters.clear()
    # Randomly selects a word from word_set
    chosen_word = choose_word(chosen_set)

    # Start of round
    while tries > 0:
        # Checks if entire word had already been entered before tries ran out.
        if len(correct_letters) == len(chosen_word):
            print("\nYou win!\n")
            chosen_set.remove(chosen_word)
            wins += 1
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
