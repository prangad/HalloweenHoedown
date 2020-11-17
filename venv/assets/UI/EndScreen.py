import pygame

class EndScreen():
    def __init__(self, status):
        self.config = {}
        if status == 3:
            self.config["BACKGROUND_COLOR"] = (175, 0, 0)
            self.config["TEXT_COLOR"] = (0, 0, 0)
            self.config["TEXT"] = "You Died"
        if status == 4:
            self.config["BACKGROUND_COLOR"] = (140, 190, 255)
            self.config["TEXT_COLOR"] = (255, 255, 255)
            self.config["TEXT"] = "You defeated the monsters and saved your neighborhood."

    def draw(self, window):
        WIDTH = window.get_width()
        HEIGHT = window.get_height()

        pygame.draw.rect(window, self.config["BACKGROUND_COLOR"], (0, 0, WIDTH, HEIGHT))

        font = pygame.font.SysFont("Arial Black", 42)
        text = font.render(self.config["TEXT"], True, self.config["TEXT_COLOR"])
        text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        window.blit(text, text_rect)
