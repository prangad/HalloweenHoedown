import random
from assets.Weapons.Weapon import Weapon

class NerdBomb(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.damage_modifier = lambda : random.randint(350, 500)/100
        self.remaining_uses = 1