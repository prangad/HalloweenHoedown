from assets.NPCS.NPC import NPC
from assets.UI.Healthbar import Healthbar
import pygame

class Werewolf(NPC):
    def __init__(self):
        NPC.__init__(self)
        self.health = 200
        self.maxHealth = self.health
        self.strength = 0
        self.modifier = 40

    def draw(self, window, position: (int, int)):
        healthbar = Healthbar(self.health, self.maxHealth, (position[0], position[1] - 40))
        pygame.draw.circle(window, (195, 0, 0), position, 20)
        healthbar.draw(window)