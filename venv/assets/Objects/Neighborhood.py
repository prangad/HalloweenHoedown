import pygame
class Neighborhood:
    def __init__(self):
        self.houses = []

    def get_objects(self):
        return [self.houses]

    def draw(self, pygame, window):
        pygame.draw.circle(window, (255, 0, 0), (400, 400), 100)