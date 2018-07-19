import player
import game_map
import mobs
import inventory
from common import getChar, arrows_move, cls
import time
import levels_game


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
            oldpos = [posx, posy]
            posx, posy = arrows_move(gamer.posx, gamer.posy, char, map_)
            gamer.change_pos(posx, posy)
            if [posx, posy] != oldpos:
                gamer.hunger -= 1/5
                gamer.update_stats()
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
            gamer.change_pos(2, 2)
            result, score = levels_game.main(actual_chunk)
            if result:
                gamer.score -= score
                gamer.key = False
                map_.change_map("ascii/map" + actual_chunk + ".txt")
                map_.map_load(2, 2)
            else:
                gamer.score -= 20
            cls()
            with open("ascii/next_level" + str(result) + ".txt") as filename:
                    print(filename.read())
            time.sleep(3)

    return


def main():
    posx = 2
    posy = 2
    gamer = player.Player("kamil", posx, posy)
    map_ = game_map.Map(gamer, "map1.txt")
    map_.map_load(posx, posy)
    gamestart(gamer, map_, posx, posy)


main()
