import sys
import pygame
import time
import gamesave
import invsceen
import combat
import startmenu
from classes import player
from classes import npcs
from classes import items
from classes import monster

pygame.init()

pygame.font.init()

font = pygame.font.SysFont("arial", 20)

inventory = player.inventory()
mountain_villager = npcs.mountain_villager()

class you(pygame.sprite.Sprite):
	image = pygame.image.load('reccources/southstand.png')
	x = 0
	y = 0
	rect = pygame.Rect(x,y,32,32)

selected = startmenu.show()

gameinfo = gamesave.fetchdata(selected)
hp = gameinfo["hp"]
inventory.stuff = gameinfo["inventory"]
bg = pygame.image.load(gameinfo["map"])
you.x,you.y = gameinfo["position"]
vel = 1
foot = "left"
f = 0
win = pygame.display.set_mode((600,600))
imag = ("reccources/southstand.png")
direction = "south"

def interact(x,y):
	if x < 221 and x > 204 and y > 154 and y < 180:
		if mountain_villager.used == False:
			line,item = mountain_villager.talkto("Hey there, I got a suprise for you!",items.sonderbonbon)	
			dialogue = font.render(line,True, (255,255,255),(0,0,0))
			win.blit(dialogue, (430-you.x,300-you.y))
			pygame.display.update()
			pygame.time.delay(2000)
			line = "You recieved" + item.name
			dialogue = font.render("You recieved: Sonderbonbon",True, (255,255,255),(0,0,0))
			win.fill((0, 0, 0))
			win.blit(bg, (-you.x, -you.y))
			win.blit(pygame.image.load(npcs.mountain_villager.image), (430-you.x,300-you.y))
			win.blit(you.image, (you.x,you.y))
			win.blit(dialogue, (430-you.x,300-you.y))
			pygame.display.update()
			pygame.time.delay(2000)
			mountain_villager.used = True
		elif mountain_villager.used == True:
			line,item = mountain_villager.talkto("Use it!",items.nothing)	
			dialogue = font.render(line,True, (255,255,255),(0,0,0))
			win.blit(dialogue, (430-you.x,300-you.y))
			pygame.display.update()
			pygame.time.delay(2000)
def toggle(foot):
	if foot == "left":
		foot = "right"
	else:
		foot = "left"
	return foot

pygame.display.set_caption("The Worse Zelda")
pygame.mouse.set_visible(False)

width = 48
height = 48

run = True
situation = "open"

def blink(times):

	i = 0

	while i < times:

		win.fill((0,0,0))
		pygame.display.update()
		pygame.time.delay(100)
		win.fill((255,255,255))
		pygame.display.update()
		pygame.time.delay(100)
		i +=1

while run:

	pygame.time.delay(10)

	for event in pygame.event.get():

		print(you.x,you.y)

		if event.type == pygame.QUIT:
			gamesave.pushdata(selected)
			run = False

	keys = pygame.key.get_pressed()

	if f%10 == 0:
		foot = toggle(foot)
 
	if keys[pygame.K_SPACE]:
		interact(you.x,you.y)
	elif keys[pygame.K_i]:
		invsceen.main()
	elif keys[pygame.K_LEFT] and you.x>0 and not keys[pygame.K_RIGHT] and not keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
		you.x -= vel
		f+=1
		direction = "west"
		imag = 'reccources/westwalk' + foot + '.png'
	elif keys[pygame.K_RIGHT] and you.x<600 and not keys[pygame.K_LEFT] and not keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
		you.x += vel
		f+=1
		direction = "east"
		imag = 'reccources/eastwalk' + foot + '.png'
	# if left arrow key is pressed
	elif keys[pygame.K_UP] and you.y>0:

		# decrement in y co-ordinate
		you.y -= vel
		f+=1
		direction = "north"
		imag = 'reccources/northwalk' + foot + '.png'
	# if left arrow key is pressed
	elif keys[pygame.K_DOWN] and you.y<600:
		you.y += vel
		f+=1
		direction = "south"
		imag = 'reccources/southwalk' + foot + '.png'
	elif keys[pygame.K_ESCAPE]:
		gamesave.pushdata(selected)
		run = False
	else:
		imag = 'reccources/'+ direction + 'stand.png'

	if you.x == 0 and you.y == 0:

		blink(3)
		combat.main(monster.ork)

	you.image = pygame.image.load(imag)
	win.fill((0, 0, 0))
	win.blit(bg, (-you.x, -you.y))
	win.blit(pygame.image.load(npcs.mountain_villager.image), (430-you.x,300-you.y))
	win.blit(you.image, (you.x,you.y))
	player.stats.position = you.x,you.y
	pygame.display.update()

pygame.quit()
