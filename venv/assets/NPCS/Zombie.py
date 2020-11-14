from assets.NPCS.NPC import NPC
import random as r

class Zombie(NPC):
    def __init__(self):
        self.health = r.randint(50, 100)
        self.strength = 0
        self.modifier = 10