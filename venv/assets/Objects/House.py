import random

from assets.NPCS import Person, Zombie, Werewolf, Vampire, Ghoul

class House():


    def __init__(self, position: (int, int), color: (int, int, int)):
        self.position = position
        self.color = color
        self.monsters = {"Person" : [],
                         "Zombie" : [],
                         "Werewolf" : [],
                         "Vampire": [],
                         "Ghoul" : []};

        monsterCount = random.randint(0, 10)
        numMonsters = 0;
        while (numMonsters < monsterCount):
            monsterType = random.choice(["Zombie", "Werewolf", "Vampire", "Ghoul"])
            if (monsterType == "Zombie"):
                self.monsters[monsterType].append(Zombie())
            if (monsterType == "Werewolf"):
                self.monsters[monsterType].append(Werewolf())
            if (monsterType == "Vampire"):
                self.monsters[monsterType].append(Vampire())
            if (monsterType == "Ghoul"):
                self.monsters[monsterType].append(Ghoul())