import random

# -------------------------
# Snowman ASCII Art stages
# -------------------------
STAGES = [
    """
     ___  
    /___\\ 
    (o o) 
    ( : ) 
    ( : ) 
    """,
    """
     ___  
    /___\\ 
    (o o) 
    ( : ) 
    """,
    """
     ___  
    /___\\ 
    (o o) 
    """,
    """
     ___  
    /___\\ 
    """
]

# -------------------------
# List of secret words
# -------------------------
WORDS = ["python", "git", "github", "snowman", "meltdown"]


# -------------------------
# Helper functions
# -------------------------
def get_random_word():
    """
    Select a random word from the WORDS list.
    :return: str
    """
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes):
    """
    Display the snowman stage according to the number of mistakes.
    :param mistakes: int
    """
    print(STAGES[mistakes])


def spaceholders(secret_word, guessed_letters):
    """
    Show the word with placeholders for letters not yet guessed.
    :param secret_word: str
    :param guessed_letters: list
    :return: str
    """
    display = ""
    for char in secret_word:
        if char in guessed_letters:
            display += char
        else:
            display += "_ "
    return display


def check_letter(secret_word, guess):
    """
    Check if the guessed letter is in the secret word.
    :param secret_word: str
    :param guess: str
    :return: bool
    """
    return guess in secret_word


# -------------------------
# Player input / guessing
# -------------------------
def ask_player(secret_word, guessed_letters, mistakes):
    """
    Handles the player's guessing loop. Updates guessed_letters and mistakes.
    :param secret_word: str
    :param guessed_letters: list
    :param mistakes: int
    :return: bool -> True if word fully guessed, False if lost
    """
    while mistakes < len(STAGES) - 1:
        print("\n")
        guess = input("Guess a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if check_letter(secret_word, guess):
            print("Correct guess:", guess)
        else:
            mistakes += 1
            print("Wrong guess.")

        display_game_state(mistakes)
        print("Word:", spaceholders(secret_word, guessed_letters))

        # Check if word is fully guessed
        if "_" not in spaceholders(secret_word, guessed_letters):
            print("Congratulations! You saved the snowman!")
            return True

    # Lost condition
    print("You lost. The snowman melted.")
    print("The word was:", secret_word)
    return False


# -------------------------
# Main game function
# -------------------------
def play_game():
    """
    Main function to start the Snowman game.
    """
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")
    display_game_state(mistakes)
    print("Word:", spaceholders(secret_word, guessed_letters))

    # Start guessing loop
    ask_player(secret_word, guessed_letters, mistakes)


# -------------------------
# Entry point
# -------------------------
if __name__ == "__main__":
    play_game()
