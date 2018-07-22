from common import getChar, Printing, cls
from termcolor import cprint


class Player:
    def __init__(self, posx, posy):
        self.score = 0
        self.char_create()
        self.posx = 2
        self.posy = 2
        self.key = False
        self.hunger = 100.0
        self.health = 100
        self.equiped = {'boots': 0, 'chest': 0, 'shoulder': 0, 'gloves': 0, 'helmet': 0, 'sword': 0, 'light': 0}
        self.update_stats()
        self.inventory = {}
        self.printing = Printing([20, 40], 61, "Stats")
        self.score = 0

    def char_create(self):
        cls()
        self.name = input("Enter your nick: \n")

    def change_score(self, value):
        self.score += value

    def change_hunger(self, value):
        self.hunger += value
        if self.hunger > 100:
            self.hunger = 100.0
        self.update_stats()

    def change_item_stat(self, item_type, value):
        self.equiped[item_type] = value
        self.update_stats()

    def update_stats(self):
        self.stats = {'defence': self.equiped['boots'] + self.equiped['chest'] + self.equiped['shoulder'] +
                      self.equiped['gloves'] + self.equiped['helmet'], 'attack': 10 + self.equiped['sword'],
                      'radius': 5 + self.equiped['light'], 'hunger': round(self.hunger, 1), 'score': self.score}

    def change_pos(self, newposx, newposy):
        self.posx = newposx
        self.posy = newposy

    def attack_mob(self, mob):
        print("You hit enemie for ", self.stats['attack'], "dmg!")
        mob.health -= self.stats["attack"]

    def run_statistic(self):
        char = ""
        while char.lower() != 'c':
            cls()
            self.print_stats()
            char = getChar(1)
            if char == '\x1b':
                getChar(2)

    def print_stats(self):
        self.printing.print_title()
        self.printing.print_row(["Stat", "Value"], header=True)

        for stat in self.stats:
            self.printing.print_row([stat, self.stats[stat]])

        cprint("|" + self.printing.table_length * "_" + "|", 'white', 'on_grey', attrs=['bold'])
