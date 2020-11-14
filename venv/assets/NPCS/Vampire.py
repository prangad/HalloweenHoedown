from assets.NPCS.NPC import NPC
import random as r

class Vampire(NPC):
    def __init__(self):
        self.health = r.randint(10, 20)
        self.strength = 10
        self.modifier = 10