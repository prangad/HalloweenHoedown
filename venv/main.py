import pygame
import State
import FightMenu
import assets.Objects.Neighborhood as Neighborhood

class Window:
    def __init__(self, neighborhood, fight_menu):
        pygame.init()
        self.window = pygame.display.set_mode([800, 800])
        self.running = True
        self.state = State.NEIGHBORHOOD
        self.neighborhood = neighborhood
        self.fight_menu = fight_menu
        self.game_loop()

    def game_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            if self.state == State.FIGHT_MENU:
                for object in self.fight_menu.get_objects():
                    print("drawing fight menu object")
            elif self.state == State.NEIGHBORHOOD:
                self.neighborhood.draw(pygame, self.window)
            # self.window.fill((150, 150, 150))
            # pygame.draw.circle(self.window, (255, 0, 0), (400, 400), 100)
            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    person = None
    enemy = None
    fight_menu = FightMenu.FightMenu(person, enemy)
    neighborhood = Neighborhood.Neighborhood()
    game = Window(neighborhood, fight_menu)