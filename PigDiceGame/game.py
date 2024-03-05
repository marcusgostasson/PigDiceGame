"""Game class."""
import time
import os
import platform
from PigDiceGame import player
from PigDiceGame import computer
from PigDiceGame import dice
from PigDiceGame import highscore
from PigDiceGame import histogram
from PigDiceGame import ascii_pictures
RED = '\033[91m'
GREEN = '\33[32m'
YELLOW = '\u001b[33m'
END = '\033[0m'
CITALIC = '\33[3m'
UNDERLINE = '\033[4m'

post_winner = highscore.Highscore()


class Game:
    """Game class."""

    def __init__(self):
        """Instanciate game class."""
        self.playing = True
        self.players = {}

    def display(self):
        """Display the startup menu to the user."""
        print(YELLOW + "Hello and welcome to Pig Dice Game" + END)
        print("""-------------------------------------------------
Press 1 if you want to play with a friend
Press 2 if you want to play vs the computer
Press 3 if you want to see the rules for the game
Press 4 if you want to see highscore
Press 5 if you want to quit
-------------------------------------------------""")

    def get_choice_from_user(self, prompting):
        """Prompting the user for an input."""
        choice = input(prompting)
        return choice

    def clear_screen(self):
        """Makes sure that it clears screen for both Windows
        and Mac users"""
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')

    def player_vs_player(self):
        """Logic when the user picks play vs another player."""
        player1 = self.setup_player()
        player2 = self.setup_player()
        self.clear_screen()
        playing = True
        while playing:
            playing = self.player_playing(player1)
            if (playing is False and player1.get_total_score() < 100):
                self.clear_screen()
                print(RED + player1.get_name() + " surrendered" + END +
                      " and " + GREEN + player2.get_name() + " won" + END)
            elif playing is True:
                playing = self.player_playing(player2)
                if (playing is False and player2.get_total_score() < 100):
                    self.clear_screen()
                    print(RED + player2.get_name() + " surrendered" + END +
                          " and " + GREEN + player1.get_name() + " won" + END)

    def player_vs_computer(self):
        """Logic when the user picks play vs the computer."""
        player1 = self.setup_player()
        self.clear_screen()
        while True:
            difficulty = self.get_choice_from_user(
"""
What difficulty do you want?
1. Playing against a new born baby
2. Playing against a grown up
3. Completly random no logic\nChoice: """) # noqa: 122 ignores line missing indentation
            if difficulty in ["1", "2", "3", "Pelle"]:
                break
            print("Invalid option")
            self.clear_screen()

        if difficulty == "Pelle":
            self.clear_screen()
            ascii_pictures.Ascii().pelle()
        intelligence = computer.Computer(difficulty)
        self.players["Computer"] = intelligence.get_total_score()
        playing = True
        while playing:
            playing = self.player_playing(player1)
            if (playing is False and player1.get_total_score() < 100):
                self.clear_screen()
                print(RED + player1.get_name() + " surrendered" + END +
                      " and " + GREEN + "Computer won" + END)
            elif playing is True:
                playing = self.computer_playing(intelligence)

    def quit(self):
        """Stop the program."""
        print("Quit out of the game")
        self.playing = False

    def handle_choice(self, choice):
        """Goes into a function depending what the user types in."""
        if choice == "1":
            self.clear_screen()
            self.player_vs_player()
        elif choice == "2":
            self.clear_screen()
            self.player_vs_computer()
        elif choice == "3":
            self.clear_screen()
            self.game_rules()
        elif choice == "4":
            self.clear_screen()
            chart = histogram.Histogram()
            chart.plot_chart(post_winner)
        elif choice == "5":
            self.quit()
        else:
            print(RED + "Invalid option" + END)

    def start_game(self):
        """Beginning of the program."""
        while self.playing:
            self.display()

            choice = self.get_choice_from_user("Choice: ")
            self.handle_choice(choice)

    def player_playing(self, current_player):
        """Logic for when the player is playing."""
        die = dice.Dice()
        score = current_player.get_total_score()
        game_is_being_played = True
        while game_is_being_played:
            print(current_player.get_name() + " you currently have "
                  + str(score) + " point(s)")

            choice = self.get_choice_from_user(
                current_player.get_name() +
""" what do you want to do?:\n
Press 1 to toss
Press 2 to stay
Press 3 to change name
Press 4 to surrender
Choice: """) # noqa: 122 ignores line missing indentation

            if choice == "1":
                self.clear_screen()
                die_value = current_player.throw_dice(die)
                print(current_player.get_name() + " rolled a " + str(die_value))
                if die_value != 1:
                    score += die_value
                    game_is_being_played = self.check_if_winner(score,
                                                                current_player)
                    continue

                self.clear_screen()
                print("Oh you got a " + str(die_value) +
                      " better luck next time\n")
                game_is_being_played = False
                return True

            if choice == "2":
                current_player.set_total_score(score)
                name = current_player.get_name()
                self.players[name] = current_player.get_total_score()

                current_points = current_player.get_total_score()
                self.clear_screen()
                print(current_player.get_name() + " stayed and now have "
                      + str(current_points) + " point(s)\n")
                game_is_being_played = False
                return True

            if choice == "3":
                self.clear_screen()
                old_name = current_player.get_name()
                value = self.players.pop(old_name)
                new_name = self.change_name(current_player)
                new_key = new_name
                self.players[new_key] = value
                self.clear_screen()
                print("Your new name is now " + new_name)
                continue

            if choice == "4":
                return False

            if choice == "ezwin":
                current_player.set_total_score(100)
                game_is_being_played = self.check_if_winner(
                    100, current_player)
            else:
                print(RED + "That's not an option" + END)
        return False

    def computer_playing(self, pc):
        """Logic for when the computer is playing."""
        die = dice.Dice()
        score = pc.get_total_score()
        score_this_round = 0
        game_is_being_played = True
        toss_counter = 0
        while game_is_being_played:
            print("Computer currently have " + str(score) + " point(s)")
            time.sleep(1)
            decision = pc.difficulty_choice(toss_counter, score_this_round)
            choice = decision[0]
            if choice == "toss":
                self.clear_screen()
                toss_counter += 1
                die_value = pc.throw_dice(die)
                print("Computer got a " + str(die_value))
                if die_value != 1:
                    score += die_value
                    game_is_being_played = self.check_if_winner(score, pc)
                    score_this_round += die_value
                    continue

                print("Oh you got a " + str(die_value)
                      + " better luck next time\n")
                game_is_being_played = False
                return True

            if choice == "stay":
                pc.set_total_score(score)
                current_points = pc.get_total_score()
                self.clear_screen()
                print("Computer stayed and now have " + str(current_points)
                      + " point(s)\n")
                game_is_being_played = False
                return True

    def check_if_winner(self, score, current_player):
        """Check if the current toss is enough to win."""
        if isinstance(current_player, player.Player):
            if score >= 100:
                print(GREEN + "You won in " + str(
                    current_player.get_tossed_amount())
                      + " throws!" + END)
                current_player.set_total_score(score)
                points = current_player.get_total_score()
                self.players[current_player.get_name()] = points
                post_winner.add_winner(current_player.get_name())
                return False

            return True
        if isinstance(current_player, computer.Computer):
            if score >= 100:
                print(GREEN + "Computer won in " + str(
                    current_player.get_tossed_amount())
                      + " throws!" + END)
                current_player.set_total_score(score)
                self.players["Computer"] = current_player.get_total_score()
                post_winner.add_winner("Computer")
                return False

        return True

    def get_player_score(self, player_name):
        """
        To get the players score, this is used for easier testing if the.

        score got updated.
        """
        if player_name in self.players:
            return self.players[player_name]

        return None

    def change_name(self, current_player):
        """Set a new name for the player."""
        print("Old name: " + current_player.get_name())
        new_name = input("Input new name: ").capitalize()
        current_player.set_name(new_name)

        return new_name

    def setup_player(self):
        """Set up the player."""
        player_name = input("What is your name? ").capitalize()
        new_player = player.Player(player_name)
        self.players[player_name] = new_player.get_total_score()

        return new_player

    def game_rules(self):
        """Display the rules of the game."""
        print(UNDERLINE + CITALIC + """
\nEach turn, a player repeatedly rolls a die until either a 1 is rolled
or the player decides to "hold":

If the player rolls a 1, they score nothing and it becomes the next
player's turn.
If the player rolls any other number, it is added to their turn total and
the player's turn continues.
If a player chooses to "hold", their turn total is added to their score,
and it becomes the next player's turn.
The first player to score 100 or more points wins\n""" + END)
