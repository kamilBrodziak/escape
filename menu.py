from common import getChar, arrows_move_menu, cls
import highscores
from game import Gamestart


def choose(option):
    options_amount = 4
    while True:
        print_menu("MAIN MENU", "main", option)
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
                game = Gamestart()
                game.run_game()

            elif option == 2:
                highscores.highscore_show()

            elif option == 3:
                pass

            elif option == 4:
                exit()


def print_menu (title, which_menu, option, func1="", func2=""):
    cls ()
    with open("menu/" + which_menu + str(option) + '.txt', 'r') as option:
        option = option.read()

    if which_menu == "menu" :
        option = option.replace(r"{}", func1.center(32), 1).replace(r"{}", func2.center(32), 1)

    print(option)



def main():
    starting_position = 1  # on what option we want to have a cursor after start main.py
    choose(starting_position)


if __name__ == '__main__':
    main()