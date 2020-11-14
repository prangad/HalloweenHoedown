from assets.NPCS.NPC import NPC

class Person(NPC):
    def __init__(self):
        self.health = 100
        self.strength = -1
        self.modifier = 0