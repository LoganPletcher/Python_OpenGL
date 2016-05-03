import pygame
from pygame import *
import sys
from sys import *
import Nodes
from Nodes import *
from time import sleep
from AStar import AstarAlg
import random
from random import *

print("Enter the y value for the starting node. It should be a number under 31.")
try:
    ay = int(raw_input())
    if (ay > 30 or ay < 0)
        ay = randrange(0,31)
except ValueError:
    ay = randrange(0,31)
print("\nEnter the x value for the starting node. It should be a number under 23.")
try:
    ax = int(raw_input())
    if (ax > 22 or ay < 0)
        ax = randrange(0,23)
except ValueError:
    ax = randrange(0,23)
print("\nEnter the y value for the goal node. It should be a number under 31.")
try:
    oy = int(raw_input())
    if (oy > 30 or oy < 0)
        oy = randrange(0,31)
except ValueError:
    oy = randrange(0,31)
print("\nEnter the x value for the goal node. It should be a number under 23.")
try:
    ox = int(raw_input())
    if (ox > 22 or ay < 0)
        ox = randrange(0,23)
except ValueError:
    ox = randrange(0,23)
print("\nEnter the number of unwalkable nodes you want in the program.")
try:
    UnwalkNodes = int(raw_input())
    if (UnwalkNodes > 357 or UnwalkNodes < 0)
        UnwalkNodes = randrange(0,350)
except ValueError:
    UnwalkNodes = randrange(0,350)

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((780,580))
keys = pygame.key.get_pressed()

'''Defined colors that are used in the drawing of objects by being in an RGB format'''
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
lightBlue = (100,100,255)
cyan = (0,225,150)
white = (255,255,255)
black = (0,0,0)
grey = (127,127,127)
pink = (255,200,200)
yellow = (255,255,0)
purple = (200,0,200)
hotpink = (255,0,200)
orange = (255,127,20)

# Colors the background of the screen #
screen.fill(grey)

ASalg = AstarAlg((31,23),(ay,ax),(oy,ox))

ASalg.UnwalkableGenerator(UnwalkNodes)

ASalg.AlgorithmS()

# Draws all the nodes #
for noderow in ASalg.nodes:
        for node in noderow:
            node.draw(screen,green)
 
# The while loop of the program that will perform the looping part of the Astar algorithm and draw shapes to the screen. #
while True:
    if ASalg.onode is ASalg.cnode:
        break
    else:
        
        # Event cases that allows the user to exit the program in the middle of the program.
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        ASalg.AlgorithmL()

       # Colors the nodes in the openList #
        for node in ASalg.openList:
            pygame.draw.rect(screen, darkBlue,
                             (node.left, node.top, node.width, node.height))
       # Colors the nodes in the closedList #
        for node in ASalg.closedList:
            pygame.draw.rect(screen, orange,
                             (node.left, node.top, node.width, node.height))
       # Colors the objective node #
        pygame.draw.rect(screen, purple,
                             (ASalg.onode.left, ASalg.onode.top, ASalg.onode.width, ASalg.onode.height))
       # Colors the agent/starting node #
        pygame.draw.rect(screen, yellow,
                             (ASalg.anode.left, ASalg.anode.top, ASalg.anode.width, ASalg.anode.height))
       # Colors the current node #
        pygame.draw.rect(screen, cyan,
                         (ASalg.cnode.left, ASalg.cnode.top, ASalg.cnode.width, ASalg.cnode.height))

    sleep(.8) #Gives the program a .8 second delay
    pygame.display.update()
# End of the while loop. #################################################################################################

# Colors the objective node one last time to overwrite the current node color #
pygame.draw.rect(screen, purple,
                 (ASalg.onode.left, ASalg.onode.top, ASalg.onode.width, ASalg.onode.height))

# Draws that path from the objective to the starting/agent node #
for noderow in ASalg.nodes:
    for node in noderow:
        if node == ASalg.cnode:
            currentnode = node
            while currentnode.parent:
                pygame.draw.line(screen, hotpink,
                                 (currentnode.left+10, currentnode.top+10),
                                 (currentnode.parent.left+10, currentnode.parent.top+10), 2)
                currentnode = currentnode.parent
pygame.display.update()

# Allows the program to continue running until the user clicks the red 'X' in the top right of the screen window or until the user
# presses the 'Esc' key.
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                pygame.quit()
                sys.exit()
