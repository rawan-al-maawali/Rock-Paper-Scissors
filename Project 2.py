#!/usr/bin/env python3
import random
import colorama
from colorama import init, Fore, Back, Style
init(convert=True)

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']


"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        entry = input("Choose: rock / paper /scissors?")
        while entry.lower() not in moves:
            entry = input("Choose: rock / paper /scissors?")
        return entry.lower()


class ReflectPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.their_move = None

    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.my_move = None

    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        else:
            index = moves.index(self.my_move)
        if index == len(moves)-1:
            index = 0
        else:
            index += 1
        return moves[index]

    def learn(self, my_move, their_move):
        self.my_move = my_move


def beats(one, two):
    if ((one == 'rock' and two == 'scissors') or
       (one == 'scissors' and two == 'paper') or
       (one == 'paper' and two == 'rock')):
        return True
    elif ((one == 'scissors' and two == 'rock') or
          (one == 'paper' and two == 'scissors') or
          (one == 'rock' and two == 'paper')):
        return False
    else:
        return "Tie"


class Game:

    def __init__(self, p1, p2, count1, count2):
        self.p1 = p1
        self.p2 = p2
        self.count1 = count1
        self.count2 = count2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}, Player 2: {move2} ")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        if beats(move1, move2) is True:
            self.count1 += 1
            print("\033[1;41mPlayer 1 wins!\033[1;m")
            print("\033[1;46mScore - ", end="")
            print(f"Player 1: {self.count1}\033[1;m", end=" ")
            print(f"\033[1;46mPlayer2: {self.count2}\033[1;m")
        elif beats(move1, move2) is False:
            self.count2 += 1
            print("\033[1;41mPlayer 2 wins!\033[1;m")
            print("\033[1;46mScore - ", end="")
            print(f"Player 1: {self.count1}\033[1;m", end=" ")
            print(f"\033[1;46mPlayer2: {self.count2}\033[1;m")
        else:
            print("\033[1;41mTie!\033[1;m")
            print("\033[1;46mScore - ", end="")
            print(f"Player 1: {self.count1}\033[1;m", end=" ")
            print(f"\033[1;46mPlayer2: {self.count2}\033[1;m")

    def play_game(self):
        print("Game start!")
        rounds = input("Enter the number of rounds: ")

        def check_string(s):
            try:
                int(s)
            except ValueError:
                return False
        while check_string(rounds) is False:
            rounds = input("Enter the number of rounds in integers please: ")
            check_string(rounds)
        rounds = int(rounds)
        for round in range(rounds):
            round += 1
            print(f"\033[1;45mRound {round}:\033[1;m")
            self.play_round()

        for n in range(5):
            print("*"*10)

        if self.count1 > self.count2:
            print("The winner is: player 1")
        elif self.count1 < self.count2:
            print("The winner is: player 2")
        else:
            print("It is a tie!")

        print("Game over!")


if __name__ == '__main__':
    options = ["a", "b", "c"]
    print("Choose your opponent: ")
    opponent = input(
        "(a)Random Player, (b)Cycle Player, (c)Reflect Player : "
    )
    while opponent.lower() not in options:
        print("Please choose a or b or c")
        opponent = input(
            "a:Random Player, b:Cycle Player, c:Reflect Player"
        )
    if opponent.lower() == "a":
        opponent = RandomPlayer()
    elif opponent.lower() == "b":
        opponent = CyclePlayer()
    else:
        opponent = ReflectPlayer()
    game = Game(HumanPlayer(), opponent, 0, 0)
    game.play_game()
