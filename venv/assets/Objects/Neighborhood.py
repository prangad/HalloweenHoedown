import pygame
import random
from assets.Objects.House import House
from assets.Objects.Player import Player

class Neighborhood:
    def __init__(self):
        # Drawing configuration options.
        self.config = {"COLOR_BACKGROUND": (40, 40, 40)}

        self.player = Player()
        self.houses = []

        self.populate()
        random.choice(self.houses).home = True

    # Populate method used to populate the neighborhood with houses on initialization.
    def populate(self):
        houseNum = random.randint(1, 5)
        for i in range(houseNum * -1, houseNum):
            self.houses.append(House((300 * i, -225)))

    # getHouseInRange method used to get the house that the playe is standing on.
    def getHouseInRange(self, position: (int, int), range: int):
        for house in self.houses:
            if (abs(house.position[0]-position[0]) <= range+house.config["SIZE"]/2)\
                    and (abs(house.position[1]-position[1]) <= range+house.config["SIZE"]/2):
                return house
        return None

    def cleared(self):
        for house in self.houses:
            if house.monsterCount > 0:
                return False
        return True

    ##################################################
    # "Non-Functional" Drawing Methods
    ##################################################
    def draw(self, window, relativePosition):
        WIDTH = window.get_width()
        HEIGHT = window.get_height()
        window.fill(self.config["COLOR_BACKGROUND"])

        for house in self.houses:
            house.draw(window, relativePosition)

        self.player.draw(window)