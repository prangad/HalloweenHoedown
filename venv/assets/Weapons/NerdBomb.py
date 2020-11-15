import random
class NerdBomb():
    def __init__(self):
        self.damage_modifier = lambda : random.randint(350, 500)/100
        self.remaining_uses = 1