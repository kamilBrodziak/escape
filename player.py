from common import getChar, Printing, cls
from termcolor import cprint


class Player:
    def __init__(self, name, posx, posy):
        self.score = 0
        self.name = name
        self.posx = 2
        self.posy = 2
        self.key = False
        self.hunger = 100.0
        self.equiped = {'boots': 0, 'chest': 0, 'shoulder': 0, 'gloves': 0, 'helmet': 0, 'sword': 0, 'light': 0}
        self.update_stats()
        self.inventory = {}
        self.printing = Printing([20, 40], 61, "Stats")

    def update_stats(self):
        self.stats = {'defence': self.equiped['boots'] + self.equiped['chest'] + self.equiped['shoulder'] +
                      self.equiped['gloves'] + self.equiped['helmet'], 'attack': 10 + self.equiped['sword'],
                      'radius': 5 + self.equiped['light'], 'hunger': round(self.hunger, 1)}

    def change_pos(self, newposx, newposy):
        self.posx = newposx
        self.posy = newposy

    def enemy_encountered(self, game):
        pass

    def attack_mob(self, mob):
        mob.health -= self.attack
        if self.sword == mob.prone:
            mob.health -= self.attack

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
