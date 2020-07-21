import pygame
from grid import Grid

surface = pygame.display.set_mode((600,600))
pygame.display.set_caption('Tic-tac-toe')

grid = Grid()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    surface.fill((0,0,0))

    grid.draw(surface)

    pygame.display.flip()