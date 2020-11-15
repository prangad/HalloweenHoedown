import random
class ChocolateBar():
    def __init__(self):
        self.damage_modifier = lambda : random.randint(200, 240)/100
        self.remaining_uses = 4