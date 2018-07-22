from common import print_back_to_menu, getChar, Printing, cls


def loading_highscore_file_into_list():
    with open('highscores.txt', 'r') as highscores:
        highscores_list = highscores.readlines()
    for i, score in enumerate(highscores_list):
        score = score[:-1].split(" ")
        score[1] = int(score[1])
        highscores_list[i] = score
    return highscores_list


def highscore_add(name, score):
    highscore_add_to_highscore_list(name, score)
    add_highscore_to_file(name, score)


def highscore_add_to_highscore_list(nick, points):
    highscore_list = loading_highscore_file_into_list()
    highscore_list.append((nick, int(points)))
    sorted_highscore_list = sorted(highscore_list, key=lambda x: int(x[1]), reverse=True)
    return sorted_highscore_list[0:10]


def add_highscore_to_file(nick, points):
    sorted_highscore_list = highscore_add_to_highscore_list(nick, points)
    string = ""
    for i in sorted_highscore_list:
        string += i[0] + " " + str(i[1]) + "\n"
    with open('highscores.txt', 'w') as highscores:
        highscores.write(string)


def highscore_show():
    cls()
    printing = Printing([10, 30, 40], 82, "TOP 10")
    printing.print_title()
    printing.print_row(['PLACE', 'NAME', 'SCORE'], header=True, decors=False)
    add_highscore_to_file('fer', 2080)
    sorted_highscores = loading_highscore_file_into_list()

    for i, result in enumerate(sorted_highscores):
        printing.print_row([i+1] + result, decors=False)

    print("\\" + 82 * "_" + "/")
    return print_back_to_menu()
