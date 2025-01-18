class enemy():
    def __init__(self,hitPoints):
        self.hitPoints = hitPoints

    def getHitPoints(self):
        return self.hitPoints
    
    def setHitPoints(self, newVal):
        self.hitPoints = newVal