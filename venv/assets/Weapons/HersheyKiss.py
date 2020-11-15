from assets.Weapons.Weapon import Weapon

class HersheyKiss(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.damage_modifier = lambda: 1
        self.remaining_uses = -1