"""Main Class."""
# import shell
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PigDiceGame import game, highscore

"""
"Pig" is a dice game for two players aiming to reach 100 points first.
Roll dice, avoiding ones to accumulate points.
Decide whether to roll again or pass to the next player.
Balancing risk and reward is key 🎲.
"""


def main():
    """Execute the main program."""
    high = highscore.Highscore()
    game.Game(high).start_game()


if __name__ == "__main__":
    main()
