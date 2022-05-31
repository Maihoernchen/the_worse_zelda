from . import player

class villager:
    used = False
    def talkto(self,line,item):
        item = item()
        inventory = player.inventory()
        print(line)
        inventory.add(item)
        return line,item

class mountain_villager (villager):
    image = "reccources/southstandv.png"
    
