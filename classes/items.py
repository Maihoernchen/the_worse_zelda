import random
from . import player

class sonderbonbon:
    name = "sonderbonbon"
    def eat(self):
        player.stats.levelup()
        player.inventory.delete("sonderbonbon")

class backpack:

    slots = 10

class light_leather_armor:
    armor = 5
    slow = 0
    durability = 60

class nothing:
    damage = 5
    armor = 1
    slow = 0
    durability = None

class axe:
    damage = random.choice([0,10])

