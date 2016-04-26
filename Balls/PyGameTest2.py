import pygame
from pygame import *
from pygame.locals import *
import sys
from sys import *
import Nodes
from Nodes import *
import math
from math import *
from time import sleep
import lowestnum
from lowestnum import *

def pythag(node, cnode):
    A = onode.pos[0] - node.pos[0]
    B = onode.pos[1] - node.pos[1]
    Asqr = A * A
    Bsqr = B * B
    Csqr = Asqr + Bsqr
    return (sqrt(Csqr)*10)

def manhattan(node, onode):
    A = onode.pos[0] - node.pos[0]
    B = onode.pos[1] - node.pos[1]
    if A < 0: A = -A
    if B < 0: B = -B
    ManDist = (A*10) + (B*10)
    return ManDist


def neighbors(cnode, nodes, openList, onode, closedList):
    Adj = []
    for y, noderow in enumerate(nodes):
        for x, node in enumerate(noderow):
            if node == cnode:
                curry = (y, x)
    for y, noderow in enumerate(nodes):
        for x, node in enumerate(noderow):
            if (nodes[y][x].walkable == True) and ((curry[0]-1 <= y <= curry[0]+1) and (curry[1]-1 <= x <= curry[1]+1)):
                Adj.append(nodes[y][x])
    return Adj

pygame.init()
#pygame.font.init()
screen = pygame.display.set_mode((1605,905))
keys = pygame.key.get_pressed()
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
lightBlue = (100,100,255)
cyan = (0,255,255)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)
yellow = (255,255,0)
purple = (200,0,200)
hotpink = (255,0,200)

screen.fill(green)

nodes = []

for y in range(0,64):
    noderow = []
    for x in range(0,36):
        node = Nodes.Node(y,x)
        noderow.append(node)
    nodes.append(noderow)

anode = nodes[63][35]
cnode = anode
onode = nodes[5][2]

for i in range(0,3):
    if not i == 1:
        nodes[4][i+1].setWalk(False)
for i in range(0,3):
    nodes[6][i+1].setWalk(False)
nodes[5][3].setWalk(False)
nodes[5][1].setWalk(False)

openList = [] #Nodes that the current node can and could walk to
closedList = [] #Nodes that the current node has already walked to

for noderow in nodes:
    for node in noderow:
        if node == cnode:
            node.setG(0)
            node.setH(int(manhattan(node, onode) * 10))
            openList.append(node)
        else:
            continue
        
neighbors(cnode, nodes, openList, onode, closedList)

gamerunning = True

while True:
    if keys[K_a]:
        if gamerunning:
            gamerunning = False
        else:
            gamerunning = True
    
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        '''if event.type==KEYDOWN:
            if '''
                
    for noderow in nodes:
        for node in noderow:
            node.draw(screen,green)

    if gamerunning:
        if not cnode == onode:
            for noderow in nodes:
                for node in noderow:
                    if node == cnode:
                        closedList.append(cnode)
                        openList.remove(node)

    if gamerunning:
        if not cnode == onode:
            Adj = neighbors(cnode, nodes, openList, onode, closedList)

    if gamerunning:
        if not cnode == onode:
            for node in Adj:
                if node not in closedList:
                    if node not in openList:
                        if onode in openList:
                            print("Got em")
                        else:
                            node.parent = cnode
                            node.setG(int(pythag(node, cnode)))
                            node.setH(manhattan(node, onode))
                            openList.append(node)
                    else:
                        cost = cnode.g + int(pythag(node, cnode))
                        if (cost < node.g):
                            node.parent = cnode
                            node.setG(cost)
        
    for node in openList:
        pygame.draw.rect(screen, darkBlue,
                         (node.left, node.top, node.width, node.height))
    for node in closedList:
        pygame.draw.rect(screen, lightBlue,
                         (node.left, node.top, node.width, node.height))
            
    pygame.draw.rect(screen, purple,
                         (onode.left, onode.top, onode.width, onode.height))
        
    pygame.draw.rect(screen, yellow,
                         (anode.left, anode.top, anode.width, anode.height))
        
    if not cnode == onode:
        pygame.draw.rect(screen, cyan,
                         (cnode.left, cnode.top, cnode.width, cnode.height))
            
    if cnode == onode:
        for noderow in nodes:
            for node in noderow:
                if node == cnode:
                    currentnode = node
                    while currentnode.parent:
                        pygame.draw.line(screen, hotpink,
                                         (currentnode.left+10, currentnode.top+10), (currentnode.parent.left+10, currentnode.parent.top+10), 2)
                        currentnode = currentnode.parent
                    gamerunning = False

    if gamerunning:
        if not cnode == onode:
            Fs = []
            for node in openList:
                Fs.append(node.getF())
                if node.getF() == lowestnum.MinNumFinder(Fs):
                    cnode = node

        '''if gamerunning:
            sleep(1)'''
    pygame.display.update()
