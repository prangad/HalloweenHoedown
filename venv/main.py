import pygame
from assets.Objects.Neighborhood import Neighborhood
from assets.Objects.Player import Player
from assets.UI.FightMenu import FightMenu

class GameState():
    NEIGHBORHOOD = 1
    FIGHT_MENU = 2

class Window:
    def __init__(self, neighborhood):
        pygame.init()
        self.window = pygame.display.set_mode([1600, 900])

        self.neighborhood = neighborhood
        self.fight_menu = None
        self.running = True
        self.state = GameState.NEIGHBORHOOD

        self.player = self.neighborhood.player
        self.game_loop()

    def game_loop(self):
        while self.running:
            pygame.time.delay(2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if self.state == GameState.NEIGHBORHOOD:
                        if event.key == pygame.K_SPACE:
                            InteractedHouse = self.neighborhood.getHouseInRange(self.player.position, self.player.config["SIZE"])
                            if InteractedHouse != None:
                                self.fight_menu = self.player.interact(InteractedHouse)
                                self.state = GameState.FIGHT_MENU
                    elif self.state == GameState.FIGHT_MENU:
                        if event.key == pygame.K_SPACE:
                            self.fight_menu.select()
                        if event.key == pygame.K_w:
                            self.fight_menu.scroll_up()
                        if event.key == pygame.K_s:
                            self.fight_menu.scroll_down()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                self.player.move(Player.LEFT)
            if keys[pygame.K_w]:
                self.player.move(Player.UP)
            if keys[pygame.K_d]:
                self.player.move(Player.RIGHT)
            if keys[pygame.K_s]:
                self.player.move(Player.DOWN)

            if self.state == GameState.FIGHT_MENU:
                if self.fight_menu.status != FightMenu.ACTIVE:
                    self.state = GameState.NEIGHBORHOOD
                else:
                    self.fight_menu.draw(self.window)
            elif self.state == GameState.NEIGHBORHOOD:
                self.neighborhood.draw(self.window, self.player.position)

            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    neighborhood = Neighborhood()
    game = Window(neighborhood)