import os
import sys
from termcolor import cprint, colored


class Printing:
    def __init__(self, col_lengths, table_length, title):
        self.col_lengths = col_lengths
        self.table_length = table_length
        self.title = title

    def print_title(self):
        cprint("/" + self.table_length * "-" + "\\", 'white', 'on_grey', attrs=['bold'])
        cprint("|" + self.table_length * " " + "|", 'white', 'on_grey', attrs=['bold'])
        cprint("|" + self.title.center(self.table_length, " ") + "|", 'white', 'on_grey', attrs=['bold'])
        cprint("|" + self.table_length * "_" + "|", 'white', 'on_grey', attrs=['bold'])

    def print_row(self, row, fillchar=" ", header=False):
        col_amount = len(row)
        self.print_decor_cells(fillchar, col_amount)
        if header:
            cprint("|", "white", "on_grey", attrs=['bold'], end="")
        else:
            print("|", end="")

        for i, el in enumerate(row):
            if header:
                cprint((" " + str(el) + " ").center(self.col_lengths[i], fillchar) + "|", "white", "on_grey",
                       attrs=["bold"], end="")
            else:
                cprint((" " + str(el) + " ").center(self.col_lengths[i], fillchar) + "|", end="")

        print("")
        self.print_decor_cells(fillchar, col_amount)
        self.print_decor_cells("-", col_amount)

    def print_decor_cells(self, fillchar, length):
        cprint("|", "grey", "on_white", attrs=['bold'], end="")
        for i in range(length):
            cprint(fillchar * self.col_lengths[i] + "|", "grey", "on_white", attrs=['bold'], end="")
        print("")


def getChar(bits):  # get tke pressed key from user
    try:
        import msvcrt
        return msvcrt.getch()

    except ImportError:
        import tty
        import sys
        import termios
        fd = sys.stdin.fileno()
        oldSettings = termios.tcgetattr(fd)

        try:
            tty.setcbreak(fd)
            answer = sys.stdin.read(bits)

        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, oldSettings)

        return answer


def arrows_move_menu(option, max_, key1, key2, char, value_change=1, min_=1):  # moving in menu
    if char == key1:
        if option > min_:
            option -= value_change

    elif char == key2:
        if option < max_:
            option += value_change

    return option


def cls():  # clearing screen in terminal
        os.system("clear")


def print_back_to_menu():
    with open("ascii/back.txt") as back_menu:
        print(back_menu.read())
    char = ""
    while char != "\n":
        char = getChar(1)
        if char == '\x1b':
            getChar(2)
