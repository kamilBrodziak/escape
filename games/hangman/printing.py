import os
import sys
import time
from termcolor import colored, cprint


def cls():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def printing_hangman(lifes, letters):
    print("Your lifes: ", end="")
    if lifes < 0:
        lifes = 0
    cprint((chr(9829) + " ") * lifes, 'red', attrs=['bold'])
    print("------------------------------------------------------\n")
    with open("games/hangman/ascii/" + str(lifes) + '.txt', 'r') as file:
        if lifes > 4:
            cprint(file.read(), 'green', attrs=['bold'])
        elif lifes > 2 and lifes < 5:
            cprint(file.read(), 'yellow', attrs=['bold'])
        elif (lifes < 3 and lifes > 1) or lifes < 1:
            cprint(file.read(), 'red', attrs=['bold'])
        elif lifes == 1:
            cprint(file.read(), 'red', attrs=['bold', 'blink'])
    print("Used letters: ", letters)


def display_hint(country):
    print("Capital of " + country)


def display_test_hint(capital):
    print("Debug mode,  capital: " + capital)


def used_letter_before():
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[F")
    print("You used that letter before, give me another one!")


def printing_hint_and_capital(capital_display_on_screen, cou_cap, life, hint):
    if life == 1:
        display_hint(cou_cap[0])
        if hint:
            display_test_hint(cou_cap[1])
    print("".join(capital_display_on_screen))
    print("------------------------------------------------------\n")
