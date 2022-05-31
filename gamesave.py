import json
from classes import player
from classes import *

def fetchdata(savestate):
    f = open('gamedata.json')
    gamedata = json.load(f)
    tempdata = gamedata["savestates"][savestate]
    return tempdata

def pushdata(savestate):
    f = open('gamedata.json')
    gamedata = json.load(f)
    gamedata["savestates"][savestate]["hp"] = player.stats.hp
    gamedata["savestates"][savestate]["level"] = player.stats.level
    gamedata["savestates"][savestate]["position"] = player.stats.position
    gamedata["savestates"][savestate]["map"] = player.stats.map
    gamedata["savestates"][savestate]["inventory"] = player.inventory.stuff
    print(gamedata)
    tempgamedata = json.dumps(gamedata, indent = 4)
    with open('gamedata.json', 'w') as outfile:
        outfile.write(tempgamedata)
    return True