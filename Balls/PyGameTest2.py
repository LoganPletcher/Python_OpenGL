import pygame
from pygame import *
import sys
from sys import *
import Nodes
from Nodes import *
import math
from math import *
from time import sleep
import lowestnum
from lowestnum import *

def pythagorean(node, onode):
    A = onode.pos[0] - node.pos[0]
    B = onode.pos[1] - node.pos[1]
    if A < 0: A = -A
    if B < 0: B = -B
    ManDist = (A*10) + (B*10)
    return ManDist


def neighbors(cnode, nodes, openList, onode, closedList):
    for noderow in nodes:
        for node in noderow:
            if node.walkable == True:
                if node not in openList:
                    if node not in closedList:
                        if cnode not in closedList:
                            closedList.append(cnode)
                            openList.remove(cnode)
                        if node.pos[0] == cnode.pos[0]-1:
                            if node.pos[1] == cnode.pos[1]-1:
                                node.setG(14+cnode.g)
                                node.setH(int(pythagorean(node, onode) * 10))
                                for noderow2 in nodes:
                                    for node2 in noderow:
                                        if node2 == cnode:
                                            node.parent = node2
                                openList.append(node)
                            elif node.pos[1] == cnode.pos[1]:
                                node.setG(10+cnode.g)
                                node.setH(int(pythagorean(node, onode) * 10))
                                for noderow2 in nodes:
                                    for node2 in noderow:
                                        if node2 == cnode:
                                            node.parent = node2
                                openList.append(node)
                            elif node.pos[1] == cnode.pos[1]+1:
                                node.setG(14+cnode.g)
                                node.setH(int(pythagorean(node, onode) * 10))
                                for noderow2 in nodes:
                                    for node2 in noderow:
                                        if node2 == cnode:
                                            node.parent = node2
                                openList.append(node)
                        elif node.pos[0] == cnode.pos[0]:
                            if node.pos[1] == cnode.pos[1]-1:
                                node.setG(10+cnode.g)
                                node.setH(int(pythagorean(node, onode) * 10))
                                for noderow2 in nodes:
                                    for node2 in noderow:
                                        if node2 == cnode:
                                            node.parent = node2
                                openList.append(node)
                            elif node.pos[1] == cnode.pos[1]+1:
                                node.setG(10+cnode.g)
                                node.setH(int(pythagorean(node, onode) * 10))
                                for noderow2 in nodes:
                                    for node2 in noderow:
                                        if node2 == cnode:
                                            node.parent = node2
                                openList.append(node)
                        elif node.pos[0] == cnode.pos[0]+1:
                            if node.pos[1] == cnode.pos[1]-1:
                                node.setG(14+cnode.g)
                                node.setH(int(pythagorean(node, onode) * 10))
                                for noderow2 in nodes:
                                    for node2 in noderow:
                                        if node2 == cnode:
                                            node.parent = node2
                                openList.append(node)
                            elif node.pos[1] == cnode.pos[1]:
                                node.setG(10+cnode.g)
                                node.setH(int(pythagorean(node, onode) * 10))
                                for noderow2 in nodes:
                                    for node2 in noderow:
                                        if node2 == cnode:
                                            node.parent = node2
                                openList.append(node)
                            elif node.pos[1] == cnode.pos[1]+1:
                                node.setG(14+cnode.g)
                                node.setH(int(pythagorean(node, onode) * 10))
                                for noderow2 in nodes:
                                    for node2 in noderow:
                                        if node2 == cnode:
                                            node.parent = node2
                                openList.append(node)


pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((255,255))
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
purple = (255,0,255)
screen.fill(green)
nodes = []
for y in range(0,10):
    noderow = []
    for x in range(0,10):
        node = Nodes.Node(y,x)
        noderow.append(node)
    nodes.append(noderow)

agentnode = nodes[2][2]
cnode = nodes[2][2]
onode = nodes[6][2]

for i in range(0,3):
    nodes[4][i+1].setWalk(False)


openList = [] #Nodes that the current can and could walk to?
closedList = []
for noderow in nodes:
    for node in noderow:
        if node == cnode:
            node.setG(0)
            node.setH(int(pythagorean(node, onode) * 10))
            openList.append(node)
        else:
            continue
neighbors(cnode, nodes, openList, onode, closedList)
while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        #print (cnode.pos)
        for noderow in nodes:
            for node in noderow:
                node.draw(screen,green)
        #
        #if not openList:
        neighbors(cnode, nodes, openList, onode, closedList)
        for node in openList:
                pygame.draw.rect(screen, darkBlue,
                                 (node.left, node.top, node.width, node.height))
        for node in closedList:
            pygame.draw.rect(screen, lightBlue,
                             (node.left, node.top, node.width, node.height))
        pygame.draw.rect(screen, purple,
                         (onode.left, onode.top, onode.width, onode.height))
        pygame.draw.rect(screen, yellow,
                         (agentnode.left, agentnode.top, agentnode.width, agentnode.height))
        pygame.draw.rect(screen, cyan,
                         (cnode.left, cnode.top, cnode.width, cnode.height))
        if not cnode == onode:
            for node in openList:
                Fs = []
                for node2 in openList:
                    Fs.append(node2.getF())
                if node.getF() == lowestnum.MinNumFinder(Fs):
                    print (node.getF())
                    cnode = node
                    #closedList.append(node)
                    #openList.remove(node)
        
        sleep(1)
        pygame.display.update()
