from EventHandler import Observable

# Base class for all weapons.
class Weapon(Observable):
    def __init__(self):
        Observable.__init__(self)
        self.damage_modifier = 1
        self.remaining_uses = -1

    # Uses a weapon, and keeps track of its uses.
    def use(self):
        if self.remaining_uses >= 1:
            self.remaining_uses -= 1

        if self.remaining_uses == 0:
            self.destroy()

        return self.remaining_uses

    # Notifies the player of the weapon breaking and removes it from their inventory.
    def destroy(self):
        self.notifyAll(self)