import pygame
from random import choice
from settings import *
#from player import Player


pygame.init()
sc=pygame.display.set_mode(RES)
clock=pygame.time.Clock()
#player = Player()

class Cell:
    def __init__(self,x,y):
        self.x, self.y = x,y
        self.walls = {'top': True, 'bottom': True, 'left': True, 'right': True}
        self.visited = False
        self.thickness = 4

    def draw_current_cell(self):
        x, y = self.x * TILE, self.y * TILE
        pygame.draw.rect(sc, pygame.Color('black'), (x+2, y+2, TILE-2, TILE-2))

    def draw(self):
        x, y = self.x * TILE, self.y * TILE
        if self.visited:
            pygame.draw.rect(sc,pygame.Color('white'), (x, y, TILE, TILE))

        if self.walls['top']:
            pygame.draw.line(sc, pygame.Color('darkorange'), (x, y), (x + TILE, y), 2)
        if self.walls['right']:
            pygame.draw.line(sc, pygame.Color('darkorange'), (x + TILE, y), (x + TILE, y + TILE), 2)
        if self.walls['bottom']:
            pygame.draw.line(sc, pygame.Color('darkorange'), (x + TILE, y + TILE), (x , y + TILE), 2)
        if self.walls['left']:
            pygame.draw.line(sc, pygame.Color('darkorange'), (x, y + TILE), (x, y), 2)

    def check_cell(self,x,y):
        find_index = lambda x, y: x + y * cols
        if x < 0 or x > cols - 1 or y < 0 or y > rows - 1:
            return False
        return grid_cells[find_index(x, y)]

    def check_neighbours(self):
        neighbours = []
        top = self.check_cell(self.x, self.y - 1)
        right = self.check_cell(self.x + 1, self.y)
        bottom = self.check_cell(self.x, self.y + 1)
        left = self.check_cell(self.x - 1, self.y)
        if top and not top.visited:
            neighbours.append(top)
        if right and not right.visited:
            neighbours.append(right)
        if bottom and not bottom.visited:
            neighbours.append(bottom)
        if left and not left.visited:
            neighbours.append(left)
        return choice(neighbours) if neighbours else False

def remove_walls(current, next):
    dx = current.x - next.x
    if dx == 1:
        current.walls['left'] = False
        next.walls['right'] = False
    elif dx == -1:
        current.walls['right'] = False
        next.walls['left'] = False
    dy = current.y - next.y
    if dy == 1:
        current.walls['top'] = False
        next.walls['bottom'] = False
    elif dy == -1:
        current.walls['bottom'] = False
        next.walls['top'] = False

grid_cells = [Cell(col, row) for row in range(rows) for col in range(cols)]
current_cell = grid_cells[0]
stack = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            #player.movement()
    sc.fill(pygame.Color('black'))
    [cell.draw() for cell in grid_cells]
    current_cell.visited = True
    current_cell.draw_current_cell()

    next_cell = current_cell.check_neighbours()
    if next_cell:
        next_cell.visited = True
        stack.append(current_cell)
        remove_walls(current_cell, next_cell)
        current_cell = next_cell
    elif stack:
        current_cell = stack.pop()
        pygame.draw.circle(sc,GREEN,player_pos,12)


    pygame.display.flip()
    clock.tick(1000)