import pygame

def show():
    selected = 0
    run = True
    pygame.init()
    win = pygame.display.set_mode((600,600))
    pygame.display.set_caption("Moving rectangle")
    pygame.mouse.set_visible(False)
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN] and selected<2:
            selected += 1
        if keys[pygame.K_UP] and selected>0:
            selected -= 1
        if keys[pygame.K_SPACE] :
            run = False
        print(selected)
    
    return selected