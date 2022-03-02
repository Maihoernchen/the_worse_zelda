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
        if self.damage > player.stats.defense:
            player.stats.hp -= self.damage
