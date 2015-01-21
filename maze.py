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

PICE_SIZE = 72
MARGIN = 25 + PICE_SIZE

BLOCK_TYPE = ('I', 'T', 'C', 'X')
BLOCK_ANGLE = (0, 90, 180, 270)

WINDOW_WIDTH = N_COLS * PICE_SIZE + 2 * MARGIN
WINDOW_HEIGHT = N_ROWS * PICE_SIZE + 2 * MARGIN

BG_COLOR = (120, 50, 50)

# *********************************************************************
# Class Block
# *********************************************************************
class Block:
	def __init__(self, bt, angle = 0):
		self.blocktype = bt
		self.blockangle = angle

	def getblocktype(self):
		return self.blocktype

	def getblockangle(self):
		return self.blockangle

	def rotate(self):
		self.blockangle = (self.blockangle + 90) % 360

	def __str__(self):
		return self.blocktype + '(' + str (self.blockangle) + ')'


# *********************************************************************
# Class Maze
# *********************************************************************
class Maze:
    def __init__(self):
    	# Initialize the maze matrix ...
    	self.maze = [Block('I')] * N_ROWS
    	for i in range(N_ROWS):
    		self.maze[i] = [Block('I')] * N_COLS
    	# Randomize maze blocks ...
    	for i in range(N_ROWS):
    		for j in range(N_COLS):
    			b = random.choice(BLOCK_TYPE)
    			a = random.choice(BLOCK_ANGLE)
    			self.SetElement(i, j, Block(b, a))
    	# Set some fixed positions like corners ...
    	self.SetElement(0, 0, Block('C',90))
    	self.SetElement(0, N_COLS - 1, Block('C'))
    	self.SetElement(N_ROWS - 1, 0, Block('C',180))
    	self.SetElement(N_ROWS - 1, N_COLS - 1, Block('C',270))

    def SetElement(self, row, col, obj):
    	self.maze[row][col] = obj

    def GetElement(self, row, col):
    	return self.maze[row][col]

    def ScrollDown(self, col, block_in):
        b_in = block_in
        for row in range(N_ROWS):
            b_out = self.GetElement(row, col)
            self.SetElement(row, col, b_in)
            b_in = b_out
        return b_out

    def ScrollUp(self, col, block_in):
        b_in = block_in
        for row in range(N_ROWS - 1, -1, -1):
            b_out = self.GetElement(row, col)
            self.SetElement(row, col, b_in)
            b_in = b_out
        return b_out

    def ScrollHorizontal(self, row, dir, block_in):
        pass

    def __str__(self):
    	strmaze = ''
    	for row in range(N_ROWS):
    		strmaze += '\n'
    		for col in range(N_COLS):
    			aux_bl = self.GetElement(row,col)
    			strmaze += str(aux_bl)
    	return strmaze


# *********************************************************************
# Functions ...
# *********************************************************************
def load_image(bType):
	if(bType == 'I'):
		filename = 'images/b1.png'
	elif(bType == 'T'):
		filename = 'images/b2.png'
	elif(bType == 'C'):
		filename = 'images/b3.png'
	elif(bType == 'X'):
		filename = 'images/b4.png'
	image = pygame.image.load(filename)
	image = image.convert()
	return image

def DrawBlock(scr, maze, mazeRow, mazeCol):
	bl = maze.GetElement(mazeRow,mazeCol)
	bl_type = bl.getblocktype()
	bl_angle = bl.getblockangle()
	img = load_image(bl_type)
	xPos = MARGIN + PICE_SIZE * mazeCol
	yPos = MARGIN + PICE_SIZE * mazeRow
	scr.blit(img, (xPos, yPos))
	pygame.display.flip()

def DrawMaze(scr, maze):
	for row in range(N_ROWS):
		for col in range(N_COLS):
			DrawBlock(scr, maze, row, col)


# *********************************************************************
# Main Program ...
# *********************************************************************

# Testing part using characters ...
M = Maze()
ExtraBlock = M.GetElement(2,2)
print "Block [2][2]: ", ExtraBlock
print "Maze: ", M

# *********************************************************************
# Graphic part ...
# *********************************************************************
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # , pygame.RESIZABLE)
pygame.display.set_caption("Maze!")
##pygame.display.set_icon(pygame.image.load(LOGO_ICO))
pygame.font.init()

screen.fill(BG_COLOR)
FontGame = pygame.font.SysFont("None", 36, True)  # Default sysfont, size=12 and bold
pygame.display.flip()

# Draw initial Maze ...
DrawMaze(screen, M)

while True:
    for event in pygame.event.get():
        if (event.type == QUIT):
            sys.exit(0)
        elif (event.type == KEYDOWN):  # Key pressed ...
            keys = pygame.key.get_pressed()  # Witch key?
            if keys[K_n]:  # Test key in keys[]
                M = Maze()
                DrawMaze(screen, M)
            elif keys[K_d]:
                ExtraBlock = M.ScrollDown(3, ExtraBlock)
                DrawMaze(screen, M)
            elif keys[K_u]:
                ExtraBlock = M.ScrollUp(3, ExtraBlock)
                DrawMaze(screen, M)
            elif keys[K_s]:
                pass
        elif (event.type == KEYUP):  # Key released ...
            if event.key == pygame.K_q:
                sys.exit(0)
        else:  # Other events ...
            pass
