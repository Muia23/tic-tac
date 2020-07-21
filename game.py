import pygame


surface = pygame.display.set_mode((700,700))
pygame.display.set_caption('Tic-tac-toe')

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    surface.fill((0,0,0))        
    pygame.display.flip()