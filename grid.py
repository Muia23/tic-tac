import pygame
import os

letterx = pygame.image.load(os.path.join('res', 'imagex.png'))
lettero = pygame.image.load(os.path.join('res', 'imageo.png'))

class Grid:
    def __init__(self):
        self.grid_lines = [((0,200), (600,200)),
                           ((0,400), (600,400)),
                           ((200,0), (200,600)),
                           ((400,0), (400,600))] 

        self.grid =[[0 for x in range(3)] for y in range(3)]        

    def draw(self, surface):
        for line in self.grid_lines:
            pygame.draw.line(surface, (200,200,200), line[0], line[1], 2)

        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.get_cell_value(x ,y) == "x":
                    surface.blit(letterx, (x*200, y*200))
                elif self.get_cell_value(x, y) == "o":
                    surface.blit(lettero, (x*200, y*200))

    def get_cell_value(self,x,y):
        return self.grid[y][x]
    
    def set_cell_value(self, x, y, value):
        self.grid[y][x] = value

    def get_mouse(self,x,y,player):
        if player == "x":
            self.set_cell_value(x, y, "x")
        elif player == "o":
            self.set_cell_value(x, y,"o")

    def print_grid(self):
        for row in self.grid:
            print(row)