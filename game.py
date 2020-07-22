import pygame
from grid import Grid

surface = pygame.display.set_mode((600,600))
pygame.display.set_caption('Tic-tac-toe')

grid = Grid()

running = True
player = "x"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:            
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()                
                grid.get_mouse(pos[0] // 200, pos[1] // 200, player)
                if player == "x":
                    player = "o"                    
                else:
                    player = "x"

                grid.print_grid()

    surface.fill((0,0,0))

    grid.draw(surface)

    pygame.display.flip()