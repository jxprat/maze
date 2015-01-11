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
N_ROWS = 9		# Number of rows of Maze
N_COLS = 9 	# Number of columns of Maze

PICE_WIDTH = 96
PICE_HEIGHT = 96
# There are 4 types of pices:
MAZE_PICE_I = '' # Vertical/Horizontal pices
MAZE_PICE_T = '' # Type T
MAZE_PICE_L = '' # Type corner
MAZE_PICE_X = '' # Type Cross

# *********************************************************************
# Class Block
# *********************************************************************
class Block:
	def __init__(self):
		self.blocktype = bt
		#self.

# *********************************************************************
# Class Maze
# *********************************************************************
class Maze:
    def __init__(self):
    	for row in range(N_ROWS):
    		for col in range(N_COLS):
    			self.maze[row][col] = Block()

