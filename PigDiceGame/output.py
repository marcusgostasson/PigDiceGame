"""Ascii class."""

END = "\033[0m"
CITALIC = "\33[3m"
UNDERLINE = "\033[4m"
YELLOW = "\u001b[33m"


class Output:
    """Instanciate ascii class."""

    def __init__(self) -> None:
        """Pass."""

    def pelle(self):
        """Pelle."""
        print(
            """@@@&&@@&&&&#/**/*,,*////((#%###%%#/*#@@@@@@&&&&@@@
@@@@@@&%(///*///((###%%&&&&&&%%%%&&#/**(%&@@@@&&@&
@@@@@%((((#######%&&&&&&&%###(((((####((((#&@@@&@@
%&&#(#((#####((((((((////*****,,*,**/(%%%%###&@@@@
&&#(//(##(/**************,,**,,,,,,,*/(#%%%##&@@@@
&%((((//***,,,,*,,*******************///(#(#(#&&#(
&##(*****************************//////////##/%%&%
&(//**,*****////**********/*****///(((((/***#(#%%%
%(**/****///////*****************//(((((//***(#%#(
@#/////////////////*******/*/////(///((((((//(#%%&
@%(((//*//**//((((####(#(((#(#####(((//(((#(((#@@@
*//(##(/((######%&&&&&&#(((#&&&&&%%%##%%%%%%((/(@@
(#%(/*/(#(((#%&&&&%%%##%(//%%%%##%%&&&%(((#(##%%@@
/(#/(///(/((((((######&#***(&%####((((((((#/###&@@
&@#(#////////////////(#/***/(#(//////(((((((##%@@@
@@@#//////((//*/*///(#(//***/##(/////((((((/(%@@@@
@&#(**///////////((#%/**,**///#%%(((((((((//#@@@@@
%#/////*/*/////(##%#(#%%###%&%##%&%###(((//(%&&&&&
@%##&&@@/**/((#%#(((//((#%&%#######%%%#((/(%##%%&@
&&%(#%%##///(#((#%%#(((##%%%%%%&&&%####((////#%&@@
&&&%%&#(%%//((((((((/////((((((#(((((###((#&&&%%&@
&%#####%&%#//((#((((((##########(((#####%#(#&@&&&&
&%%%%&&@@&%%(/(#((/(((#((((((((((((###%%##(((&@@@@
@@&&&&&%%%%%#(((((/////(((##((((/(##&@&%##((//%&&@"""
        )
        print("You chose death\n")

    def game_rules(self):
        """Display the rules of the game."""
        print(
            UNDERLINE
            + CITALIC
            + """
\nEach turn, a player repeatedly rolls a die until either a 1 is rolled
or the player decides to "hold":

If the player rolls a 1, they score nothing and it becomes the next
player's turn.
If the player rolls any other number, it is added to their turn total and
the player's turn continues.
If a player chooses to "hold", their turn total is added to their score,
and it becomes the next player's turn.
The first player to score 100 or more points wins\n"""
            + END
        )

    def display(self):
        """Display the startup menu to the user."""
        print(YELLOW + "Hello and welcome to Pig Dice Game" + END)
        print(
            """-------------------------------------------------
Press 1 if you want to play with a friend
Press 2 if you want to play vs the computer
Press 3 if you want to see the rules for the game
Press 4 if you want to see highscore
Press 5 if you want to quit
-------------------------------------------------"""
        )
