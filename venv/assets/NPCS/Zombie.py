from assets.NPCS.NPC import NPC
from assets.UI.Healthbar import Healthbar
import random as r
import pygame

class Zombie(NPC):
    def __init__(self):
        self.health = r.randint(50, 100)
        self.maxHealth = self.health
        self.strength = 0
        self.modifier = 10
        
    def draw(self, window, position: (int, int)):
        healthbar = Healthbar(self.health, self.maxHealth, (position[0], position[1] - 40))
        pygame.draw.circle(window, (165, 0, 0), position, 20)
        healthbar.draw(window)