import pygame
from assets.UI.FightMenu import FightMenu

class Player():
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 3

    def __init__(self):
        self.position = (0, 0)
        self.config = {"COLOR": (255, 255, 255),
                       "OUTLINE": (0, 0, 0),
                       "SIZE": 25,
                       "OUTLINE_WIDTH": 1}

    def draw(self, window):
        WIDTH = window.get_width();
        HEIGHT = window.get_height();
        pygame.draw.circle(window, self.config["OUTLINE"], (WIDTH/2, HEIGHT/2), self.config["SIZE"])
        pygame.draw.circle(window, self.config["COLOR"], (WIDTH/2, HEIGHT/2), self.config["SIZE"]-(self.config["OUTLINE_WIDTH"]*2))

    def move(self, direction):
        if (direction == Player.LEFT):
            self.position = (self.position[0]-1, self.position[1])
        if (direction == Player.UP):
            self.position = (self.position[0], self.position[1]-1)
        if (direction == Player.RIGHT):
            self.position = (self.position[0]+1, self.position[1])
        if (direction == Player.DOWN):
            self.position = (self.position[0], self.position[1]+1)

    def interact(self, House):
        return FightMenu(self, House)