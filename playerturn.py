import random
from item import *

class playerturn():
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def action(self):

        playerChoice = ""
        playerChoice = input()

        if (playerChoice == "a"):
            self.enemy.hitPoints = self.enemy.hitPoints - random.randint(0,3)
        if (playerChoice == "i"):
            print("Item Name:")
            itemName = input()
            self.player.usePlayerItem(itemName)
        
