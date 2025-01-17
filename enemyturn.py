import random

class enemyturn():
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
    
    def action(self):
        self.player.hitPoints = self.player.hitPoints - random.randint(0,3)
