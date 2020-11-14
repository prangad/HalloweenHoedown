import pygame
import random

from assets.NPCS.Zombie import Zombie
from assets.NPCS.Werewolf import Werewolf
from assets.NPCS.Vampire import Vampire
from assets.NPCS.Ghoul import Ghoul

class House():
    def __init__(self, position: (int, int)):
        self.position = position
        self.monsters = {"Person" : [],
                         "Zombie" : [],
                         "Werewolf" : [],
                         "Vampire": [],
                         "Ghoul" : []};
        self.config = {"SIZE": 200,
                       "OUTLINE_COLOR": (0, 0, 0),
                       "OUTLINE_WIDTH": 1,
                       "ROOF_COLOR": (80, 40, 0)}

        monsterCount = random.randint(0, 10)
        self.color = pygame.Color((0, 0, 0))
        self.color.hsva = (100-(10*monsterCount), 100, 100, 0)
        print("MONSTERS: {0}".format(monsterCount))
        numMonsters = 0;
        while (numMonsters < monsterCount):
            monsterType = random.choice(["Zombie", "Werewolf", "Vampire", "Ghoul"])
            if (monsterType == "Zombie"):
                self.monsters[monsterType].append(Zombie())
            if (monsterType == "Werewolf"):
                self.monsters[monsterType].append(Werewolf())
            if (monsterType == "Vampire"):
                self.monsters[monsterType].append(Vampire())
            if (monsterType == "Ghoul"):
                self.monsters[monsterType].append(Ghoul())
            numMonsters += 1

    def draw(self, window, relativePosition):
        WIDTH = window.get_width()
        HEIGHT = window.get_height()

        pygame.draw.rect(window, self.config["OUTLINE_COLOR"], [WIDTH/2 + (self.position[0]-(self.config["SIZE"]/2))-relativePosition[0],
                                                                (HEIGHT/2 + (self.position[1]-(self.config["SIZE"]/2))+(self.config["SIZE"]/3))-relativePosition[1],
                                                                self.config["SIZE"],
                                                                (self.config["SIZE"]/3)*2])
        pygame.draw.rect(window, self.color, [WIDTH/2 + ((self.position[0] - (self.config["SIZE"] / 2)) + self.config["OUTLINE_WIDTH"])-relativePosition[0],
                                              HEIGHT/2 + ((self.position[1] - (self.config["SIZE"] / 2)) + (self.config["SIZE"] / 3) + self.config["OUTLINE_WIDTH"])-relativePosition[1],
                                              self.config["SIZE"]-(self.config["OUTLINE_WIDTH"]*2),
                                              ((self.config["SIZE"] / 3) * 2)-(self.config["OUTLINE_WIDTH"]*2)])
        pygame.draw.polygon(window, self.config["ROOF_COLOR"], [(WIDTH/2 + self.position[0]-(self.config["SIZE"]/2)-relativePosition[0], HEIGHT/2 + (self.position[1]-(self.config["SIZE"]/2))+(self.config["SIZE"]/3)-relativePosition[1]),
                                                                (WIDTH/2 + self.position[0]-(self.config["SIZE"]/2)+self.config["SIZE"]/2-relativePosition[0], HEIGHT/2 + self.position[1]-(self.config["SIZE"]/2)-relativePosition[1]),
                                                                (WIDTH/2 + self.position[0]+self.config["SIZE"]/2-relativePosition[0], HEIGHT/2 + (self.position[1]-(self.config["SIZE"]/2))+(self.config["SIZE"]/3)-relativePosition[1])])
        pygame.draw.polygon(window, self.config["OUTLINE_COLOR"], [(WIDTH/2 + self.position[0]-(self.config["SIZE"]/2)-relativePosition[0], HEIGHT/2 + (self.position[1]-(self.config["SIZE"]/2))+(self.config["SIZE"]/3)-relativePosition[1]),
                                                                (WIDTH/2 + self.position[0]-(self.config["SIZE"]/2)+self.config["SIZE"]/2-relativePosition[0], HEIGHT/2 + self.position[1]-(self.config["SIZE"]/2)-relativePosition[1]),
                                                                (WIDTH/2 + self.position[0]+self.config["SIZE"]/2-relativePosition[0], HEIGHT/2 + (self.position[1]-(self.config["SIZE"]/2))+(self.config["SIZE"]/3)-relativePosition[1])],
                                                                width=1)