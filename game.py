import player
import game_map
import mobs
import inventory
from common import getChar, arrows_move
import time


def gamestart(gamer, map_, posx, posy):
    enemies = {'O', 'G', 'B'}
    chest = '$'
    levels = {'1', '2', '3', '4', '5'}
    inv = inventory.Inv(6, gamer)
    while True:
        print(map_)
        char = getChar(1)
        if char == "\x1b":
            char = getChar(2)
            posx, posy = arrows_move(gamer.posx, gamer.posy, char, map_)
            gamer.change_pos(posx, posy)
            map_.map_load(posx, posy)
        elif char == "\n":
            pass
        elif char.lower() == 'c':
            gamer.run_statistic()
        elif char.lower() == "i":
            inv.run_inv()
            map_.map_load(posx, posy)
        actual_chunk = map_.ascii_map[posy][posx]
        if actual_chunk in enemies or actual_chunk == chest:
            map_.replace_char(map_.ascii_map[posy][posx], " ", posx, posy)
            if actual_chunk in enemies:
                gamer.enemy_encountered(map_)
            elif actual_chunk == chest:
                inv.add_rand("items.txt", 40)
        elif actual_chunk in levels and gamer.key:
            gamer.key = False
            gamer.change_pos(2, 2)
            map_.change_map("map" + actual_chunk + ".txt")
            map_.map_load(2, 2)
    return


def main():
    posx = 2
    posy = 2
    gamer = player.Player("kamil", posx, posy)
    map_ = game_map.Map(gamer, "map1.txt")
    map_.map_load(posx, posy)
    gamestart(gamer, map_, posx, posy)


main()
