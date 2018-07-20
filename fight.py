import random
import time
from common import cls, getChar
from mobs import Mob


class Fight:
    def __init__(self, gamer):
        self.gamer = gamer
        with open("questions.txt") as q:
            self.lines = q.readlines()
        for i, line in enumerate(self.lines):
            line = line[:-1].split(';')
            line[2] = line[2].split(',')
            line[2] = {'A': line[2][0], 'B': line[2][1], 'C': line[2][2], 'D': line[2][3]}
            self.lines[i] = line

    def random_quest(self):
        cls()
        self.chosen_q = random.choice(self.lines)

    def start_fight(self, which_enemy, which_level):
        self.mob = Mob(which_enemy, which_level)
        self.random_quest()
        self.score = self.mob.health
        char = ""
        option = 'A'
        movement = {'[CA': 'B', '[CC': 'D', '[DB': 'A', '[DD': 'C', '[BA': 'C', '[BB': 'D', '[AC': 'A', '[AD': 'B',
                    '[AA': 'A', '[DA': 'A', '[AB': 'B', '[CB': 'B', '[DC': 'C', '[BC': 'C', '[BD': 'D', '[CD': 'D'}
        while self.mob.health > 0 and self.gamer.health > 0:
            char = ""
            self.random_quest()
            while char != "\n":
                with open("ascii/ans_ascii_" + option + ".txt") as filename:
                    self.string = filename.read()

                self.string = self.string.replace('[]', str(self.gamer.health) + (7 - len(str(self.gamer.health))) * " ", 1)
                self.string = self.string.replace('[]', str(self.mob.health) + (5 - len(str(self.mob.health))) * " ", 1 )
                self.string = self.string.replace('{}', self.chosen_q[0] + (86 - len(self.chosen_q[0])) * " " , 1)
                self.string = self.string.replace('{}', self.chosen_q[2]['A'] + (22 - len(self.chosen_q[2]['A'])) * " " , 1)
                self.string = self.string.replace('{}', self.chosen_q[2]['B'] + (24 - len(self.chosen_q[2]['B'])) * " " , 1)
                self.string = self.string.replace('{}', self.chosen_q[2]['C'] + (22 - len(self.chosen_q[2]['C'])) * " " , 1)
                self.string = self.string.replace('{}', self.chosen_q[2]['D'] + (24 - len(self.chosen_q[2]['D'])) * " " , 1)

                cls()

                print(self.string)

                char = getChar(1)
                if char == "\x1b":
                    char = getChar(2)
                    option = movement[char + option]
                elif char == "\n":
                    ans = option
                    x = 1
                    break

            if ans == self.chosen_q[1]:
                print ("Well done!  You hit your enemie!")
                time.sleep (1.5)
                self.gamer.attack_mob(self.mob)
                time.sleep (1.5)
            else: 
                print ("Damn! You missed ")
                time.sleep (1.5)

            self.mob.attack_player(self.gamer)
            time.sleep (1.5)

            if self.mob.health <= 0:
                print ("Enemie is Dead! Well done hero!")
                self.gamer.score += self.score
                self.gamer.key = self.mob.have_key
                time.sleep (1.5)
                self.gamer.health = 100

            elif self.gamer.health <= 0:
                print ("Wow you are dead! Game over!")
                time.sleep (1.5)


# x = Fight(100, 100, 5, 20)
# x.random_quest()
# x.egse()
