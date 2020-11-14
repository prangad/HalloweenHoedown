import pygame

class FightMenu:
    def __init__(self, player, house):
        self.player = player
        self.house = house
        self.config = {"UI_MARGIN" : 5,
                       "BORDER_THICKNESS" : 1,
                       "COLOR_BACKGROUND": (40, 40, 40),
                       "COLOR_ACCENT": (200, 200, 200),
                       "COLOR_PRIMARY": (60, 60, 60)}

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