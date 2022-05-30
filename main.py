import pygame
import time
import gamesave
import startmenu
from classes import player

pygame.init()

class you(pygame.sprite.Sprite):
	image = pygame.image.load('reccources/southstand.png')
	x = 0
	y = 0
	rect = pygame.Rect(x,y,32,32)

selected = startmenu.show()

gameinfo = gamesave.fetchdata(selected)
hp = gameinfo["hp"]
bg = pygame.image.load(gameinfo["map"])
you.x,you.y = gameinfo["position"]


win = pygame.display.set_mode((600,600))


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


	if keys[pygame.K_LEFT] and you.x>0:
		you.x -= vel
		imag = 'reccources/westwalk' + foot + '.png'

	if keys[pygame.K_RIGHT] and you.x<600:
		you.x += vel
		imag = 'reccources/eastwalk' + foot + '.png'

	# if left arrow key is pressed
	if keys[pygame.K_UP] and you.y>0:

		# decrement in y co-ordinate
		you.y -= vel
		imag = 'reccources/northwalk' + foot + '.png'
	# if left arrow key is pressed
	if keys[pygame.K_DOWN] and you.y<600:
		you.y += vel
		imag = 'reccources/southwalk' + foot + '.png'
	if keys[pygame.K_ESCAPE]:
		gamesave.pushdata(selected)
		run = False
	if you.x == 0 and you.y == 0:

		situation = "combat"
		blink(3)

	you.image = pygame.image.load(imag)
	win.fill((0, 0, 0))
	win.blit(bg, (-you.x, -you.y))
	win.blit(you.image, (you.x,you.y))
	player.stats.position = you.x,you.y
	pygame.display.update()

	while situation == "combat" and run:
		for event in pygame.event.get():

			if event.type == pygame.QUIT:

				run = False

		win.fill((255,255,255))
		win.blit(bg, (0-x,0-y))
		pygame.display.update()

pygame.quit()
