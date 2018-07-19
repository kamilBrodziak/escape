import random
import os
import sys


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


class GameStart:
    def __init__(self):
        self.new_game()

    def new_game(self):
        self.board_id = [i for i in range(9)]
        self.board = [""] * 9
        self.actual_pos = 0
        self.win = ""

    def run(self):
        while self.win not in {True, False}:
            cls()
            self.make_move()
            self.check_result()
            if self.win in {True, False}:
                break
            self.opponent_move()
            self.check_result()

    def make_move(self):
        char = ""
        while char != '\n':
            cls()
            self.print_board()
            char = getChar(1)
            if char == '\x1b':
                char = getChar(2)
                if char == '[A' and self.actual_pos > 2:
                    if self.actual_pos - 3 in self.board_id:
                        self.actual_pos -= 3
                    elif self.actual_pos - 6 in self.board_id:
                        self.actual_pos -= 6
                elif char == '[B' and self.actual_pos < 6:
                    if self.actual_pos + 3 in self.board_id:
                        self.actual_pos += 3
                    elif self.actual_pos + 6 in self.board_id:
                        self.actual_pos += 6
                elif char == '[C' and self.actual_pos < 8:
                    copy_pos = self.actual_pos
                    while copy_pos < 8:
                        copy_pos += 1
                        if copy_pos in self.board_id:
                            self.actual_pos = copy_pos
                            break
                elif char == '[D' and self.actual_pos > 0:
                    copy_pos = self.actual_pos
                    while copy_pos > 0:
                        copy_pos -= 1
                        if copy_pos in self.board_id:
                            self.actual_pos = copy_pos
                            break
        del self.board_id[self.board_id.index(self.actual_pos)]
        self.board[self.actual_pos] = "X"

    def opponent_move(self):
        choice = random.choice(self.board_id)
        self.board[choice] = 'O'
        del self.board_id[self.board_id.index(choice)]
        self.print_board()

    def check_result(self):
        result = {'X': True, 'O': False}
        b = self.board
        matches = [[b[0], b[4], b[8]], [b[2], b[4], b[6]],
                    [b[0], b[3], b[6]], [b[1], b[4], b[7]], [b[2], b[5], b[8]],
                    [b[0], b[1], b[2]], [b[3], b[4], b[5]], [b[6], b[7], b[8]]]
        for key in result:
            match = [key, key, key]
            if match in matches:
                self.win = result[key]
        if len(self.board) == 0:
            self.win = False
    
    def print_board(self):
        empty = "          \n          \n          \n          \n          \n          \n          \n          ".split("\n")
        x = "XX      XX\n XX    XX \n  XX  XX  \n   XXXX   \n   XXXX   \n  XX  XX  \n XX    XX \nXX      XX".split("\n")
        o = "  OOOOOO  \n OO    OO \nOO      OO\nOO      OO\nOO      OO\nOO      OO\n OO    OO \n  OOOOOO  ".split('\n')
        what_in_row = {'': empty, 'X': x, 'O': o}
        for i in range(0, 7, 3):
            sequence = [what_in_row[self.board[i]], what_in_row[self.board[i+1]], what_in_row[self.board[i+2]]]
            if self.actual_pos in {i, i+1, i+2}:
                sequence[self.actual_pos % 3] = what_in_row['X']
            for row in zip(sequence[0], sequence[1], sequence[2]):
                print(row[0], row[1], row[2], sep=" | ")
            print('-' * 36)