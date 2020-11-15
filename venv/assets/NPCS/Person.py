from assets.NPCS.NPC import NPC
from assets.UI.Healthbar import Healthbar
import pygame

class Person(NPC):
    def __init__(self):
        NPC.__init__(self)
        self.health = 100
        self.maxHealth = self.health
        self.strength = -1
        self.modifier = 0

    def draw(self, window, position: (int, int)):
        pygame.draw.circle(window, (0, 255, 0), position, 20)