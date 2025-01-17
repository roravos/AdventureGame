import random

class playerturn():
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def action(self):
        print(self.player.hitPoints,",",self.enemy.hitPoints)
        playerChoice = ""
        playerChoice = input()
        if (playerChoice == "a"):
            self.enemy.hitPoints = self.enemy.hitPoints - random.randint(0,3)