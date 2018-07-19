import os

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


def arrows_move(option, max_, key1, key2, char, value_change=1, min_=1):  # moving in menu
    if char == key1:
        if option > min_:
            option -= value_change

    elif char == key2:
        if option < max_:
            option += value_change

    return option


def cls():  # clearing screen in terminal
        os.system("clear")

def char_create ():
    nick = input ("Enter your nick: \n")
    gender = input ("Male / Female \n")
    if gender == 'Male' or gender == 'Female' or gender == 'male' or gender == 'female':
        char_info = [nick, gender]

    else :
        print ('Invalid gender!')
        return char_create()
    cls()
    print (char_info)


def print_back_to_menu():
    with open("back.txt") as back_menu:
        print(back_menu.read())

