import items
import player

class ork:
    hp = 10
    head = ''
    body = items.lightweight_leather_armor
    leggs = ''
    hand = ''
    defense = body.armor + head.armor + leggs.armor
    damage = hand.damage
    def attack(self):
        if self.damage > player.stats.defense:
            player.stats.hp -= self.damage
