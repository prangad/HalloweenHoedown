import pygame
from assets.Objects.House import House

class Neighborhood:
    def __init__(self):
        self.houses = []
        self.houses.append(House((100, 100)))
        self.config = {"COLOR_BACKGROUND": (40, 40, 40)}

    def draw(self, window, relativePosition):
        WIDTH = window.get_width()
        HEIGHT = window.get_height()
        window.fill(self.config["COLOR_BACKGROUND"])

        for house in self.houses:
            house.draw(window, relativePosition)

    def getHouseInRange(self, position: (int, int), range: int):
        for house in self.houses:
            if (abs(house.position[0]-position[0]) <= range+house.config["SIZE"]/2)\
                    and (abs(house.position[1]-position[1]) <= range+house.config["SIZE"]/2):
                return house
        return None