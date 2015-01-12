# *********************************************************************
# System imports ...
# *********************************************************************
import random
import sys
import time
import pygame
from pygame.locals import *

# *********************************************************************
# Constants ...
# *********************************************************************
N_ROWS = 7	# Number of rows of Maze
N_COLS = 7 	# Number of columns of Maze

PICE_WIDTH = 96
PICE_HEIGHT = 96
MARGIN = 50

WINDOW_WIDTH = N_COLS * PICE_WIDTH + 2 * MARGIN
WINDOW_HEIGHT = N_ROWS * PICE_HEIGHT + 2 * MARGIN

# There are 4 types of pices:
PICE_TYPE = ('I', 'T', 'L', 'X')

# *********************************************************************
# Class Block
# *********************************************************************
class Block:
	blocktype = None
	blockangle = 0

	def __init__(self, bt, angle = 0):
		self.blocktype = bt
		self.blockangle = angle

	def rotate(self):
		self.blockangle += 90 % 360

# *********************************************************************
# Class Maze
# *********************************************************************
class Maze:
    def __init__(self):
    	for row in range(N_ROWS):
    		for col in range(N_COLS):
    			self.maze[row][col] = Block()



# *********************************************************************
# Main Program ...
# *********************************************************************


# *********************************************************************
# Graphic part ...
# *********************************************************************
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # , pygame.RESIZABLE)
pygame.display.set_caption("Maze!")
##pygame.display.set_icon(pygame.image.load(LOGO_ICO))
pygame.font.init()

screen.fill(BG_COLOR)
FontGame = pygame.font.SysFont("None", 36, True)  # Default sysfont, size=12 and bold

while True:
    for event in pygame.event.get():
        if (event.type == QUIT):
            sys.exit(0)
        elif (event.type == KEYDOWN):  # Key pressed ...
            keys = pygame.key.get_pressed()  # Witch key?
            if keys[K_n]:  # Test key in keys[]
                pass
            elif keys[K_h]:
                pass
            elif keys[K_s]:
                pass
        elif (event.type == KEYUP):  # Key released ...
            if event.key == pygame.K_q:
                sys.exit(0)
        else:  # Other events ...
            pass
