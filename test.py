from classes import player as player
from classes import monster as monster
from classes import npcs as npcs
from classes import items as items
from gamesave import fetchdata
from gamesave import pushdata
from startmenu import show

savestate = show()
gameinfo = fetchdata(savestate)

player.stats.hp = gameinfo["hp"]
player.stats.level = gameinfo["level"]

print(gameinfo)

ork = monster.ork()
you = player.stats()

print("You got attacked by an Ork!")
ork.attack()
print(you.hp)

pushdata(0,"hp",you.hp)