import pygame
import random
from assets.Objects.House import House
from assets.NPCS.Person import Person
from assets.Resources.Dialog import Dialog
from assets.UI.EndScreen import EndScreen

from assets.Weapons.HersheyKiss import HersheyKiss
from assets.Weapons.ChocolateBar import ChocolateBar
from assets.Weapons.SourStraw import SourStraw
from assets.Weapons.NerdBomb import NerdBomb

class FightMenu:
    # Fight menu variables used to determine the state of the fight.
    ACTIVE = -1
    FLED = 1
    LEFT = 2
    DEATH = 3
    WIN = 4

    def __init__(self, player, house, cleared):
        # Random drawing configuration variables.
        self.config = {"UI_MARGIN": 5,
                       "BORDER_THICKNESS": 1,
                       "COLOR_BACKGROUND": (40, 40, 40),
                       "COLOR_ACCENT": (200, 200, 200),
                       "COLOR_PRIMARY": (60, 60, 60),
                       "MONSTER_SPACING": 20,
                       "MONSTER_MARGIN": lambda numMonsters, WIDTH: WIDTH / 2 - (numMonsters * WIDTH / 25),
                       "MONSTER_MIN_Y": 300}

        self.player = player
        self.house = house
        self.cleared = cleared
        self.menuOptions = {"Attack": [],
                            "Flee": []}
        # Sets menu options if the player enters a house with no monsters in it.
        if self.house.monsterCount <= 0:
            self.menuOptions = {"Leave": [],
                                "Search": [],
                                "Sleep": []}
        self.displayOptions = list(self.menuOptions.keys())
        self.selectedOption = 0
        self.status = FightMenu.ACTIVE
        self.notificationQueue = [] # Used to display combat and relevant dialog.
        if self.house.home:
            self.notificationQueue.append("Momma! Papa! There's monsters everywhe-")
            self.notificationQueue.append("Oh, no... Not here, too!")
            self.notificationQueue.append("(This is your home. Take note.)")

        self.endscreen = None

    # Used to scroll up on the selected menu text.
    def scroll_up(self):
        if self.selectedOption > 0 and len(self.notificationQueue) <= 0:
            self.selectedOption -= 1

    # Used to scroll down on the selected menu text.
    def scroll_down(self):
        if (self.selectedOption < len(self.menuOptions)-1) and len(self.notificationQueue) <= 0:
            self.selectedOption += 1

    # Select the highlighted menu option and perform the necessary tasks.
    def select(self):
        # Displays the next notification in the notification queue.
        if len(self.notificationQueue) > 0:
            self.notificationQueue.pop(0)
            return

        if list(self.menuOptions.keys())[self.selectedOption] == "Leave": # Handles leaving.
            self.status = FightMenu.LEFT
        elif list(self.menuOptions.keys())[self.selectedOption] == "Search": # Handles searching.
            if (self.house.searched):
                self.notificationQueue.append("You find nothing of interest.")
            else:
                self.house.searched = True
                self.notificationQueue.append("You found a {0} in the house, and it's been added to your inventory.".format(self.player.addWeapon().__class__.__name__))
        elif list(self.menuOptions.keys())[self.selectedOption] == "Sleep": # Handles sleeping.
            if not self.house.home:
                self.notificationQueue.append("You can't just sleep in random people's houses!")
                return
            if self.house.home and self.cleared:
                self.notificationQueue.append("You collapse on your bed and immediately fall into a deep sleep...")
                self.status = self.WIN
                self.endscreen = EndScreen(self.status)
            else:
                self.notificationQueue.append("There's monsters everywhere! Now might not be the best time to do that.")
        elif list(self.menuOptions.keys())[self.selectedOption] == "Flee": # Handles fleeing.
            if (random.random() <= 0.4):
                self.status = FightMenu.FLED
            else:
                self.notificationQueue.append(random.choice(Dialog.FLEE_MESSAGES))
                self.performMonstersTurn()
        elif list(self.menuOptions.keys())[self.selectedOption] == "Attack": # Handles attacking.
            HersheyKissCount, ChocolateBarCount, SourStrawCount, NerdBombCount = self.player.get_inventory_count()
            self.menuOptions = {"Hershey Kiss (x{0})".format(HersheyKissCount): [],
                                "Chocolate Bar (x{0})".format(ChocolateBarCount): [],
                                "Sour Straw (x{0})".format(SourStrawCount): [],
                                "Nerd Bomb (x{0})".format(NerdBombCount): []}
            self.selectedOption = 0

        else:
            self.performPlayerTurn()
            self.selectedOption = 0

    # Method to perform a player's turn.
    def performPlayerTurn(self):
        weapons = [HersheyKiss, ChocolateBar, SourStraw, NerdBomb]
        selectedWeapon = self.player.get_weapon(weapons[self.selectedOption])

        if selectedWeapon == None:
            self.notificationQueue.append("You do not have any of that weapon.")
            return

        for monster in self.house.monsters:
            if not monster.health <= 0 and not monster.__class__ == Person:
                damage = self.player.attack(selectedWeapon, monster)
                self.notificationQueue.append(
                    "You attacked {0} with a {1} and did {2} damage.".format(monster.__class__.__name__,
                                                                           selectedWeapon.__class__.__name__,
                                                                           format(damage, '.2f')))

        if selectedWeapon.use() == 0:
            self.notificationQueue.append("Your weapon has broke.")

        self.performMonstersTurn()

        if self.house.monsterCount <= 0:
            self.menuOptions = {"Leave": [],
                                "Search": [],
                                "Sleep": []}
        else:
            self.menuOptions = {"Attack": [],
                                "Flee": []}

    def performMonstersTurn(self):
        amountHealed = 0
        badGuys = []
        for monster in self.house.monsters:
            if monster.__class__ == Person:
                amountHealed += 1
            else:
                badGuys.append(monster)

        if len(badGuys) > 0:
            attackingMonster = random.choice(badGuys)
            damage = attackingMonster.attack()
            self.player.take_damage(damage)
            self.notificationQueue.append(
                "{0} attacked you and did {1} damage.".format(attackingMonster.__class__.__name__,
                                                              format(damage, '.2f')))
            if self.player.health <= 0:
                self.status = self.DEATH
                self.endscreen = EndScreen(self.status)
                self.notificationQueue.append("As the monster tears into your halloween candy bag, you ponder...")
                self.notificationQueue.append("Why...?")
                self.notificationQueue.append("Your candy falls to the floor in slow motion...")
                return

        if (amountHealed > 0):
            self.player.take_damage(amountHealed*-1)
            self.notificationQueue.append("{0} {1} feeling normal again and {2} you candy. You gain {0} health.".format(amountHealed,
                                                                                                                          "people are" if amountHealed>1 else "person is",
                                                                                                                          "toss" if amountHealed>1 else "tosses"))


    ##################################################
    # "Non-Functional" Drawing Methods
    ##################################################
    def draw(self, window):
        if self.endscreen and len(self.notificationQueue)<=0:
            self.endscreen.draw(window)
            return

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
        if len(self.notificationQueue) <= 0:
            font = pygame.font.SysFont("Verdana", 32)
            for i in range(len(self.menuOptions.keys())):
                menuOption = font.render(list(self.menuOptions.keys())[i], True, (255, 200, 200) if (i == self.selectedOption) else (160, 160, 160))
                window.blit(menuOption, (self.config["UI_MARGIN"]*2 + self.config["BORDER_THICKNESS"],
                                         (((HEIGHT/5)*4) + self.config["UI_MARGIN"]) + self.config["BORDER_THICKNESS"] + (i*font.get_height())))
        else:
            font = pygame.font.SysFont("Segoe UI", 48)
            notificationText = font.render(self.notificationQueue[0], True, (255, 255, 255))
            continueText = font.render("Press SPACE to continue...", True, (255, 255, 255))
            window.blit(notificationText, (self.config["UI_MARGIN"]*2 + self.config["BORDER_THICKNESS"],
                                           (((HEIGHT/5)*4) + self.config["UI_MARGIN"]) + self.config["BORDER_THICKNESS"]))
            window.blit(continueText, (self.config["UI_MARGIN"]*2 + self.config["BORDER_THICKNESS"],
                                       (((HEIGHT/5)*4) + self.config["UI_MARGIN"]) + self.config["BORDER_THICKNESS"] + font.get_height()))

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