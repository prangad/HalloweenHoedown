import random as r
import pygame

from assets.NPCS.NPC import NPC
from assets.UI.Healthbar import Healthbar
from assets.Weapons.NerdBomb import NerdBomb

# Ghoul class that inherits from parent class NPC.
class Ghoul(NPC):
    def __init__(self):
        NPC.__init__(self)
        self.health = r.randint(40, 80)
        self.maxHealth = self.health
        self.strength = 15
        self.modifier = 15
        self.image = pygame.image.load("assets\\Resources\\Ghoul.png")

    # Overridden damage taking method to add NerdBomb exception.
    def take_damage(self, damage, weapon):
        if weapon.__class__ == NerdBomb:
            damage *= 5
        return super().take_damage(damage, weapon)

    def draw(self, window, position: (int, int)):
        healthbar = Healthbar(self.health, self.maxHealth, (position[0], position[1] - self.image.get_height()/2 - 10))
        window.blit(self.image, (position[0]-self.image.get_width()/2, position[1]-self.image.get_height()/2))
        healthbar.draw(window)
