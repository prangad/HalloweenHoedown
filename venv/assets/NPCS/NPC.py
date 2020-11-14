import random as r

class NPC():
    def __init__(self):
        self.health = 0
        self.strength = 0
        self.modifier = 0

    def attack(self):
        return r.randint(self.strength, self.strength + self.modifier)

    def die(self):
        return