import random
class SourStraw():
    def __init__(self):
        self.damage_modifier = lambda : random.randint(100, 175)/100
        self.remaining_uses = 2