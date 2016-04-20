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
yellow = (255,255,0)
purple = (255,0,255)
screen.fill(green)
nodes = []
for y in range(0,10):
    noderow = []
    for x in range(0,10):
        node = Nodes.Node(y,x)
        noderow.append(node)
    nodes.append(noderow)

cnode = nodes[2][2]
onode = nodes[6][2]

for i in range(0,3):
    nodes[4][i+1].setWalk(False)

openList = [] #Nodes that the current can and could walk to?

while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        print (cnode.pos)
        for noderow in nodes:
            for node in noderow:
                node.draw(screen,green)
        pygame.draw.rect(screen, purple,
                         (onode.left, onode.top, onode.width, onode.height))
        pygame.draw.rect(screen, yellow,
                         (cnode.left, cnode.top, cnode.width, cnode.height))
        pygame.display.update()
