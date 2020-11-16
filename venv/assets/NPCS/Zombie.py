from assets.NPCS.NPC import NPC
from assets.UI.Healthbar import Healthbar
import random as r
import pygame
from assets.Weapons.SourStraw import SourStraw

class Zombie(NPC):
    def __init__(self):
        NPC.__init__(self)
        self.health = r.randint(50, 100)
        self.maxHealth = self.health
        self.strength = 0
        self.modifier = 10
        self.image = pygame.image.load("assets\\Resources\\Zombie.png")
        
    def draw(self, window, position: (int, int)):
        healthbar = Healthbar(self.health, self.maxHealth, (position[0], position[1] - self.image.get_height()/2 - 10))
        window.blit(self.image, (position[0] - self.image.get_width() / 2, position[1] - self.image.get_height() / 2))
        healthbar.draw(window)

    def take_damage(self, damage, weapon):
        if weapon.__class__ == SourStraw:
            damage *= 2
        return super().take_damage(damage, weapon)