from common import print_back_to_menu, getChar

def loading_highscore_file_into_list():
    highscore_list = []
    with open('highscores.txt', 'r') as highscores:
        for line in highscores:
            one_score = line.split(" ", )
            if line != "" and line != '\n' and line != " ":
                highscore_list.append(one_score)
    return highscore_list


def highscore_add(name, score):
    highscore_add_to_highscore_list(name, score)
    add_highscore_to_file(name, score)


def highscore_add_to_highscore_list(nick, points):
    highscore_list = loading_highscore_file_into_list()
    highscore_list.append(
        (nick, int(points)))
    sorted_highscore_list = sorted(highscore_list, key=lambda x: float(x[1]))
    if len(sorted_highscore_list) > 10:
        sorted_highscore_list = sorted_highscore_list[:-1]
    return sorted_highscore_list


def add_highscore_to_file(nick, points):
    sorted_highscore_list = highscore_add_to_highscore_list(
        nick, points)
    with open('highscores.txt', 'w') as highscores:
        for i in sorted_highscore_list:
            line = i[0] + " " + str(i[1])
            highscores.write(line + '\n')


def highscore_show():
    print("---PLACE-----NICK-------------SCORE-----\n")
    sorted_highscores = loading_highscore_file_into_list()
    place_nr = 1
    for result in sorted_highscores:
        print(3 * " " + str(place_nr) + "." + (7 - len(str(place_nr))) * " " + result[0] +
              (19 - len(result[0])) * " " + str(round(float(result[1]), 3)))
        place_nr += 1
    print(" " + 79 * "_")
    return print_back_to_menu()

    