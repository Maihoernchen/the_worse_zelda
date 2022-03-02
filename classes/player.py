from . import items

class inventory:
    slots = 10
    stuff = []
    def add(self,item):
        self.stuff.append(item)

class equipped:
    head = items.nothing
    body = items.light_leather_armor
    leggs = items.nothing
    hand = items.nothing
    def equip(self,slot,item):
        self.slot = item

class stats:
    damage = equipped.hand
    defense = equipped.head.armor + equipped.body.armor + equipped.leggs.armor
    hp = 5

class spells:
    def attacke(self):
        print("achne")
