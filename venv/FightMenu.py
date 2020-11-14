import pygame
import Person

class FightMenu:
    def __init__(self, person, enemy):
        self.person = person
        self.enemy = enemy

    def get_objects(self):
        return [self.person, self.enemy]