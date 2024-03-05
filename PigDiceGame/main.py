"""Main Class."""
# import shell
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PigDiceGame import game, highscore


def main():
    """Execute the main program."""
    high = highscore.Highscore()
    game.Game(high).start_game()


if __name__ == "__main__":
    main()
