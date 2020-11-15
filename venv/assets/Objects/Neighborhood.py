import pygame
from assets.Objects.House import House
from assets.Objects.Player import Player

class Neighborhood:
    def __init__(self):
        self.player = Player()
        self.houses = []
        self.config = {"COLOR_BACKGROUND": (40, 40, 40)}

        self.populate()

    def populate(self):
        for i in range(-5, 5):
            self.houses.append(House((250 * i, -125)))

    def draw(self, window, relativePosition):
        WIDTH = window.get_width()
        HEIGHT = window.get_height()
        window.fill(self.config["COLOR_BACKGROUND"])

        for house in self.houses:
            house.draw(window, relativePosition)

        self.player.draw(window)

    def getHouseInRange(self, position: (int, int), range: int):
        for house in self.houses:
            if (abs(house.position[0]-position[0]) <= range+house.config["SIZE"]/2)\
                    and (abs(house.position[1]-position[1]) <= range+house.config["SIZE"]/2):
                return house
        return None