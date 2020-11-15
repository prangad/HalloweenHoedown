import pygame
import random

from assets.NPCS.Zombie import Zombie
from assets.NPCS.Werewolf import Werewolf
from assets.NPCS.Vampire import Vampire
from assets.NPCS.Ghoul import Ghoul
from assets.NPCS.Person import Person
from EventHandler import Observable, Observer

class House(Observer):
    def __init__(self, position: (int, int)):
        self.position = position
        self.monsters = []
        self.config = {"SIZE": 200,
                       "OUTLINE_COLOR": (0, 0, 0),
                       "OUTLINE_WIDTH": 1,
                       "ROOF_COLOR": (80, 40, 0)}

        self.monsterCount = random.randint(0, 10)
        self.color = pygame.Color((0, 0, 0))

        monsterTypes = [Zombie, Werewolf, Vampire, Ghoul]
        numMonsters = 0;
        while (numMonsters < self.monsterCount):
            monster = random.choice(monsterTypes)()
            Observer.__init__(self, monster)
            self.monsters.append(monster)
            numMonsters += 1

    def notify(self, *args, **kwargs):
        for i in range(len(self.monsters)):
            if self.monsters[i] == args[0]:
                self.monsters[i] = Person()
                self.monsterCount -= 1

    def draw(self, window, relativePosition):
        WIDTH = window.get_width()
        HEIGHT = window.get_height()
        self.color.hsva = (100 - (10 * self.monsterCount), 100, 100, 0)

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