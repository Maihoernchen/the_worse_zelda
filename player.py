class inventory:
    slots = 10
    stuff = []
    def add(self,item)
        self.stuff.append(item)

class equipped:
    head = ''
    body = ''
    leggs = ''
    hand = ''
    def equip(self,slot,item):
        self.slot = item

class stats:
    damage = hand
    defense = head.armor + body.armor + leggs.armor
    hp = 5
