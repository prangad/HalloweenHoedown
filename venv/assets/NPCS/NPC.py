import random as r
from EventHandler import Observable

class NPC(Observable):
    def __init__(self):
        Observable.__init__(self)
        self.health = 0
        self.strength = 0
        self.modifier = 0

    def attack(self):
        return r.randint(self.strength, self.strength + self.modifier)

    def take_damage(self, damage, weapon):
        self.health = self.health-damage if (damage <= self.health) else 0
        if (self.health <= 0):
            self.notifyAll(self)

    def draw(self):
        pass