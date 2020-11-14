import pygame

class Healthbar():
    def __init__(self, health, maxHealth, position: (int, int)):
        self.maxHealth = maxHealth
        self.health = health
        self.position = position
        self.config = {"BORDER_COLOR": (255, 255, 255),
                       "BORDER_THICKNESS": 1,
                       "BACKGROUND_COLOR": (255, 60, 60),
                       "FOREGROUND_COLOR": (70, 240, 115),
                       "WIDTH": 60,
                       "HEIGHT": 12}

    def draw(self, window):
        pygame.draw.rect(window, self.config["BORDER_COLOR"], (self.position[0] - self.config["WIDTH"] / 2,
                                                               self.position[1] - self.config["HEIGHT"] / 2,
                                                               self.config["WIDTH"], self.config["HEIGHT"]))
        pygame.draw.rect(window, self.config["BACKGROUND_COLOR"], (self.position[0] - self.config["WIDTH"] / 2 + self.config["BORDER_THICKNESS"],
                                                                   self.position[1] - self.config["HEIGHT"] / 2 + self.config["BORDER_THICKNESS"],
                                                                   self.config["WIDTH"] - self.config["BORDER_THICKNESS"]*2,
                                                                   self.config["HEIGHT"] - self.config["BORDER_THICKNESS"]*2))
        pygame.draw.rect(window, self.config["FOREGROUND_COLOR"], (self.position[0] - self.config["WIDTH"] / 2 + self.config["BORDER_THICKNESS"],
                                                                   self.position[1] - self.config["HEIGHT"] / 2 + self.config["BORDER_THICKNESS"],
                                                                   (self.config["WIDTH"] - self.config["BORDER_THICKNESS"] * 2)*(self.health/self.maxHealth),
                                                                   self.config["HEIGHT"] - self.config["BORDER_THICKNESS"] * 2))