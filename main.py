import pygame
import time
import fetch
import startmenu

# containersize: 48px
# doubled: 96px

left_collide = []
right_collide = []
up_collide = []
down_collide = []

gameinfo = fetch.fetchdata(0)

pygame.init()

bg = pygame.image.load("MapImages/mountvillage.png")

win = pygame.display.set_mode((600,600))

# set the pygame window name
pygame.display.set_caption("Moving rectangle")
pygame.mouse.set_visible(False)

# object current co-ordinates
x = 100
y = 100


BLACK = (0, 0, 0)
WHITE = (200, 200, 200)

# dimensions of the object
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
	    # creates time delay of 10ms
	pygame.time.delay(10)

	for event in pygame.event.get():

		print(x,y)

		if event.type == pygame.QUIT:

			run = False

	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT] and x>0 and x not in left_collide:

		x -= 12

	if keys[pygame.K_RIGHT] and x<600:

		# increment in x co-ordinate
		x += 12

	# if left arrow key is pressed
	if keys[pygame.K_UP] and y>0:

		# decrement in y co-ordinate
		y -= 12

	# if left arrow key is pressed
	if keys[pygame.K_DOWN] and y<600:

		y += 12

	if x == 0 and y == 0:

		situation = "combat"
		blink(3)

	win.fill((0, 0, 0))
	win.blit(bg, (-x, -y))

	pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))

	pygame.display.update()

	while situation == "combat" and run:
		for event in pygame.event.get():

			if event.type == pygame.QUIT:

				run = False

		win.fill((255,255,255))
		win.blit(bg, (0-x,0-y))
		pygame.display.update()

pygame.quit()
