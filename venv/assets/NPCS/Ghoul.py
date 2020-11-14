from assets.NPCS.NPC import NPC
import random as r

class Ghoul(NPC):
    def __init__(self):
        self.health = r.randint(40, 80)
        self.strength = 15
        self.modifier = 15