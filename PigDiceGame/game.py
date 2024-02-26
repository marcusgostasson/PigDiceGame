from . import player
from . import computer
from . import dice
from . import highscore
import random
# Did we put a licence when we created the repository?
RED = '\033[91m'
GREEN = '\33[32m'
END = '\033[0m'


class Game:
    """Initialize the Game class."""
    def __init__(self):
        self.playing = True
        self.players = {}

    def display(self):
        """Displaying the startup menu to the user."""

        print("""Hello and welcome to Pig Dice Game
Press 1 if you want to play with a friend
Press 2 if you want to play vs the computer
Press 3 if you want to see the rules for the game
Press 4 if you want to quit""")

    def get_choice_from_user(self, prompting):
        """Prompting the user for an input until its a number."""

        while True:
            try:
                choice = int(input(prompting))
            except ValueError:
                print(RED + "Invalid input. That is not a number" + END)
                continue

            return choice

    def player_vs_player(self):
        """The logic when the user picks play vs another player."""

        player1 = self.setup_player()
        player2 = self.setup_player()
        playing = True
        while playing:
            playing = self.player_playing(player1)
            if (playing is False and player1.get_total_score() < 100):
                print(RED + player1.get_name() + " surrendered" + END + " and " + GREEN + player2.get_name() + " won" + END)
            elif playing is True:
                playing = self.player_playing(player2)
                if (playing is False and player2.get_total_score() < 100):
                    print(RED + player2.get_name() + " surrendered" + END + " and " + GREEN + player1.get_name() + " won" + END)

    def player_vs_computer(self):
        """The logic when the user picks play vs the computer."""

        player_name = input("What is your name? ")
        player1 = player.Player(player_name)
        self.players[player1.get_name()] = player1.get_total_score()
        difficulty = self.get_choice_from_user("""What difficulty do you want?
1. Playing against a new born baby
2. Playing against my uncle that is pretty good with numbers
3. Playing against Pelle, if you know you know
4. Completly random no logic\nChoice: """)
        intelligence = computer.Computer(difficulty)
        playing = True
        while playing:
            playing = self.player_playing(player1)
            if (playing is False and player1.get_total_score() < 100):
                print(RED + player1.get_name() + " surrendered" + END + " and " + GREEN + "Computer won" + END)
            elif playing is True:
                playing = self.computer_playing(intelligence)
                if (playing is False and computer.get_total_score() < 100):
                    print(RED + "Computer surrendered" + END + " and " + GREEN + player1.get_name() + " won" + END)

    def quit(self):
        """Stops the program"""

        print("Quit out of the game")
        self.playing = False

    def handle_choice(self, choice):
        """Goes into a function depending what the user types in."""

        if choice == 1:
            self.player_vs_player()
        elif choice == 2:
            self.player_vs_computer()
        elif choice == 3:
            self.game_rules()
        elif choice == 4:
            self.quit()
        else:
            print(RED + "Invalid option" + END)

    def start_game(self):
        """The beginning of the program."""

        while self.playing:
            self.display()

            choice = self.get_choice_from_user("Choice: ")
            self.handle_choice(choice)

    def player_playing(self, current_player):
        """The logic for when the player is playing."""

        die = dice.Dice()
        score = current_player.get_total_score()  # Getting score from the player
        game_is_being_played = True
        while game_is_being_played:
            print(current_player.get_name() + " you currently have " + str(score) + " point(s)")

            choice = self.get_choice_from_user(current_player.get_name() + " what do you want to do?:\nPress 1 to toss\nPress 2 to stay\nPress 3 to change name\nPress 4 to surrender\nChoice: ")

            if choice == 1:
                die_value = current_player.throw_dice(die)
                print(current_player.get_name() + " got a " + str(die_value))
                if die_value != 1:
                    score += die_value
                    game_is_being_played = self.check_if_winner(score, current_player)
                    continue
                else:
                    print("Oh you got a " + str(die_value) + " better luck next time\n")
                    game_is_being_played = False
                    return True

            elif choice == 2:
                current_player.set_total_score(score)
                self.players[current_player.get_name()] = current_player.get_total_score()
                current_points = current_player.get_total_score()
                print(current_player.get_name() + " stayed and now have " + str(current_points) + " point(s)\n")
                game_is_being_played = False
                return True

            elif choice == 3:
                old_name = current_player.get_name()
                value = self.players.pop(old_name)
                new_name = self.change_name(current_player)
                new_key = new_name
                self.players[new_key] = value

                print("Your new name is now " + new_name)

            elif choice == 4:
                return False

            elif choice == 1337:
                current_player.set_total_score(100)
                game_is_being_played = self.check_if_winner(100, current_player)
            else:
                print(RED + "That's not an option" + END)
        return False

    def computer_playing(self, computer):
        """The logic for when the computer is playing."""

        die = dice.Dice()
        score = computer.get_total_score()  # Getting score from the computer
        game_is_being_played = True
        toss_counter = 0 # something with the first toss is 100% toss then i change weight based on how many toss
        while game_is_being_played:
            print("Computer currently have " + str(score) + " point(s)")

            decision = computer.difficulty_choice(toss_counter, score)

            if decision == "toss":
                die_value = computer.throw_dice(die)
                print("Computer got a " + str(die_value))
                if die_value != 1:
                    score += die_value
                    game_is_being_played = self.check_if_winner(score)
                    continue
                else:
                    print("Oh you got a " + str(die_value) + " better luck next time\n")
                    game_is_being_played = False
                    return True

            elif decision == "stay":
                computer.set_total_score(score)
                current_points = computer.get_total_score()
                print("Computer stayed and now have " + str(current_points) + " point(s)\n")
                game_is_being_played = False
                return True

            else:
                print("Invalid option!")  # Can make this print in red
        return False

    def check_if_winner(self, score, current_player):
        """Checks if the current toss is enough to win."""
        
        post_winner = highscore.Highscore()

        if score >= 100:
            print("You won in " + str(current_player.get_tossed_amount()) + " throws!")  # can make this green
            current_player.set_total_score(score)
            self.players[current_player.get_name()] = current_player.get_total_score()
            post_winner.add_winner(current_player.get_name())
            return False
        else:
            return True

    def get_player_score(self, player_name):
        """To get the players score, this is used for easier testing if the score got updated."""

        if player_name in self.players:
            return self.players[player_name]
        else:
            return None

    def change_name(self, current_player):
        """Sets a new name for the player."""

        new_name = input("Input new name: ")
        current_player.set_name(new_name)

        return new_name

    def setup_player(self):
        """Sets up the player."""

        player_name = input("What is your name? ")
        new_player = player.Player(player_name)
        self.players[player_name] = new_player.get_total_score()

        return new_player

    def game_rules(self):
        """Displays the rules of the game."""

        print("""\nEach turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to "hold":

If the player rolls a 1, they score nothing and it becomes the next player's turn.
If the player rolls any other number, it is added to their turn total and the player's turn continues.
If a player chooses to "hold", their turn total is added to their score, and it becomes the next player's turn.
The first player to score 100 or more points wins\n""")
