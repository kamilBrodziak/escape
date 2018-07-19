class Mob:
    def __init__(self, name, which_level):
        self.which_level = which_level
        self.mobs = {'O': self.change_mob_stat(10, 80, False), 'G': self.change_mob_stat(5, 30, False),
                     'B': self.change_mob_stat(20, 150, True)}
        _ = self.mobs[name]
        if name == 'O':
            self.change_mob_stat(10, 80, False)
        elif name == 'G':
            self.change_mob_stat(5, 30, False)
        elif name == 'B':
            self.change_mob_stat(20, 150, True)

    def change_mob_stat(self, attack, life, have_key):
        self.attack = attack * self.which_level
        self.health = life * self.which_level
        self.have_key = have_key

    def attack_player(self, gamer):
        attack = round(self.attack * (1 - gamer.stats["defence"]/100), 2)
        gamer.health -= attack
        print("Enemie hits you for", attack, "dmg")
