from turtle import position
from . import items
import sys

class equipped:
    head = items.nothing
    body = items.light_leather_armor
    hand = items.nothing
    backpack = items.backpack
    def equip(self,slot,item):
        self.slot = item

class inventory:
    slots = equipped.backpack.slots
    stuff = []
    def add(self,item):
        self.stuff.append(item.name)
    def delete(self,item):
        self.stuff.remove(item)

class stats:
    map = "MapImages/mountvillage.png"
    position = [100,200]
    level = 1
    hplist = [10,12,15,18,25,35]
    damage = equipped.hand.damage
    defense = equipped.body.armor
    hp = hplist[level]
    def levelup(self):
        self.level += 1

class spells:
    def attacke(self):
        print("achne")
