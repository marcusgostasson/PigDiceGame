#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from . import player
from . import computer
from . import dice
import random
# Did we put a licence when we created the repository?


class Game:
    def __init__(self):
        self.playing = True
        self.players = {}

    def display(self):
        print("""Hello and welcome to Pig Dice Game
Press 1 if you want to play with a friend
Press 2 if you want to play vs the computer
Press 3 if you want to see the rules for the game
Press 4 if you want to quit""")

    def get_choice_from_user(self, prompting):
        while (True):
            try:
                choice = int(input(prompting))
                if choice in [1, 2, 3, 4]:
                    return choice
                else:
                    print("Invalid choice. Enter a number between 1 and 4")
            except ValueError:
                raise ValueError("Invalid input. That is not a number")

    def player_vs_player(self):
        player1 = self.setup_player()
        player2 = self.setup_player()
        playing = True
        while (playing):
            playing = self.player_playing(player1)
            if (playing is False and player1.get_total_score() < 100):
                print(player1.get_name() + " surrendered and " + player2.get_name() + " won")
            elif (playing is True):
                playing = self.player_playing(player2)
                if (playing is False and player2.get_total_score() < 100):
                    print(player2.get_name() + " surrendered and " + player1.get_name() + " won")

    def player_vs_computer(self):
        player_name = input("What is your name? ")
        player1 = player.Player(player_name)
        difficulty = self.get_choice_from_user("""What difficulty do you want?
1. Playing against a new born baby
2. Playing against my uncle that is pretty good with numbers
3. Playing against Pelle, if you know you know
4. Completly random no logic""")
        computer = computer.Computer(difficulty)
        playing = True
        while (playing):
            playing = self.player_playing(player1)
            if (playing is True):
                playing = self.computer_playing(computer)

    def quit(self):
        print("Quit out of the game")
        self.playing = False

    def handle_choice(self, choice):
        if (choice == 1):
            self.player_vs_player()
        elif (choice == 2):
            self.player_vs_computer()
        elif (choice == 3):
            self.game_rules()
        else:
            self.quit()

    def start_game(self):
        while (self.playing):
            self.display()

            choice = self.get_choice_from_user("Choice: ")
            self.handle_choice(choice)

    def player_playing(self, current_player):
        die = dice.Dice()
        score = current_player.get_total_score()  # Getting score from the player
        game_is_being_played = True
        while (game_is_being_played):
            print(current_player.get_name() + " you currently have " + str(score) + " point(s)")
            choice = self.get_choice_from_user(current_player.get_name() + " what do you want to do?:\nPress 1 to toss\nPress 2 to stay\nPress 3 to change name\nPress 4 to surrender\nChoice: ")

            if (choice == 1):
                dieValue = current_player.throw_dice(die)
                print(current_player.get_name() + " got a " + str(dieValue))
                if (dieValue != 1):
                    score += dieValue
                    game_is_being_played = self.check_if_winner(score, current_player)
                    continue
                else:
                    print("Oh you got a " + str(dieValue) + " better luck next time\n")
                    game_is_being_played = False
                    return True

            elif (choice == 2):
                current_player.set_total_score(score)
                self.players[current_player.get_name()] = current_player.get_total_score()
                currentPoints = current_player.get_total_score()
                print(current_player.get_name() + " stayed and now have " + str(currentPoints) + " point(s)\n")
                game_is_being_played = False
                return True

            elif (choice == 3):
                old_name = current_player.get_name()
                value = self.players.pop(old_name)
                new_name = self.change_name(current_player)
                new_key = new_name
                self.players[new_key] = value

                print("Your new name is now " + new_name)

            elif (choice == 4):
                return False

            else:
                print("Invalid option!")  # Can make this print in red
        return False

    def computer_playing(self, computer):
        die = dice.Dice()
        difficulty = computer.get_difficulty()
        score = computer.get_total_score()  # Getting score from the computer
        game_is_being_played = True
        options = ["toss", "stay"]
        tossCounter = 0 # something with the first toss is 100% toss then i change weight based on how many toss
        while (game_is_being_played):
            print(computer.get_name() + " you currently have " + str(score) + " point(s)")
            pick = random.choices(options, weights=difficulty) # Problem can be with logic to stay at 20 because now the logic is weight based

            choice = pick
            if (choice == "toss"):
                dieValue = computer.throw_dice(die)
                print(computer.get_name() + " got a " + str(dieValue))
                if (dieValue != 1):
                    score += dieValue
                    game_is_being_played = self.check_if_winner(score)
                    continue
                else:
                    print("Oh you got a " + str(dieValue) + " better luck next time\n")
                    game_is_being_played = False
                    return True

            elif (choice == "stay"):
                computer.set_total_score(score)
                current_points = computer.get_total_score()
                print(computer.get_name() + " stayed and now have " + str(current_points) + " point(s)\n")
                game_is_being_played = False
                return True

            else:
                print("Invalid option!")  # Can make this print in red
        return False

    def check_if_winner(self, score, current_player):
        if (score >= 100):
            print("You won in " + str(current_player.get_tossed_amount()) + " throws!")  # can make this green
            current_player.set_total_score(score)
            return False
        else:
            return True

    def get_player_score(self, player_name):
        if (player_name in self.players):
            return self.players[player_name]
        else:
            return None

    def change_name(self, current_player):
        new_name = input("Input new name: ")
        current_player.set_name(new_name)

        return new_name

    def setup_player(self):
        player_name = input("What is your name? ")
        new_player = player.Player(player_name)
        self.players[player_name] = new_player.get_total_score()

        return new_player

    def game_rules(self):
        print("""\nEach turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to "hold":

If the player rolls a 1, they score nothing and it becomes the next player's turn.
If the player rolls any other number, it is added to their turn total and the player's turn continues.
If a player chooses to "hold", their turn total is added to their score, and it becomes the next player's turn.
The first player to score 100 or more points wins\n""")
