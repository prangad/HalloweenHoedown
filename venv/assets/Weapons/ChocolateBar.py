import random
from assets.Weapons.Weapon import Weapon

# Child class of the Weapon class.
class ChocolateBar(Weapon):
    def __init__(self):
        self.__class__.__name__ = "Chocolate Bar"
        Weapon.__init__(self)
        # Gets a random modifier each time it's accessed.
        self.damage_modifier = lambda : random.randint(200, 240)/100
        self.remaining_uses = 4