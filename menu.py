from highscores import highscore_show
from game import game_start
from common import cls, Printing, print_back_to_menu
from credit import credit


class PrintingMenu:
    def __init__(self, menu_title, menu_options, menu_width, actual_pos):
        self.menu_title = menu_title
        self.menu_options = menu_options
        self.menu_indentation = 10
        self.option_indendation = 8
        self.chosen_option_indendation = 6
        self.menu_width = menu_width
        self.option_width = menu_width - 2 * self.option_indendation
        self.chosen_option_width = menu_width - 2 * self.chosen_option_indendation
        self.actual_pos = actual_pos

    def change_option(self, new_pos):
        self.actual_pos = new_pos

    def print_menu(self):
        self.cls()
        self.print_title()
        self.print_options()
        self.print_footer()

    def print_title(self):
        self.print_cell(self.menu_indentation, self.menu_width, "█", self.menu_title)

    def print_cell(self, indendation, width, fillchar, title):
        print((indendation + 1) * " " + width * "_")
        print(indendation * " " + fillchar + width * " " + fillchar)
        print(indendation * " " + fillchar + (" " + title + " ").center(width, " ") + fillchar)
        print(indendation * " " + fillchar + width * "_" + fillchar)

    def print_options(self):
        for i, option in enumerate(self.menu_options):
            self.print_option(option[0], i)

    def print_option(self, option, i):
        if self.actual_pos == i:
            width = self.chosen_option_width
            indendation = self.chosen_option_indendation + self.menu_indentation
            fillchar = "█"
        else:
            width = self.option_width
            indendation = self.option_indendation + self.menu_indentation
            fillchar = "|"
        self.print_cell(indendation, width, fillchar, option)

    def print_footer(self):
        print(self.menu_indentation * " " + "_" * self.menu_width)

    def cls(self):  # clearing screen in terminal
        import os
        os.system("clear")


class Menu:
    def __init__(self, title, menu_width, menu_options):
        self.actual_pos = 0
        self.menu_options = menu_options  # list of lists, el[0] - name, el[1] - function name
        self.display = PrintingMenu(title, menu_options, menu_width, self.actual_pos)

    def run_menu(self):
        while True:
            self.display.print_menu()
            self.getChar(1)
            if self.char == "\x1b":
                self.getChar(2)
                self.arrows_move()
            elif self.char == "\n":
                self.menu_options[self.actual_pos][1]()

    def arrows_move(self):
        if self.char == '[A' and self.actual_pos > 0:
            self.actual_pos -= 1
        elif self.char == '[B' and self.actual_pos < len(self.menu_options) - 1:
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
    menu_width = 50
    menu_title = 'Menu'
    menu_options = [['New game', game_start], ['Highscores', highscore_show],
                    ['Credits & Info', credit], ['Exit', exit]]
    menu = Menu(menu_title, menu_width, menu_options)
    menu.run_menu()


if __name__ == '__main__':
    main()
