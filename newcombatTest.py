from player import player
from enemy import enemy
from playerturn import *

p = player(10)
e = enemy(10)
pturn = playerturn(p,e)

pturn.action()
pturn.action()

