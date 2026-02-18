"""
Game_UnterschichtLogic.py
Contains the main game logic for Snowman.
Imports the Snowman stages from ASCII_UnterschichtArt.
"""

import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


# -------------------------
# Helper functions
# -------------------------
def get_random_word():
    """Select a random word from the WORDS list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Display the current snowman stage and guessed word placeholders."""
    print(STAGES[mistakes])
    print("Word:", spaceholders(secret_word, guessed_letters))


def spaceholders(secret_word, guessed_letters):
    """Return the secret word with placeholders for unguessed letters."""
    result = ""
    for char in secret_word:
        if char in guessed_letters:
            result += char
        else:
            result += "_ "
    return result


def check_letter(secret_word, guess):
    """Return True if the guessed letter is in the secret word."""
    return guess in secret_word


# -------------------------
# Player guessing logic
# -------------------------
def ask_player(secret_word, guessed_letters, mistakes):
    """
    Handles the player's guessing loop. Updates guessed_letters and mistakes.
    Returns True if word fully guessed, False if lost.
    """
    while mistakes < len(STAGES) - 1:
        print("\n")
        guess = input("Guess a letter: ").lower()

        # Input validation: single alphabet character
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
            print("Wrong guess.")
            mistakes += 1

        display_game_state(mistakes, secret_word, guessed_letters)

        if "_" not in spaceholders(secret_word, guessed_letters):
            print("Congratulations! You saved the snowman!")
            return True

    print("You lost. The snowman melted.")
    print("The word was:", secret_word)
    return False


# -------------------------
# Main game function
# -------------------------
def play_game():
    """Start a full game of Snowman."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")
    display_game_state(mistakes, secret_word, guessed_letters)

    ask_player(secret_word, guessed_letters, mistakes)
