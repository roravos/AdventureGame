from player import player
from enemy import enemy
from playerturn import *
from enemyturn import *
from item import *

#Temporary. Will be created in adventure.py for final implementation
p = player(10)
e = enemy(10)
pturn = playerturn(p,e)
eturn = enemyturn(p,e)
i = item(3, "Healing",p)
p.addItem(i)

#incomplete. will be in a class and have its own method
while (p.hitPoints > 0 and e.hitPoints > 0):
    print(p.hitPoints,",",e.hitPoints) #Only implemented for testing
    pturn.action()
    eturn.action()

if (p.hitPoints <= 0):
    print("You Lose!")

if (e.hitPoints <= 0):
    print("You Win!")

