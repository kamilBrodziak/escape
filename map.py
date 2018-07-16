import sys
import os


def cls():  # clearing screen in terminal
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


class Map:
    def __init__(self, radius, filename):
        self.radius = radius
        with open(filename) as mapfile:
            self.map = mapfile.read().splitlines()

    def change_radius(new_radius):
        self.radius = new_radius

    def map_load(self, posx, posy):
        radiusx_start = posx - 2 * self.radius if posx - 2 * self.radius >= 0 else 0
        radiusx_end = posx + 2 * self.radius if posx + 2 * self.radius <= len(self.map[0]) else len(self.map[0])
        radiusy_start = posy - self.radius if posy - self.radius >= 0 else 0
        radiusy_end = posy + self.radius if posy + self.radius <= len(self.map) else len(self.map)
        map_copy = self.map[:]
        map_copy[posy] = list(map_copy[posy])
        map_copy[posy][posx] = "@"
        map_copy[posy] = "".join(map_copy[posy])
        new_map = ""
        for i in range(radiusy_start, radiusy_end):
            new_map += 10 * " " + "|" + str(map_copy[i][radiusx_start:radiusx_end]) + "|\n"
        self.map_show = new_map

    def __str__(self):
        return self.map_show


class Player:
    def __init__(self, name, posx, posy):
        self.name = name
        self.posx = 2
        self.posy = 2
        self.key = False
        self.thirst = 100

    def change_pos(self, newposx, newposy):
        self.posx = newposx
        self.posy = newposy


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


def arrows_move(posx, posy, char):  # moving in menu
    arrows_ud = {"[A": -1, "[B": 1, "[C": 0, "[D": 0}  # up down
    arrows_lr = {"[A": 0, "[B": 0, "[C": 1, "[D": -1}  # left right
    if posx + arrows_lr[char] < 0 or posx + arrows_lr[char] > len(game.map[0]) - 1 or \
        posy + arrows_ud[char] < 0 or posy + arrows_ud[char] > len(game.map) - 1 or \
            game.map[posy + arrows_ud[char]][posx + arrows_lr[char]] == "#":
        return posx, posy
    return posx + arrows_lr[char], posy + arrows_ud[char]


game = Map(120, "map1.txt")
posx = 2
posy = 2
gamer = Player("kamil", posx, posy)
game.map_load(posx, posy)


def print_game_window(game):
    cls()
    print("\n"*5)
    length_window_game = len(game.map_show.split("\n")[0]) - 12
    print(10 * " ",  length_window_game * "-")
    print(game, end="")
    print(10 * " ", length_window_game * "-")


while True:
    print_game_window(game)
    char = getChar(1)
    if(char == "\x1b"):
        char = getChar(2)
        posx, posy = arrows_move(posx, posy, char)
        gamer.change_pos(posx, posy)
        game.map_load(posx, posy)
