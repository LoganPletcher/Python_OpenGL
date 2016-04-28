import pygame
from pygame import *
import sys
from sys import *
import Nodes
from Nodes import *
import math
from math import *
import random
from random import *

class AstarAlg:
    '''Requires the length and height of the grid, the y & x of the starting/agent node, and the y & x of the objective node'''
    def __init__(self, (glength, gheight), (ay, ax), (oy, ox)):
        self.nodes = []
        '''These for loops create all the nodes that will populate the grid.'''
        for y in range(0, glength):
            noderow = []
            for x in range(0, gheight):
                node = Nodes.Node(y,x)
                noderow.append(node)
            self.nodes.append(noderow)
        '''The starting node, aka the "agent" node.'''
        self.anode = self.nodes[ay][ax]
        '''The node that the algorithm runs checks in relation to. The current node.'''
        self.cnode = self.anode
        '''The goal or "objective" node for the algorithm.'''
        self.onode = self.nodes[oy][ox]
        self.openList = []
        self.closedList = []

    '''Function that uses the pythagorean theorem to find the diagonal distance between two points and returns the result.
       Used for finding the g of a node.'''
    def pythag(self, node, cnode):
        A = cnode.pos[0] - node.pos[0]
        B = cnode.pos[1] - node.pos[1]
        Asqr = A * A
        Bsqr = B * B
        Csqr = Asqr + Bsqr
        return int((sqrt(Csqr)*10))

    '''Function that finds the manhattan distance between two points and returns the result.
       Used for finding the h of a node.'''
    def manhattan(self, node, onode):
        A = onode.pos[0] - node.pos[0]
        B = onode.pos[1] - node.pos[1]
        if A < 0: A = -A
        if B < 0: B = -B
        ManDist = (A) + (B)
        return (ManDist * 10)

    '''Function that finds all the walkable neighbors of the current node and adds them to a list that is returned.'''
    def neighbors(self):
        Adj = []
        for y, noderow in enumerate(self.nodes):
            for x, node in enumerate(noderow):
                if node == self.cnode:
                    currN = (y, x)
        for y, noderow in enumerate(self.nodes):
            for x, node in enumerate(noderow):
                if (self.nodes[y][x].walkable == True) and ((currN[0]-1 <= y <= currN[0]+1) and (currN[1]-1 <= x <= currN[1]+1)):
                    Adj.append(self.nodes[y][x])
        return Adj

    '''Function that sets the h value for all the nodes.'''
    def Hsetter(self):
        for noderow in self.nodes:
            for node in noderow:
                node.setH(int(self.manhattan(node, self.onode)))

    '''Function that takes in a list of nodes adjecent to the current node and sets their parent, g,
       and adds them to the openList if they are not in the openList or the closedList.
       If they are in the openList or closedList it checks to see if the current node is a better parent than the node's current parent node.'''
    def AdjacentSorter(self, Adj):
        for node in Adj:
            if node not in self.openList and node not in self.closedList:
                node.parent = self.cnode
                node.setG(self.pythag(node, self.cnode))
                self.openList.append(node)
            else:
                cost = self.cnode.g + self.pythag(node, self.cnode)
                if (cost < node.g):
                    node.parent = self.cnode
                    node.setG(cost)
    
    '''Function that runs the first part of the Astar algorithm that shouldn't be looped.'''
    def AlgorithmS(self):
        self.Hsetter()
        self.closedList.append(self.anode)
        self.AdjacentSorter(self.neighbors())

    '''Function that runs the part of the Astar algorithm that should be looped.'''
    def AlgorithmL(self):
        self.openList.sort(key = lambda x : x.f)
        '''Sorts the openList by the lowest f score of the contained nodes and sets the current node to the node with the lowest f.'''
        self.cnode = self.openList[0]
        self.closedList.append(self.cnode)
        '''Adds the current node to the closedList and removes it from the openList'''
        self.openList.remove(self.cnode)
        self.AdjacentSorter(self.neighbors())

    '''Function to randomly set a passed in number of nodes as unwalkable.'''
    def UnwalkableGenerator(self, num):
        maxY = 0
        maxX = 0
        for noderow in self.nodes:
            maxY += 1
        for node in self.nodes[0]:
            maxX += 1
        for i in range(0,num):
            y = randrange(0,maxY)
            x = randrange(0,maxX)
            while self.nodes[y][x] is self.anode or self.nodes[y][x] is self.onode:
                y = randrange(0,maxY)
                x = randrange(0,maxX)
            self.nodes[y][x].setWalk(False)

'''
ASalg = AstarAlg((11,11),(10,10),(5,2))
ASalg.UnwalkableGenerator(54)
ASalg.AlgorithmS()
while True:
    if ASalg.cnode == ASalg.onode:
        break
    else:
        ASalg.AlgorithmL()
for noderow in ASalg.nodes:
    for node in noderow:
        if node == ASalg.cnode:
            currentnode = node
            while currentnode.parent:
                print (currentnode.pos,'->',currentnode.parent.pos)
                currentnode = currentnode.parent
'''

















