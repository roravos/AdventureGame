
items = []

class player():
    def __init__(self,hitPoints):
        self.hitPoints = hitPoints

    def getHitPoints(self):
        return self.hitPoints
    
    def setHitPoints(self, newVal):
        self.hitPoints = newVal

    def addItem(self, thisItem):
        items.append(thisItem)

    def usePlayerItem(self, itemName):
        for x in items:
            print(x.itemtype)
            if x.itemtype == itemName:
                x.useItem()
