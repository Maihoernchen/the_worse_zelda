import random
from . import player

class sonderbonbon:
    name = "sonderbonbon"
    icon = "reccources/sonderbonbon.png"
    def use(self):
        stats = player.stats()
        inventory = player.inventory()
        stats.levelup()
        inventory.delete("sonderbonbon")

class backpack:

    slots = 25

class light_leather_armor:
    armor = 5
    slow = 0
    durability = 60

class nothing:
    name = "nothing"
    damage = 5
    armor = 1
    slow = 0
    durability = None

class axe:
    damage = random.choice([0,10])

