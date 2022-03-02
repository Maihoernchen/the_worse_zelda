import player

class mountain_villager_1:
    look = "reccources/npcs/mountain_villager_1"
    def talkto(self,line,item):
        print(line)
        player.inventory.add(item)
