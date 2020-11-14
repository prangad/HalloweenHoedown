import random as r

class NPC():
    def __init__(self):
        self.health = 0
        self.strength = 0
        self.modifier = 0

    def attack(self):
        return r.randint(self.strength, self.strength + self.modifier)

    def take_damage(self, damage, weapon):
        self.health = self.health-damage if (damage <= health) else 0

        if self.health == 0:
            self.die()

    def die(self):
        pass

    def draw(self):
        pass