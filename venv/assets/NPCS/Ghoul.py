from assets.NPCS.NPC import NPC
from assets.UI.Healthbar import Healthbar
import pygame
import random as r

class Ghoul(NPC):
    def __init__(self):
        NPC.__init__(self)
        self.health = r.randint(40, 80)
        self.maxHealth = self.health
        self.strength = 15
        self.modifier = 15

    def draw(self, window, position: (int, int)):
        healthbar = Healthbar(self.health, self.maxHealth, (position[0], position[1]-40))
        pygame.draw.circle(window, (255, 0, 0), position, 20)
        healthbar.draw(window)
