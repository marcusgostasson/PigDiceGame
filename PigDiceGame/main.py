"""Main Class."""
# import shell
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PigDiceGame import game, highscore

# !/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    """Execute the main program."""
    high = highscore.Highscore()
    #high.retreive_highscore_file()
    game.Game(high).start_game()


if __name__ == "__main__":
    main()
