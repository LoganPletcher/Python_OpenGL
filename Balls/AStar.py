import pygame
from pygame import *
import sys
from sys import *
import Nodes
from Nodes import *
import math
from math import *
import lowestnum
from lowestnum import *

class AstarAlg:
    def __init__(self, (glength, gheight), (ay, ax), (oy, ox)):
        self.nodes = []
        for y in range(0, glength):
            noderow = []
            for x in range(0, gheight):
                node = Nodes.Node(y,x)
                noderow.append(node)
            self.nodes.append(noderow)
        self.anode = self.nodes[ay][ax]
        self.cnode = self.anode
        self.onode = self.nodes[oy][ox]
        self.openList = []
        self.closedList = []

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
        ManDist = (A) + (B)
        return ManDist

    def neighbors(self):
        Adj = []
        for y, noderow in enumerate(self.nodes):
            for x, node in enumerate(noderow):
                if node == self.cnode:
                    curry = (y, x)
        for y, noderow in enumerate(nodes):
            for x, node in enumerate(noderow):
                if (nodes[y][x].walkable == True) and ((curry[0]-1 <= y <= curry[0]+1) and (curry[1]-1 <= x <= curry[1]+1)):
                    Adj.append(nodes[y][x])
        return Adj

butt = AstarAlg((11,11),(10,10),(5,2))
