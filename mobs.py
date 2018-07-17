class Mob:
    def __init__(self, name, attack, defence, life, have_key, posx, posy):
        self.name = name
        self.posx = 2
        self.posy = 2
        self.attack = attack
        self.defence = defence
        self.life = life
        self.prone = prone
        self.have_key = have_key

    def attack_player(self, player):
        player.health -= self.attack * (1 - player.defence)