class Enemie:
    def __init__ (self, type, lvl, hp, attack, deffence, weakness, key):
        self.mob_type = type
        self.mob_lvl = lvl
        self.mob_hp = hp
        self.mob_attack = attack
        self.mob_deffence = deffence
        self.mob_weakness = weakness
        self.have_key = key

    def changestat(self, lvl, hp, attack, deffence, key):
        self.mob_lvl = lvl
        self.mob_hp = hp
        self.mob_attack = attack
        self.mob_deffence = deffence
        self.have_key = key

ork = Enemie ('Orc', 1, 100, 10, 10, 'bow', 0)
#ork.changestat (2, 120, 12, 10)

goblin = Enemie ('Goblin', 1, 30, 2, 0, 'sword', 0)
#goblin.changestat (2, 120, 12, 10)

boss = Enemie ('Dragon', 10, 500, 40, 20, 'nothink you have', 0)

'''
ork_2 = Enemie ('Orc', 2, 120, 12, 10, 'bow')
ork_3 = Enemie ('Orc', 3, 150, 15, 15, 'bow')

goblin_2 = Enemie ('Goblin', 2, 35, 4, 2, 'sword')
goblin_3 = Enemie ('Goblin', 3, 40, 8, 5, 'sword')
'''