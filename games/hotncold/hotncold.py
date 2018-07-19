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
        self.win = False
        self.hits = 5

    def run(self):
        self.random_numb = random.randint(1, 10)
        self.print_start()
        self.input_anw()

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
        hits = self.hits
        while hits > 0:
            answ = int(input('Give me you answer: '))
            hits -= 1
            if not answ.isdigit():
                print('That\'s not number! ')
            if answ > self.random_numb:
                print("Too high, you have", hits, "tries left!")
            elif answ < self.random_numb:
                print("To low, you have", hits, "tries left!")
            elif answ == self.random_numb:
                print("You won and moved to next level!!")
                time.sleep(3)
                self.win = True
                return
        print("You lost, you stay in this level!")
        time.sleep(3)
        self.win = False
