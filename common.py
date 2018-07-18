import os
import sys
from termcolor import cprint


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
                print((" " + str(el) + " ").center(self.col_lengths[i], fillchar) + "|", end="")

        print("")
        self.print_decor_cells(fillchar, col_amount)
        self.print_decor_cells("-", col_amount)

    def print_decor_cells(self, fillchar, length):
        cprint("|", "grey", "on_white", attrs=['bold'], end="")
        for i in range(length):
            cprint(fillchar * self.col_lengths[i] + "|", "grey", "on_white", attrs=['bold'], end="")
        print("")


def cls():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


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


def arrows_move(posx, posy, char, map_):  # moving in menu/game
    arrows_ud = {"[A": -1, "[B": 1, "[C": 0, "[D": 0}  # up down
    arrows_lr = {"[A": 0, "[B": 0, "[C": 1, "[D": -1}  # left right
    if posx + arrows_lr[char] < 0 or posx + arrows_lr[char] > len(map_.ascii_map[0]) - 1 or \
        posy + arrows_ud[char] < 0 or posy + arrows_ud[char] > len(map_.ascii_map) - 1 or \
            map_.ascii_map[posy + arrows_ud[char]][posx + arrows_lr[char]] == "#":
        return posx, posy
    elif map_.ascii_map[posy + arrows_ud[char]][posx + arrows_lr[char]] == "$":
        pass
    elif map_.ascii_map[posy + arrows_ud[char]][posx + arrows_lr[char]] in {'O', 'G', 'B'}:
        pass
    return posx + arrows_lr[char], posy + arrows_ud[char]