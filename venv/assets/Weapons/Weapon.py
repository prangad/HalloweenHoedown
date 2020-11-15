from EventHandler import Observable

class Weapon(Observable):
    def __init__(self):
        Observable.__init__(self)
        self.damage_modifier = 1
        self.remaining_uses = -1

    def use(self):
        if self.remaining_uses >= 1:
            self.remaining_uses -= 1

        if self.remaining_uses == 0:
            self.destroy()

        return self.remaining_uses

    def destroy(self):
        self.notifyAll(self)