def print_menu (title, which_menu, option, func1="", func2=""):
    with open("menu/" + which_menu + str(option) + '.txt', 'r') as option:
        option = option.read()

    if which_menu == "menu" :
        option = option.replace(r"{}", func1.center(32), 1).replace(r"{}", func2.center(32), 1)

    print(option)


def char_create():
    char_info = []
    