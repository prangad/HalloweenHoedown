import pygame
import random
from assets.UI.FightMenu import FightMenu
from assets.Weapons.HersheyKiss import HersheyKiss
from assets.Weapons.SourStraw import SourStraw
from assets.Weapons.ChocolateBar import ChocolateBar
from assets.Weapons.NerdBomb import NerdBomb
from EventHandler import Observer

# Player class is an observer of its weapons. Receives info on whether or not the weapon has broke.
class Player(Observer):
    # Used for player movement directions.
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 3

    def __init__(self):
        # Random drawing configuration variables.
        self.config = {"COLOR": (255, 255, 255),
                       "OUTLINE": (0, 0, 0),
                       "SIZE": 25,
                       "OUTLINE_WIDTH": 1}

        self.position = (0, 0) # Start player in the middle of the world.
        self.health = random.randint(100, 125)
        self.maxHealth = self.health
        self.strength = random.randint(10, 20)
        self.inventory = [HersheyKiss()] # Ensures the player always has a HersheyKiss weapon.

        # Populate the rest of the player's inventory with weapons.
        for i in range(9):
            self.addWeapon()

    # Add weapon method used in initialization and searching houses.
    def addWeapon(self):
        possibleWeapons = [SourStraw, ChocolateBar, NerdBomb]
        addedWeapon = random.choice(possibleWeapons)()
        Observer.__init__(self, addedWeapon)  # Register the weapon with the observer. (For when it breaks.)
        self.inventory.append(addedWeapon)
        return addedWeapon

    # Player movement, given the current keys down.
    def move(self, keys):
        if keys[pygame.K_a]:
            self.position = (self.position[0]-1, self.position[1])
        if keys[pygame.K_w]:
            self.position = (self.position[0], self.position[1]-1)
        if keys[pygame.K_d]:
            self.position = (self.position[0]+1, self.position[1])
        if keys[pygame.K_s]:
            self.position = (self.position[0], self.position[1]+1)

    # Interacts with a house by initializing a FightMenu for that house.
    def interact(self, House, Cleared):
        return FightMenu(self, House, Cleared)

    # Player takes damage, clamping the health within the bounds of 0 and maxHealth.
    def take_damage(self, damage):
        self.health = self.health-damage
        self.health = max(min(self.health, self.maxHealth), 0)

    # Attacks a monster with a specific weapon.
    def attack(self, weapon, monster):
        damage = self.strength * weapon.damage_modifier()
        trueDamage = monster.take_damage(damage, weapon)  # Gets/returns the damage taken by the monster.
        # The reason we do this is because some monsters have immunity/modifiers for certain weapons.
        return trueDamage

    # Returns the first instance of a specific weapon type.
    def get_weapon(self, weaponClass):
        for i in range(len(self.inventory)):
            if self.inventory[i].__class__ == weaponClass:
                return self.inventory[i]
        return None

    # Returns the number of weapon types in a player's inventory.
    def get_inventory_count(self):
        ChocolateBarCount, SourStrawCount, NerdBombCount = 0, 0, 0

        for weapon in self.inventory:
            if weapon.__class__ == ChocolateBar:
                ChocolateBarCount += 1
            elif weapon.__class__ == SourStraw:
                SourStrawCount += 1
            elif weapon.__class__ == NerdBomb:
                NerdBombCount += 1

        return "Unlimited", ChocolateBarCount, SourStrawCount, NerdBombCount

    # When received, it means the weapon broke.
    def receive(self, *args, **kwargs):
        self.inventory.remove(args[0]) # Remove the boken weapon from the player's inventory.


    ##################################################
    # "Non-Functional" Drawing Methods
    ##################################################
    def draw(self, window):
        WIDTH = window.get_width();
        HEIGHT = window.get_height();
        pygame.draw.circle(window, self.config["OUTLINE"], (WIDTH/2, HEIGHT/2), self.config["SIZE"])
        pygame.draw.circle(window, self.config["COLOR"], (WIDTH/2, HEIGHT/2), self.config["SIZE"]-(self.config["OUTLINE_WIDTH"]*2))