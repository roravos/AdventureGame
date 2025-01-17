from player import player
from enemy import enemy
from playerturn import *
from enemyturn import *

p = player(10)
e = enemy(10)
pturn = playerturn(p,e)
eturn = enemyturn(p,e)

while (p.hitPoints != 0 and e.hitPoints != 0):
    pturn.action()
    eturn.action()


