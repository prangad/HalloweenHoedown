import random
from assets.Weapons.Weapon import Weapon

# Child class of the Weapon class.
class NerdBomb(Weapon):
    def __init__(self):
        self.__class__.__name__ = "Nerd Bomb"
        Weapon.__init__(self)
        # Returns random modifier each time it's called.
        self.damage_modifier = lambda : random.randint(350, 500)/100
        self.remaining_uses = 1