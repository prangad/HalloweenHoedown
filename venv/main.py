import pygame
from assets.Objects.Neighborhood import Neighborhood
from assets.Objects.Player import Player
from assets.UI.FightMenu import FightMenu
from assets.UI.EndScreen import EndScreen

# GameState class used to determine which content to display.
class GameState():
    NEIGHBORHOOD = 1
    FIGHT_MENU = 2

class Window:
    def __init__(self, neighborhood):
        # Basic pygame setup and initialization.
        pygame.init()
        self.window = pygame.display.set_mode([1600, 900])

        # Basic required information for the game.
        self.neighborhood = neighborhood
        self.fight_menu = None # To be populated later when a player interacts with a house.
        self.running = True
        self.state = GameState.NEIGHBORHOOD # Start in the neighborhood.
        self.player = self.neighborhood.player

        self.game_loop() # Start the game loop.

    def game_loop(self):
        while self.running:
            pygame.time.delay(2) # Delay user input. (Players were too fast.)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # When the player presses the X button, end the game.
                    self.running = False
                if event.type == pygame.KEYDOWN: # Handle player pressing keys.
                    if self.state == GameState.NEIGHBORHOOD and event.key == pygame.K_SPACE: # Attempt an interaction.
                        InteractedHouse = self.neighborhood.getHouseInRange(self.player.position, self.player.config["SIZE"])
                        if InteractedHouse != None:
                            self.fight_menu = self.player.interact(InteractedHouse, self.neighborhood.cleared())
                            self.state = GameState.FIGHT_MENU
                    elif self.state == GameState.FIGHT_MENU: # Handle fight menu key input.
                        if event.key == pygame.K_SPACE:
                            self.fight_menu.select()
                        if event.key == pygame.K_w:
                            self.fight_menu.scroll_up()
                        if event.key == pygame.K_s:
                            self.fight_menu.scroll_down()

            self.player.move(pygame.key.get_pressed())

            # Draw the respective contrent that needs to be drawn.
            if self.state == GameState.FIGHT_MENU:
                if self.fight_menu.status == FightMenu.LEFT or self.fight_menu.status == FightMenu.FLED:
                    self.state = GameState.NEIGHBORHOOD
                else:
                    self.fight_menu.draw(self.window)
            elif self.state == GameState.NEIGHBORHOOD:
                self.neighborhood.draw(self.window, self.player.position)

            # Updates all pixels on the drawing window.
            pygame.display.flip()

        # Game over, loop ended. Close game.
        pygame.quit()


# Basic Python main method to initialize a new game.
if __name__ == "__main__":
    neighborhood = Neighborhood()
    game = Window(neighborhood)