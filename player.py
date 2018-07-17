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

    def enemy_encountered(self, game):
        pass

    def attack_mob(self, mob):
        mob.health -= self.attack
        if self.sword == mob.prone:
            mob.health -= self.attack

    # def chest_encountered(self, inv):
    #     inv.add_to_inv("items.txt", 20)