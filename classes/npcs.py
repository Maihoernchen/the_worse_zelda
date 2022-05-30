from . import player

class villager:
    def talkto(self,line,item):
        print(line)
        player.inventory.add(item)

class mountain_villager (villager):
    look = "reccources/npcs/mountain_villager"
    
