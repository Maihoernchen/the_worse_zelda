import pygame
import time
from classes import player
from classes import items

def main():
    pygame.init()

    win = pygame.display.set_mode((600,600))
    pygame.display.set_caption("The Worse Zelda")
    pygame.mouse.set_visible(False)
    mx = 0
    my = 0

    def drawGrid(mx,my):
        rect = pygame.Rect(mx+2.5, my+2.5, 115, 115)
        pygame.draw.rect(win,(255,255,255),rect, 2)
        blockSize = 120 #Set the size of the grid block
        for x in range(0, 600, blockSize):
            for y in range(0, 600, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(win, (255,255,255), rect, 1)
    while True:
        pygame.time.delay(75)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            return True
        if keys[pygame.K_UP] and my>20:
            my -=120
        elif keys[pygame.K_DOWN] and my<480:
            my +=120
        elif keys[pygame.K_LEFT] and mx>20:
            mx -=120
        elif keys[pygame.K_RIGHT] and mx<480:
            mx +=120
        win.fill((0,0,0))
        drawGrid(mx,my)
        for dt in range(len(player.inventory.stuff)):
            print(player.inventory.stuff)
            if player.inventory.stuff[dt] == "sonderbonbon":
                it = pygame.image.load(items.sonderbonbon.icon)
                win.blit(it, (dt*120+10,dt*120+10))
        pygame.display.update()