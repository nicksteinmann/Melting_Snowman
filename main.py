import random

# Snowman ASCII Art stages
STAGES = [
    # Stage 0: Full snowman
    """
     ___  
    /___\\ 
    (o o) 
    ( : ) 
    ( : ) 
    """,
    # Stage 1: Bottom part starts melting
    """
     ___  
    /___\\ 
    (o o) 
    ( : ) 
    """,
    # Stage 2: Only the head remains
    """
     ___  
    /___\\ 
    (o o) 
    """,
    # Stage 3: Snowman completely melted
    """
     ___  
    /___\\ 
    """
]

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: ", secret_word)
    display_game_state(mistakes, secret_word, guessed_letters)
    print(spaceholders(secret_word))

    # TODO: Build your game loop here.
    # For now, simply prompt the user once:

    guess = asking_player(secret_word, mistakes)
    guessed_letters.append(guess)


def spaceholders(secret_word):
    return "_" * len(secret_word)


def check_letter(secret_word, guess):
    if guess in secret_word:
        return True


def asking_player(secret_word, mistakes):
    mistakes = 0
    while mistakes < 3:
        guess = input("Guess a letter: ").lower()
        check_if_correct = check_letter(secret_word, guess)  # -> bool
        if check_if_correct:
            print("You guessed: " + guess)
            print(STAGES[mistakes])
            return guess
        else:
            print("Wrong guess. Try again.")
            mistakes += 1
            print(STAGES[mistakes])
    print("You lost. Try again.")


if __name__ == "__main__":
    play_game()
