import player
import game_map
import mobs


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


def arrows_move(posx, posy, char, map_):  # moving in menu/game
    arrows_ud = {"[A": -1, "[B": 1, "[C": 0, "[D": 0}  # up down
    arrows_lr = {"[A": 0, "[B": 0, "[C": 1, "[D": -1}  # left right
    if posx + arrows_lr[char] < 0 or posx + arrows_lr[char] > len(map_.ascii_map[0]) - 1 or \
        posy + arrows_ud[char] < 0 or posy + arrows_ud[char] > len(map_.ascii_map) - 1 or \
            map_.ascii_map[posy + arrows_ud[char]][posx + arrows_lr[char]] == "#":
        return posx, posy
    elif map_.ascii_map[posy + arrows_ud[char]][posx + arrows_lr[char]] == "$":
        pass
    elif map_.ascii_map[posy + arrows_ud[char]][posx + arrows_lr[char]] in {'O', 'G', 'B'}:
        pass
    return posx + arrows_lr[char], posy + arrows_ud[char]


def gamestart(gamer, map_, posx, posy):
    special_chars = {'O', 'G', 'B', '$'}
    while True:
        print(map_)
        char = getChar(1)
        if char == "\x1b":
            char = getChar(2)
            posx, posy = arrows_move(posx, posy, char, map_)
            gamer.change_pos(posx, posy)
            map_.map_load(posx, posy)
        elif char == "\n":
            pass
        if map_.ascii_map[posy][posx] in special_chars:
            gamer.enemy_encountered(map_)
            map_.replace_char(map_.ascii_map[posy][posx], " ", posx, posy)
    return


def main():
    map_ = game_map.Map(5, "map1.txt")
    posx = 2
    posy = 2
    gamer = player.Player("kamil", posx, posy)
    map_.map_load(posx, posy)
    gamestart(gamer, map_, posx, posy)


main()
