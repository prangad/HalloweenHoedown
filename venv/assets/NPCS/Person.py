from assets.NPCS.NPC import NPC
from assets.UI.Healthbar import Healthbar
import pygame
import random

class Person(NPC):
    def __init__(self):
        NPC.__init__(self)
        self.health = 100
        self.maxHealth = self.health
        self.strength = -1
        self.modifier = 0
        self.image = pygame.image.load("assets\\Resources\\Person"+str(random.randint(1, 6))+".png")

    def draw(self, window, position: (int, int)):
        window.blit(self.image, (position[0] - self.image.get_width() / 2, position[1] - self.image.get_height() / 2))