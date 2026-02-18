"""
main.py
Entry point for the Snowman game.
"""

from game_logic import play_game

if __name__ == "__main__":
    while True:
        play_game()

        while True:
            restart = input("Would you like to play again? (y/n): ").lower()

            if restart == "y":
                print("Restarting the game...")
                break  # verlässt nur die innere Schleife
            elif restart == "n":
                print("Goodbye!")
                exit()
            else:
                print("Please enter y or n.")
