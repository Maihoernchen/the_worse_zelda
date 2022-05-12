from . import items
from . import player

class ork:
    hp = 10
    head = items.nothing
    body = items.light_leather_armor
    leggs = items.nothing
    hand = items.axe
    defense = body.armor + head.armor + leggs.armor
    damage = hand.damage
    def attack(self):
        edamage = self.damage - player.stats.defense
        print(edamage)
        if self.damage > player.stats.defense:
            player.stats.hp -= edamage
        player.equipped.body.durability -= edamage
