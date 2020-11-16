from assets.NPCS.NPC import NPC
from assets.UI.Healthbar import Healthbar
from assets.Weapons.ChocolateBar import ChocolateBar
import random as r
import pygame

class Vampire(NPC):
    def __init__(self):
        NPC.__init__(self)
        self.health = r.randint(10, 20)
        self.maxHealth = self.health
        self.strength = 10
        self.modifier = 10
        self.image = pygame.image.load("assets\\Resources\\Vampire.png")

    def draw(self, window, position: (int, int)):
        healthbar = Healthbar(self.health, self.maxHealth, (position[0], position[1] - self.image.get_height()/2 - 10))
        window.blit(self.image, (position[0] - self.image.get_width() / 2, position[1] - self.image.get_height() / 2))
        healthbar.draw(window)

    def take_damage(self, damage, weapon):
        if weapon.__class__ == ChocolateBar:
            damage = 0
        return super().take_damage(damage, weapon)
