import random
from EventHandler import Observable

#Base class for all NPC's. Observable to
class NPC(Observable):
    def __init__(self):
        Observable.__init__(self)
        self.health = 0
        self.strength = 0
        self.modifier = 0

    # Basic attack method.
    def attack(self):
        return random.randint(self.strength, self.strength + self.modifier)

    # The most basic damage-taking function. Can be added to by child classes.
    def take_damage(self, damage, weapon):
        self.health = self.health-damage if (damage <= self.health) else 0
        if (self.health <= 0):
            self.notifyAll(self)
        return damage

    # To be overridden by child classes.
    def draw(self):
        pass