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

    def get_color(cls):
        return random.choice([color.value for color in cls])


class Player:

    def move(self):
        return "rock"

    def learn(self, my_move, their_move):
        print("learn player")
        pass

    def beats(self, one, two):
        return (
            (one == "rock" and two == "scissors")
            or (one == "scissors" and two == "paper")
            or (one == "paper" and two == "rock")
        )

    def typewriter_simulator(self, message):
        for char in message:
            print(char, end="")
            if char in string.punctuation:
                time.sleep(0.5)
            time.sleep(0.03)

    print("")

    def print_pause(self, statment_printer, delye=2):
        # this is a function to puse a masge
        print(Color.get_color() + statment_printer)
        time.sleep(delye)

    def input_choise(self):
        while True:
            option = input(
                "Please choose one of the options:"
                "Please check 1-rock 2-paper 3-scissors\n"
            ).lower()
            if option in moves:
                return option
            print(f"Option {option} is invalid. Try again!")

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

    def learn(self, my_move, their_move):
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

    def __init__(self):
        Player.__init__(self)
        self.their_move = None

    def learn(self, my_move, their_move):
        self.their_move = their_move

    def move(self):
        if self.their_move is None:
            return (random.choice(moves))
        else:
            return self.their_move


class CyclePlayer(Player):
    print("hi im class cycleplayer")

    def __init__(self):
        Player.__init__(self)
        self.last_move = None

    def move(self):
        move = None
        if self.last_move is None:
            return random.choice(moves)
        else:
            index = moves.index(self.last_move) + 1
            if index >= len(moves):
                index = 0
            move = moves[index]
        self.last_move = move
        return move

    def learn(self, my_move, their_move):
        print("learn CyclePlayer")
        self.last_move = my_move


class Game:
    countcomputer = 0
    countperson = 0
    round = 3

    def __init__(self, human, random):
        self.p1 = human
        self.p2 = random
        self.count_wins = 0
        self.count_losses = 0
        self.count_ties = 0

    def play_round(self):
        computer = self.p2.move()
        print("this is a random choise =:", self.p2.move())
        player = self.p1.move()

        print(f"Player 1: {player}  Player 2: {computer}")
        self.p1.learn(player, computer)
        self.p2.learn(computer, player)

        if self.p1.beats(computer, player):
            self.count_wins += 1
            print(f"wins:{self.count_wins}")
        elif computer == player:
            self.count_ties += 1
            print(f"ties:{self.count_ties}")
        elif self.p2.beats(player, computer):
            self.count_losses += 1
            print(f"losses:{self.count_losses}")
        else:
            print("tada mistake")
        print(f"Player One Score: {self.count_wins}"
              f"Player Two Score: {self.count_losses}\n")

    def play_game(self):
        print("Game start!")
        for round in range(self.round):
            print("-----------------")
            print(f"Round {round}:")
            self.play_round()
            # self.checke()
            print("count palyer computer :", self.count_wins)
            print("count palyer human :", self.count_losses)
        if self.count_wins > self.count_losses:
            print("the computer wine !")
            print(
                f"""Final \nPlayer One Points: {self.count_wins} """
                f""" Player Two Points: {self.count_losses}"""
            )

        else:
            print("the human wine !")
            print(
                f"""Final \nPlayer One Points: {self.count_losses} """
                f""" Player Two Points: {self.count_wins}"""
            )


if __name__ == "__main__":
    print("hallo ")
    strategies = {
      "1": Player(),
      "2": RandomPlayer(),
      "3": CyclePlayer(),
      "4": ReflectPlayer()
    }
    while True:
        opt = input("please enter the option favert run"
                    "round bettwen RandomPlayer and :"
                    "1-Player 2-RandomPlayer 3-CyclePlayer 4-ReflectPlayer:"
                    "if need a exit a program press a number 9:\n"
                    )
        if opt in strategies:
            game = Game(HumanPlayer(), strategies[opt])
            game.play_game()
            print("________________________new palayer_______________________")
        elif opt == "9":
            print("exit a program")
            exit(0)
        else:
            print("please enter viled a choise")
