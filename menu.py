import ui
from common import getChar, arrows_move_menu, char_create
import highscores
import common, game


def choose(option):
    options_amount = 4
    while True:
        ui.print_menu("MAIN MENU", "main", option)
        char = getChar(1)

        if char == '\x1b':  # arrows movement in menu
            char = getChar(2)
            option = arrows_move_menu(option, options_amount, '[A', '[B', char)
        
        # moving in menu by pressing numbers on keyboard
        elif char.isdigit() and int(char) > 0 and int(char) < options_amount + 1:
            option = int(char)
        
        # choosing an option by enter
        elif char == '\n':
            if option == 1:
                common.char_create()
                game.main()

            elif option == 2:
                highscores.highscore_show()

            elif option == 3:
                pass

            elif option == 4:
                exit()


def main():
    starting_position = 1  # on what option we want to have a cursor after start main.py
    choose(starting_position)


if __name__ == '__main__':
    main()