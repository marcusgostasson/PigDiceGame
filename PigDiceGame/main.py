"""Main Class."""
# import shell
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PigDiceGame import game

# !/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    """Execute the main program."""
    # print(__doc__)
    # shell.Shell().cmdloop()
    game.Game().start_game()


if __name__ == "__main__":
    main()
