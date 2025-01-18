class item():
    def __init__(self, value, itemtype, char): #char = character. Can be a player or an enemy
        self.value = value
        self.itemtype = itemtype
        self.char = char

    def useItem(self):
        if self.itemtype == "Healing":
            currentHitPoints = self.char.getHitPoints() + self.value
            self.char.setHitPoints(currentHitPoints)

