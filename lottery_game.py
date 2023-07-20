import time
import random
import string
import enum

moves = ["rock", "paper", "scissors"]


class Color(enum.Enum):
    red = "\033[91m"
    purple = "\033[95m"
    blue = "\033[94m"
    cyan = "\033[96m"
    green = "\033[92m"
    orange = "\033[33m"
    yellow = "\033[93m"
    bold = "\033[1m"
    underline = "\033[4m"
    black = "\033[0m"

    @classmethod
    def get_color(cls):
        return random.choice([color.value for color in cls])


class Player:
    @classmethod
    def move(self):
        return "rock"

    @classmethod
    def learn(self, my_move, their_move):
        print("learn player")
        pass

    @classmethod
    def beats(one, two):
        return (
            (one == "rock" and two == "scissors")
            or (one == "scissors" and two == "paper")
            or (one == "paper" and two == "rock")
        )

    @classmethod
    def typewriter_simulator(message):
        for char in message:
            print(char, end="")
            if char in string.punctuation:
                time.sleep(0.5)
            time.sleep(0.03)

    print("")

    @classmethod
    def print_pause(statment_printer, delye=2):
        # this is a function to puse a masge
        print(Color.get_color() + statment_printer)
        time.sleep(delye)

    @classmethod
    def input_choise(self):
        while True:
            option = input(
                "Please choose one of the options:"
                "Please check 1-rock 2-paper 3-scissors\n"
            )
            if option in moves:
                return option
            print(f"Option {option} is invalid. Try again!")

    @classmethod
    def description(self):
        # this is a func use a puse a masge to description player
        self.print_pause(
            "Welcome to the Rock Paper Scissors game."
            "Thank you for choosing.\n", 2
        )

        self.print_pause(
            "Now you have reached the Rock Paper Scissors game."
            "There are three basic options in the game."
            "Basic options for playing it .\n", 1)
        self.print_pause('The 3 basic options are'
                         "1-rock 2-paper 3-scissors.\n", 2)


class RandomPlayer(Player):

    print("ff")
    print("hi im class randomplayer")

    @classmethod
    def learn(self, my_move, their_move):
        print("learn random")
        pass

    def move(self):
        option = random.choice(moves)
        return option


class HumanPlayer(Player):
    print("hi im class humanplayer")

    def move(self):
        option = ""
        option = self.input_choise()
        return option


class ReflectPlayer(Player):
    print("hi im class reflectplayer")

    def move(self):
        return game.p1.move


class CyclePlayer(Player):
    print("hi im class cycleplayer")

    def move(self):

        while self.round == 0:
            self.round += 1
            return RandomPlayer.move(self)

        try:
            return moves[moves.index(self.move) + 1]

        except IndexError:
            return moves[0]


class Game:
    countcomputer = 0
    countperson = 0

    def __init__(self, human, random):
        self.p1 = human
        self.p2 = random

    def play_round(self):
        computer = self.p2.move()
        print("this is a random choise =:", self.p2.move())
        player = self.p1.move()

        print(f"Player 1: {player}  Player 2: {computer}")
        self.p1.learn(player, computer)
        self.p2.learn(computer, player)
        self.checke(player, computer)

    def checke(self, player, computer):

        print("basil checker")

        if player == computer:
            print("Tie!")
        elif player == "rock":
            if computer == "paper":
                print("You lose!", computer, "covers", player)
                self.countcomputer += 1

            else:
                print("You win!", player, "smashes", computer)
                self.countperson += 1
        elif player == "paper":
            if computer == "scissors":
                print("You lose!", computer, "cut", player)
                self.countcomputer += 1
            else:
                print("You win!", player, "covers", computer)
                self.countperson += 1
        elif player == "scissors":
            if computer == "rock":
                print("You lose...", computer, "smashes", player)
                self.countcomputer += 1
            else:
                print("You win!", player, "cut", computer)
                self.countperson += 1
        else:
            print("That's not a valid play. Check your spelling!")

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print("-----------------")
            print(f"Round {round}:")
            self.play_round()
            # self.checke()
        print("count palyer computer :", self.countcomputer)
        print("count palyer human :", self.countperson)
        if self.countcomputer > self.countperson:
            print("the computer wine !")
            print(
                f"""Final \nPlayer One Points: {self.countperson} """
                f""" Player Two Points: {self.countcomputer}"""
            )

        else:
            print("the human wine !")
            print(
                f"""Final \nPlayer One Points: {self.countperson} """
                f""" Player Two Points: {self.countcomputer}"""
            )


if __name__ == "__main__":

    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
    print("________________________new palayer_______________________")
