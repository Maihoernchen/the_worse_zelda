from classes import player as player
from classes import monster as monster
from classes import npcs as npcs
from classes import items as items

ork = monster.ork()
you = player.stats()

print("You got attacked by an Ork!")
ork.attack()
print(you.hp)
