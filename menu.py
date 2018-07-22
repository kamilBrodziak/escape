from highscores import highscore_show
from game import game_start
from common import cls, Printing, print_back_to_menu
from credit import credit


class PrintingMenu:
    def __init__(self, title, options_names, length, actual_pos):
        self.title = title
        self.options_names = options_names
        self.length = length
        self.actual_pos = actual_pos
        self.rs = 10  # amount of spaces from right
        self.diff = 8  # difference of spaces between title and options
        self.change = 2  # difference of chosen option and other options

    def change_option(self, new_pos):
        self.actual_pos = new_pos

    def print_menu(self):
        self.cls()
        self.print_title()
        self.print_options()
        self.print_footer()

    def print_title(self):
        print((self.rs + 1) * " " + self.length * "_")
        print(self.rs * " " + "█" + self.length * " " + "█")
        print(self.rs * " " + "█" + self.title.center(self.length, " ") + "█")
        print(self.rs * " " + "█" + self.length * "_" + "█")

    def print_options(self):
        for i, option in enumerate(self.options_names):
            self.print_option(option, i)

    def print_option(self, option, i):
        if self.actual_pos == i:
            change = self.change
            fillchar = "█"
        else:
            change = 0
            fillchar = "|"
        lchange = self.rs + self.diff - change
        rchange = self.diff * 2 - 2 * change
        print((lchange + 1) * " " + (self.length - rchange) * "_")
        print(lchange * " " + fillchar + (self.length - rchange) * " " + fillchar)
        print(lchange * " " + fillchar + (" " + option + " ").center(self.length - rchange, " ") + fillchar)
        print(lchange * " " + fillchar + (self.length - rchange) * "_" + fillchar)

    def print_footer(self):
        print(self.rs * " " + "_" * self.length)

    def cls(self):  # clearing screen in terminal
        import os
        os.system("clear")


class Menu:
    def __init__(self, title, options_names, length, functions):
        self.actual_pos = 0
        self.options_names = options_names
        self.display = PrintingMenu(title, options_names, length, self.actual_pos)
        self.functions = functions

    def run_menu(self):
        while True:
            self.display.print_menu()
            self.getChar(1)
            if self.char == "\x1b":
                self.getChar(2)
                self.arrows_move()
            elif self.char == "\n":
                self.functions[self.actual_pos]()

    def arrows_move(self):
        if self.char == '[A' and self.actual_pos > 0:
            self.actual_pos -= 1
        elif self.char == '[B' and self.actual_pos < len(self.options_names) - 1:
            self.actual_pos += 1
        self.display.change_option(self.actual_pos)

    def getChar(self, bits):  # get the pressed key from user
        try:
            import msvcrt
            self.char = msvcrt.getch()
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
            self.char = answer


def main():
    functions = [game_start, highscore_show, credit, exit]
    menu = Menu("MENU", ['New game', 'Highscores', 'Credits & Info', 'Exit Game'], 50, functions)
    menu.run_menu()


if __name__ == '__main__':
    main()
