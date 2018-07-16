import sys
import os
import threading
import time


def cls():  # clearing screen in terminal
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


class Map:
    def __init__(self, radius, filename):
        self.radius = radius
        with open(filename) as mapfile:
            self.ascii_map = mapfile.read().splitlines()

    def change_radius(new_radius):
        self.radius = new_radius

    def map_load(self, posx, posy):
        radiusx_start = posx - 2 * self.radius if posx - 2 * self.radius >= 0 else 0
        radiusx_end = posx + 2 * self.radius if posx + 2 * self.radius <= len(self.ascii_map[0]) else \
            len(self.ascii_map[0])
        radiusy_start = posy - self.radius if posy - self.radius >= 0 else 0
        radiusy_end = posy + self.radius if posy + self.radius <= len(self.ascii_map) else len(self.ascii_map)
        map_copy = self.ascii_map[:]
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
        self.hunger = 100
        self.attack = 10
        self.sword = 0
        self.boots = 0
        self.chest = 0
        self.pants = 0
        self.helmet = 0
        self.defence = self.boots + self.pants + self.chest + self.helmet
        self.life = 100
        self.inventory = {}

    def change_pos(self, newposx, newposy):
        self.posx = newposx
        self.posy = newposy

    def attack_mob(self, mob):
        mob.health -= self.attack
        if self.sword == mob.prone:
            mob.health -= self.attack

    def inventory_add(self):
        pass

    def inventory_equip(self):
        pass


class Mob:
    def __init__(self, name, attack, defence, life, have_key, posx, posy):
        self.name = name
        self.posx = 2
        self.posy = 2
        self.attack = attack
        self.defence = defence
        self.life = life
        self.prone = prone
        self.have_key = have_key

    def attack_player(self, player):
        player.health -= self.attack * (1 - player.defence)


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


def arrows_move(posx, posy, char, game):  # moving in menu
    arrows_ud = {"[A": -1, "[B": 1, "[C": 0, "[D": 0}  # up down
    arrows_lr = {"[A": 0, "[B": 0, "[C": 1, "[D": -1}  # left right
    if posx + arrows_lr[char] < 0 or posx + arrows_lr[char] > len(game.ascii_map[0]) - 1 or \
        posy + arrows_ud[char] < 0 or posy + arrows_ud[char] > len(game.ascii_map) - 1 or \
            game.ascii_map[posy + arrows_ud[char]][posx + arrows_lr[char]] == "#":
        return posx, posy
    return posx + arrows_lr[char], posy + arrows_ud[char]


def print_game_window(game, gamer):
    cls()
    print(gamer.thirst)
    print("\n"*5)
    length_window_game = len(game.map_show.split("\n")[0]) - 12
    print(10 * " ",  length_window_game * "-")
    print(game, end="")
    print(10 * " ", length_window_game * "-")


def test(gamer, run_event):
    while run_event.is_set():
        time.sleep(1)
        gamer.thirst -= 1
    return


def gamestart(gamer, game, posx, posy, run_event):
    while run_event.is_set():
        print_game_window(game, gamer)
        char = getChar(1)
        if char == "\x1b":
            char = getChar(2)
            posx, posy = arrows_move(posx, posy, char, game)
            gamer.change_pos(posx, posy)
            game.map_load(posx, posy)
        elif char == "i":
            pass
    return


def main():
    game = Map(5, "map1.txt")
    posx = 2
    posy = 2
    gamer = Player("kamil", posx, posy)
    game.map_load(posx, posy)
    run_event = threading.Event()
    run_event.set()
    t2 = threading.Thread(target=test, args=(gamer, run_event, ))
    t1 = threading.Thread(target=gamestart, args=(gamer, game, posx, posy, run_event))
    t1.start()
    t2.start()
    try:
        while 1:
            time.sleep(.1)
    except KeyboardInterrupt:
        run_event.clear()
        t1.join()
        t2.join()
        return


main()
