import pygame
import State
import FightMenu
from assets.Objects.Neighborhood import Neighborhood
from assets.Objects.Player import Player

class Window:
    def __init__(self, neighborhood, fight_menu):
        pygame.init()
        self.window = pygame.display.set_mode([1600, 900])
        self.running = True
        self.state = State.NEIGHBORHOOD
        self.neighborhood = neighborhood
        self.player = Player()
        self.fight_menu = fight_menu
        self.game_loop()

    def game_loop(self):
        while self.running:
            pygame.time.delay(5)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        InteractedHouse = self.neighborhood.getHouseInRange(self.player.position, self.player.config["SIZE"])
                        if InteractedHouse != None:
                            self.fight_menu = self.player.interact(InteractedHouse)
                            self.state = State.FIGHT_MENU

            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                self.player.move(Player.LEFT)
            if keys[pygame.K_w]:
                self.player.move(Player.UP)
            if keys[pygame.K_d]:
                self.player.move(Player.RIGHT)
            if keys[pygame.K_s]:
                self.player.move(Player.DOWN)

            if self.state == State.FIGHT_MENU:
                self.fight_menu.draw(self.window)
            elif self.state == State.NEIGHBORHOOD:
                self.neighborhood.draw(self.window, self.player.position)
                self.player.draw(self.window)

            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    fight_menu = FightMenu.FightMenu(None, None)
    neighborhood = Neighborhood()
    game = Window(neighborhood, fight_menu)