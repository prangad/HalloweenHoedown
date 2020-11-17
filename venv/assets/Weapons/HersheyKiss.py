from assets.Weapons.Weapon import Weapon

# Child class of the Weapon class.
class HersheyKiss(Weapon):
    def __init__(self):
        self.__class__.__name__ = "Hershey Kiss"
        Weapon.__init__(self)
        # Lambda used for continuity with other weapons.
        self.damage_modifier = lambda: 1
        self.remaining_uses = -1