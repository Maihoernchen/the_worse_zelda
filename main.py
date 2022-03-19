import pygame
import time

pygame.init()

bg = pygame.image.load("MapImages/mountvillage.png")

win = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)

# set the pygame window name
pygame.display.set_caption("Moving rectangle")
pygame.mouse.set_visible(False)

# object current co-ordinates
x = 400
y = 400

# dimensions of the object
width = 20
height = 20

vel = 1

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
    while situation == "open" and run:
	    # creates time delay of 10ms
        pygame.time.delay(10)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x>0:

            x -= vel

        if keys[pygame.K_RIGHT] and x<960-width:

		# increment in x co-ordinate
            x += vel

	# if left arrow key is pressed
        if keys[pygame.K_UP] and y>0:

		# decrement in y co-ordinate
            y -= vel

	# if left arrow key is pressed
        if keys[pygame.K_DOWN] and y<540-height:

            y += vel

        if x == 0 and y == 0:

            situation = "combat"
            blink(3)

        win.fill((0, 0, 0))

        win.blit(bg, (0,0))

        pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))

        pygame.display.update()

    while situation == "combat" and run:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                run = False

        win.fill((255,255,255))
        win.blit(bg, (-50,-50))
        pygame.display.update()

pygame.quit()
