import json

def fetchdata(savestate):
    f = open('gamedata.json')
    gamedata = json.load(f)
    tempdata = gamedata["savestates"][savestate]
    return tempdata