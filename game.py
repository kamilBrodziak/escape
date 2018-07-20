import player
import game_map
import mobs
import inventory
from common import getChar, cls
import time
import levels_game
import fight
from termcolor import cprint
from highscores import add_highscore_to_file, highscore_add_to_highscore_list


class Gamestart:
    def __init__(self):
        self.gamer = player.Player(2, 2)
        self.which_level = 1
        self.map_ = game_map.Map(self.gamer, "map" + str(self.which_level) + ".txt")
        self.inv = inventory.Inv(6, self.gamer, "items.txt")
        self.actual_chunk = self.map_.ascii_map[self.gamer.posy][self.gamer.posx]
        self.enemies = {'O', 'G', 'B'}
        self.chest = '$'
        self.levels = {'1', '2', '3', '4'}
        self.fighting = fight.Fight(self.gamer)
        self.END_LEVEL = 3
        self.which_ending = ""
        self.hint = False

    def run_game(self):
        self.map_.map_load(2, 2)
        while self.gamer.health > 0 and self.gamer.hunger > 0 and self.which_level < self.END_LEVEL + 1:
            print(self.map_)
            self.actions()
            if self.actual_chunk in self.enemies or self.actual_chunk == self.chest:
                self.map_.replace_char(self.map_.ascii_map[self.gamer.posy][self.gamer.posx], " ", self.gamer.posx, self.gamer.posy)
                if self.actual_chunk in self.enemies:
                    self.fighting.start_fight(self.actual_chunk, self.which_level)
                    self.inv.add_rand(4)
                    self.actual_chunk = self.map_.ascii_map[self.gamer.posy][self.gamer.posx]
                elif self.actual_chunk == self.chest:
                    self.inv.add_rand(2)
            elif self.actual_chunk in self.levels and self.gamer.key:
                self.start_level_game()
        highscore_add_to_highscore_list(self.gamer.name, self.gamer.score)
        add_highscore_to_file(self.gamer.name, self.gamer.score)
        if self.which_ending == "":
            self.which_ending = "LooseScreen"
        self.print_end_screen()

    def actions(self):
        char = getChar(1)
        if char == "\x1b":
            char = getChar(2)
            self.arrows_move(char)
        elif char.lower() == 'c':
            self.gamer.run_statistic()
        elif char.lower() == "i":
            self.inv.run_inv()
            self.map_.map_load(self.gamer.posx, self.gamer.posy)
        elif char == "0":
            self.inv.add_rand(50)
        elif char == "9":
            self.gamer.key = True
        elif char == '2':
            self.which_level = 2
            self.change_map("map" + str(self.which_level) + ".txt")
            self.gamer.posx = 115
            self.gamer.posy = 20
            self.map_.map_load(115, 20)
        elif char == '3':
            self.which_level = 3
            self.change_map("map" + str(self.which_level) + ".txt")
            self.gamer.posx = 119
            self.gamer.posy = 29
            self.map_.map_load(119, 29)
        elif char == '8':
            self.gamer.equiped['light'] = 100
            self.gamer.update_stats()
            self.map_.map_load(self.gamer.posx, self.gamer.posy)
            # print(self.map_)
        elif char == "7":
            self.hint = True

    def arrows_move(self, char):
        arrows_ud = {"[A": -1, "[B": 1, "[C": 0, "[D": 0}  # up down
        arrows_lr = {"[A": 0, "[B": 0, "[C": 1, "[D": -1}  # left right
        if self.map_.ascii_map[self.gamer.posy + arrows_ud[char]][self.gamer.posx + arrows_lr[char]] != "█":
            self.gamer.posx += arrows_lr[char]
            self.gamer.posy += arrows_ud[char]
            self.gamer.hunger -= 1/5
            self.gamer.update_stats()
            self.map_.map_load(self.gamer.posx, self.gamer.posy)
            self.actual_chunk = self.map_.ascii_map[self.gamer.posy][self.gamer.posx]

    def start_level_game(self):
        level_game = levels_game.LevelGameStart(self.which_level, self.hint)
        level_game.load_game()

        if level_game.result:
            self.gamer.score += 1000
            self.which_level += 1
            if self.which_level == self.END_LEVEL + 1:
                self.which_ending = "WinScreen"
                return
                
            self.gamer.key = False
            self.change_map("map" + str(self.which_level) + ".txt")
        else:
            self.gamer.score -= 100
            self.gamer.posx -= 1
            self.map_.map_load(self.gamer.posx, self.gamer.posy)
        cls()

    def change_map(self, filename):
        self.map_ = game_map.Map(self.gamer, filename)
        self.gamer.posx = 2
        self.gamer.posy = 2
        self.map_.map_load(2, 2)
    
    def print_end_screen(self):
        cls()
        color = 'green' if self.which_ending == "WinScreen" else 'red'
        with open("ascii/" + self.which_ending + ".txt") as screen:
            cprint(screen.read(), color, attrs=['bold'])
        time.sleep(2)
