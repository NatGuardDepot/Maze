from settings import *
import pygame
import math

class Player:
        def __init__(self):
             self.x, self.y = player_pos
             self.angle = player_angle

player_speed = 5

player = player.get_rect()
player.center = TILE // 2, TILE // 2
directions = {'a': (-player_speed, 0), 'd': (player_speed, 0), 'w': (0, -player_speed), 's': (0, player_speed)}
keys = {'a': pygame.K_a, 'd': pygame.K_d, 'w': pygame.K_w, 's': pygame.K_s}
direction = (0, 0)