import pygame
import random
from assets.Objects.House import House
from assets.NPCS.Person import Person
from assets.Resources.Dialog import Dialog

class FightMenu:
    ACTIVE = -1
    COMPLETE = 0
    FLED = 1
    DEATH = 2

    def __init__(self, player, house):
        self.player = player
        self.house:House = house
        self.config = {"UI_MARGIN" : 5,
                       "BORDER_THICKNESS" : 1,
                       "COLOR_BACKGROUND": (40, 40, 40),
                       "COLOR_ACCENT": (200, 200, 200),
                       "COLOR_PRIMARY": (60, 60, 60),
                       "MONSTER_SPACING": 20,
                       "MONSTER_MARGIN": lambda numMonsters, WIDTH: WIDTH/2 - (numMonsters * WIDTH/25),
                       "MONSTER_MIN_Y": 300}
        self.menuOptions = {"Attack": self.player.inventory,
                            "Flee": []}
        self.displayOptions = list(self.menuOptions.keys())
        self.selectedOption = 0
        self.status = FightMenu.ACTIVE
        self.turn = self.player
        self.notificationQueue = []

    def scroll_up(self):
        if self.selectedOption > 0 and len(self.notificationQueue) <= 0:
            self.selectedOption -= 1

    def scroll_down(self):
        if (self.selectedOption < len(self.menuOptions)-1) and len(self.notificationQueue) <= 0:
            self.selectedOption += 1

    def select(self):
        if len(self.notificationQueue) > 0:
            self.notificationQueue.pop(0)
            return

        if self.turn == self.player:
            if self.selectedOption == 1:
                if (random.random() <= 0.4):
                    self.status = FightMenu.FLED
                else:
                    self.notificationQueue.append(random.choice(Dialog.FLEE_MESSAGES))
            elif self.selectedOption == 0:
                for monster in self.house.monsters:
                    if not monster.health <= 0 and not monster.__class__ == Person:
                        self.notificationQueue.append("You attacked {0} with {1} and did {2} damage.".format(monster.__class__.__name__,
                                                                                                   self.player.inventory[0].__class__.__name__,
                                                                                                   self.player.strength))
                        monster.take_damage(self.player.strength, self.player.inventory[0])
        else:
            pass

    def draw(self, window):
        WIDTH = window.get_width()
        HEIGHT = window.get_height()
        window.fill(self.config["COLOR_BACKGROUND"])

        # Bottom Menu Framing / Backdrop
        pygame.draw.rect(window, self.config["COLOR_ACCENT"], [self.config["UI_MARGIN"],
                                                   ((HEIGHT/5)*4) + self.config["UI_MARGIN"],
                                                   WIDTH-(self.config["UI_MARGIN"]*2),
                                                   (HEIGHT/5)-(self.config["UI_MARGIN"]*2)])
        pygame.draw.rect(window, self.config["COLOR_PRIMARY"], [self.config["UI_MARGIN"] + self.config["BORDER_THICKNESS"],
                                                   (((HEIGHT/5)*4) + self.config["UI_MARGIN"]) + self.config["BORDER_THICKNESS"],
                                                   (WIDTH-(self.config["UI_MARGIN"]*2)) - (self.config["BORDER_THICKNESS"]*2),
                                                   ((HEIGHT/5)-(self.config["UI_MARGIN"]*2)) - (self.config["BORDER_THICKNESS"]*2)])

        # Bottom Menu Options
        font = pygame.font.SysFont("Verdana", 36)
        for i in range(len(self.menuOptions.keys())):
            menuOption = font.render(list(self.menuOptions.keys())[i], True, (255, 200, 200) if (i == self.selectedOption) else (160, 160, 160))
            window.blit(menuOption, (self.config["UI_MARGIN"]*2 + self.config["BORDER_THICKNESS"],
                                     (((HEIGHT/5)*4) + self.config["UI_MARGIN"]) + self.config["BORDER_THICKNESS"] + (i*font.get_height())))

        #HUD Drawing
        font = pygame.font.SysFont("Arial Black", 60)
        pygame.draw.rect(window, self.config["COLOR_ACCENT"], [self.config["UI_MARGIN"],
                                                   self.config["UI_MARGIN"],
                                                   WIDTH - (self.config["UI_MARGIN"] * 2),
                                                   font.get_height() + self.config["UI_MARGIN"]])
        pygame.draw.rect(window, (255, 60, 60), [self.config["UI_MARGIN"] + self.config["BORDER_THICKNESS"],
                                                   self.config["UI_MARGIN"] + self.config["BORDER_THICKNESS"],
                                                   (WIDTH - (self.config["UI_MARGIN"] * 2) - self.config["BORDER_THICKNESS"]*2),
                                                   (font.get_height() + self.config["UI_MARGIN"]) - self.config["BORDER_THICKNESS"]*2])
        pygame.draw.rect(window, (70, 240, 115), [self.config["UI_MARGIN"] + self.config["BORDER_THICKNESS"],
                                                 self.config["UI_MARGIN"] + self.config["BORDER_THICKNESS"],
                                                 ((WIDTH - (self.config["UI_MARGIN"] * 2) - self.config["BORDER_THICKNESS"] * 2) * (self.player.health/self.player.maxHealth)),
                                                 (font.get_height() + self.config["UI_MARGIN"]) - self.config["BORDER_THICKNESS"] * 2])

        healthText = font.render("Health", True, (0, 0, 0))
        window.blit(healthText, (self.config["UI_MARGIN"] * 2 + WIDTH/2 - 120, self.config["UI_MARGIN"] * 2))

        #Enemy Drawing
        monsterPosXScalar = ((WIDTH-self.config["MONSTER_MARGIN"](len(self.house.monsters), WIDTH)*2)/(len(self.house.monsters)-1)) if (len(self.house.monsters) > 1) else 0
        for i in range(len(self.house.monsters)):
            self.house.monsters[i].draw(window, ((monsterPosXScalar*i+self.config["MONSTER_MARGIN"](len(self.house.monsters), WIDTH)) if len(self.house.monsters) > 1 else WIDTH/2,
                                                 self.config["MONSTER_MIN_Y"]))

        if len(self.notificationQueue) > 0:
            font = pygame.font.SysFont("Segoe UI", 48)
            notificationText = font.render(self.notificationQueue[0], True, (255, 255, 255))
            continueText = font.render("Press SPACE to continue...", True, (255, 255, 255))
            window.blit(notificationText, (self.config["UI_MARGIN"] + self.config["BORDER_THICKNESS"],
                                           (((HEIGHT / 50) * 33) + self.config["UI_MARGIN"]) + self.config["BORDER_THICKNESS"]))
            window.blit(continueText, (self.config["UI_MARGIN"] + self.config["BORDER_THICKNESS"],
                                           (((HEIGHT / 50) * 36) + self.config["UI_MARGIN"]) + self.config["BORDER_THICKNESS"]))