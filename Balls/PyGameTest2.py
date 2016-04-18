import pygame
from pygame import *

pygame.init()
pygame.font.init()

background = [1, 1, 2, 2, 2, 1]
playerpos = 3
leftmove = 0

size = width, height = 1600, 900
speed = [500, 500]
black = 0, 0, 0
red = 255, 0, 0

surfa = pygame.Surface((10, 10), 0, 0, (1, 1, 1, 1))

screen = pygame.display.set_mode(size)
pygame.draw.rect(surfa,red,(1,1,10,10))


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
