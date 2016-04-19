import pygame
from pygame import *
import sys
from sys import *
import Nodes
from Nodes import *
import collections
from collections import *

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((255,255))
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)
screen.fill(green)
nodes = Counter()
for i in range(0,10):
    for j in range(0,10):
        node = Nodes.Node(i,j)
        nodes[node] = (i * 10) + j

for node in nodes:
    node.draw(screen,green)

while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        #pygame.draw.rect(screen,(255,0,0),(0,0,30,30))
        pygame.display.update()
