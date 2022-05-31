import pygame
import time

def main():
    pygame.init()

    win = pygame.display.set_mode((600,600))
    pygame.display.set_caption("The Worse Zelda")
    pygame.mouse.set_visible(False)
    mx = 0
    my = 0

    def drawGrid(mx,my):
        blockSize = 120 #Set the size of the grid block
        for x in range(0, 600, blockSize):
            for y in range(0, 600, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(win, (255,255,255), rect, 1)
        rect = pygame.Rect(mx, my, blockSize, blockSize)
        pygame.draw.rect(win,(0,0,0),rect, 2)
    while True:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            return True
        if keys[pygame.K_UP] and my>120:
            my -=120
        elif keys[pygame.K_DOWN] and my<500:
            my +=120
        elif keys[pygame.K_LEFT] and mx>120:
            mx -=120
        elif keys[pygame.K_RIGHT] and mx<600:
            mx +=120
        drawGrid(mx,my)
        pygame.display.update()