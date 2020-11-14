from assets.NPCS.NPC import NPC

class Werewolf(NPC):
    def __init__(self):
        self.health = 200
        self.strength = 0
        self.modifier = 40