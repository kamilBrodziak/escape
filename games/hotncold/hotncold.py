import random
import sys
import os
import time


def cls():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


class HotCold:
    def __init__(self):
        self.run()

    def run(self):
        self.hits = 5
        self.random_numb = random.randint(1, 10)
        self.print_start()
        self.win = self.input_anw()

    def print_start(self):
        cls()
        print("/" + "-" * 60 + "\\")
        print("|" + 60 * " " + "|")
        string = 'Hot n Cold game'
        print("|" + string.center(60, " ") + "|")
        print("|" + 60 * "_" + "|")
        string = 'Try to guess random number from 1 to 10'
        print(string)

    def input_anw(self):
        while self.hits > 0:
            answ = int(input('Give me you answer: '))
            self.hits -= 1
            if answ > self.random_numb:
                print("Too high, you have", self.hits, "tries left!")
            elif answ < self.random_numb:
                print("To low, you have", self.hits, "tries left!")
            elif answ == self.random_numb:
                print("You won and moved to next level!!")
                time.sleep(2)
                self.win = True
                return
        print("You lost, you stay in this level!")
        time.sleep(2)
        self.win = False