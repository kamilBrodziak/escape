import sys
import os
import time
from termcolor import colored


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

    def change_radius(self, new_radius):
        self.radius = new_radius

    def map_load(self, posx, posy):
        radiusx_start = posx - 2 * self.radius if posx - 2 * self.radius >= 0 else 0
        radiusx_end = posx + 2 * self.radius if posx + 2 * self.radius <= len(self.ascii_map[0]) else \
            len(self.ascii_map[0])
        radiusy_start = posy - self.radius if posy - self.radius >= 0 else 0
        radiusy_end = posy + self.radius if posy + self.radius <= len(self.ascii_map) else len(self.ascii_map)
        map_copy = self.replace_char_in_string(colored("@", "blue"), posx, posy)
        new_map = ""
        for i in range(radiusy_start, radiusy_end):
            radiusx_end_copy = radiusx_end if i != posy else radiusx_end + len(colored("@", "blue")) - 1
            new_map += 10 * " " + "|" + map_copy[i][radiusx_start:radiusx_end_copy] + "|\n"
        self.map_show = new_map
        special_signs = {'G': colored("G", "yellow"), 'O': colored("O", "yellow", attrs=["dark"]), 'B': colored("B", "red"), '$': colored('$', 'green')}
        for i in special_signs.keys():
            self.replace_char(i, special_signs[i])

    def replace_char_in_string(self, new, posx, posy):
        map_copy = self.ascii_map[:]
        map_copy[posy] = list(map_copy[posy])
        map_copy[posy][posx] = new
        map_copy[posy] = "".join(map_copy[posy])
        return map_copy

    def replace_char(self, old, new, posx=None, posy=None):
        if posx is None or posy is None:
            self.map_show = self.map_show.replace(old, new)
        else:
            self.ascii_map = self.replace_char_in_string(" ", posx, posy)

    def __str__(self):
        cls()
        length_window_game = len(self.map_show.split("\n")[0]) - 12
        up_bottom_frame = 11 * " " + length_window_game * "-" + "\n"
        printed = "\n" * 6 + up_bottom_frame + self.map_show + up_bottom_frame
        return printed
