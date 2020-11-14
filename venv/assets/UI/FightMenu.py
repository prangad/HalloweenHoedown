import pygame
import random
from assets.Objects.House import House

class FightMenu:
    def __init__(self, player, house):
        self.player = player
        self.house:House = house
        self.config = {"UI_MARGIN" : 5,
                       "BORDER_THICKNESS" : 1,
                       "COLOR_BACKGROUND": (40, 40, 40),
                       "COLOR_ACCENT": (200, 200, 200),
                       "COLOR_PRIMARY": (60, 60, 60),
                       "MONSTER_SPACING": 20,
                       "MONSTER_MARGIN": lambda numMonsters: 800 - (numMonsters * 60),
                       "MONSTER_MIN_Y": 200}
        self.menuOptions = {"Attack": [],
                            "Select Weapon": [],
                            "Flee": []}

    def draw(self, window):
        WIDTH = window.get_width()
        HEIGHT = window.get_height()
        window.fill(self.config["COLOR_BACKGROUND"])

        # Bottom Menu Framing / Backdrop
        pygame.draw.rect(window, self.config["COLOR_ACCENT"], [self.config["UI_MARGIN"],
                                                   ((HEIGHT/3)*2) + self.config["UI_MARGIN"],
                                                   WIDTH-(self.config["UI_MARGIN"]*2),
                                                   (HEIGHT/3)-(self.config["UI_MARGIN"]*2)])
        pygame.draw.rect(window, self.config["COLOR_PRIMARY"], [self.config["UI_MARGIN"] + self.config["BORDER_THICKNESS"],
                                                   (((HEIGHT/3)*2) + self.config["UI_MARGIN"]) + self.config["BORDER_THICKNESS"],
                                                   (WIDTH-(self.config["UI_MARGIN"]*2)) - (self.config["BORDER_THICKNESS"]*2),
                                                   ((HEIGHT/3)-(self.config["UI_MARGIN"]*2)) - (self.config["BORDER_THICKNESS"]*2)])

        #HUD Drawing
        font = pygame.font.SysFont("Roboto", 48)
        pygame.draw.rect(window, self.config["COLOR_ACCENT"], [self.config["UI_MARGIN"],
                                                   self.config["UI_MARGIN"],
                                                   WIDTH - (self.config["UI_MARGIN"] * 2),
                                                   font.get_height() + self.config["UI_MARGIN"]])
        pygame.draw.rect(window, self.config["COLOR_PRIMARY"], [self.config["UI_MARGIN"] + self.config["BORDER_THICKNESS"],
                                                   self.config["UI_MARGIN"] + self.config["BORDER_THICKNESS"],
                                                   (WIDTH - (self.config["UI_MARGIN"] * 2) - self.config["BORDER_THICKNESS"]*2),
                                                   (font.get_height() + self.config["UI_MARGIN"]) - self.config["BORDER_THICKNESS"]*2])
        text = font.render("Health: {0}".format(100), True, (180, 0, 0))
        window.blit(text, (self.config["UI_MARGIN"]*2, self.config["UI_MARGIN"]*2))

        #Enemy Drawing
        monsterPosXScalar = ((WIDTH-self.config["MONSTER_MARGIN"](len(self.house.monsters))*2)/(len(self.house.monsters)-1)) if (len(self.house.monsters) > 1) else 0
        for i in range(len(self.house.monsters)):
            self.house.monsters[i].draw(window, ((monsterPosXScalar*i+self.config["MONSTER_MARGIN"](len(self.house.monsters))) if len(self.house.monsters) > 1 else WIDTH/2,
                                                 self.config["MONSTER_MIN_Y"]))