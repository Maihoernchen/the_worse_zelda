import pygame

def show():
    x = 350
    y = 257
    selected = 0
    run = True
    pygame.init()
    win = pygame.display.set_mode((600,600))
    pygame.display.set_caption("Startmenu")
    pygame.mouse.set_visible(False)
    bg = pygame.image.load('reccources/satrtmenu.png')
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN] and selected<2:
            selected += 1
            y += 100
        if keys[pygame.K_UP] and selected>0:
            selected -= 1
            y -= 100
        if keys[pygame.K_SPACE] :
            run = False
        print(selected)
        win.fill((255,255,255))
        win.blit(bg, (0,0))
        pygame.draw.rect(win, (255, 255, 255), (x,y, 24, 24))
        pygame.display.update()
    
    return selected