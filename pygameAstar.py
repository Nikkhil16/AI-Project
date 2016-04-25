import numpy
from prettytable import PrettyTable
import pygame
import random
 

# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [200, 200]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("First TRY")
 
# Loop done?
done = False

clock = pygame.time.Clock()

##############################################
###########   A STAR   ############

def psbl_children(current,grid):
    possible_children = []
    if (current[1][0] + 1 < len(grid)) and (grid[current[1][0] + 1][current[1][1]]) == 0:
        child = (current[1][0] + 1,current[1][1])
        possible_children.append(child)
    if (current[1][0] - 1 >= 0) and (grid[current[1][0] - 1][current[1][1]]) == 0:
        child = (current[1][0] - 1,current[1][1])
        possible_children.append(child)
    if (current[1][1] + 1 < len(grid[0])) and (grid[current[1][0]][current[1][1]+1]) == 0:
        child = (current[1][0],current[1][1]+1)
        possible_children.append(child)
    if (current[1][1] - 1 >= 0) and (grid[current[1][0]][current[1][1] - 1]) == 0:
        child = (current[1][0],current[1][1]-1)
        possible_children.append(child)
    #print possible_children
    return possible_children

def rl_children(closed,available1,possible_children):
    real_children = []
    for i in range(len(possible_children)):
        if closed[possible_children[i][0]][possible_children[i][1]] == 0:
            if available1[possible_children[i][0]][possible_children[i][1]] == 0:
                real_children.append(possible_children[i])
    #print real_children
    return real_children

def m_heuristic(real_child,goal,count):
    x = real_child[0]
    y = real_child[1]
    h = abs(goal[0]-x) + abs(goal[1]-y)
    real_child = (h,real_child)
    return (real_child)

def print_current(current):
	grid1 = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			grid1[i][j] = grid[i][j]
	grid1[current[1][0]][current[1][1]] = 5

	for row in range(len(grid)):
		for column in range(len(grid[0])):
			color = WHITE
			if grid1[row][column] == 1:
				color = GRAY
			if grid1[row][column] == 5:
				color = GREEN
			pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
			pygame.time.delay(5)
	pygame.display.flip()

	p = PrettyTable()
	for row in grid1:
		p.add_row(row)
	#print p.get_string(header=False)
	print(grid1)

	
	

##############################################
###############   MAIN LOOP   ################
if __name__ == "__main__":
	
    # Define colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    GRAY = (115, 113, 113)

    WIDTH = 20
    HEIGHT = 20

    # This sets the margin between each cell
    MARGIN = 5
     
    # Create a 2 dimensional array. list of lists.
    grid = []
    grid1 = []
    grid = [[0, 1, 0, 0, 0, 0],
	    [0, 1, 0, 0, 1, 0],
	    [0, 1, 0, 1, 1, 0],
	    [0, 1, 0, 0, 1, 0],
	    [0, 0, 0, 0, 1, 0]]

    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    
    available = []
    available1 =[[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    init = [0, 0]
    goal = [len(grid)-1, len(grid[0])-1]
    count = 0
    current = [count,init]
    print "The robot's position is"
    print_current(current)
    while current[1][0] != goal[0] or current[1][1] != goal[1]:
        closed[current[1][0]][current[1][1]]=1
        count += 1
        #print "The robot can sense"
        #sense(grid,current)
        possible_children = psbl_children(current,grid)
        real_children = rl_children(closed,available1,possible_children)
        for i in range(len(real_children)):
            real_children[i] = m_heuristic(real_children[i],goal,count)
        for i in range(len(real_children)):
            available1[possible_children[i][0]][possible_children[i][1]] = 2
            available.append(real_children[i])
        available.sort()
        available.reverse()
        current = available.pop()
        print "The robot's position is"
        print_current(current)
    print("SOLVED")

########### PYGAME INTERFACE ###################
   
    while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True  # exit
			elif event.type == pygame.MOUSEBUTTONDOWN:
				# User clicks the mouse. Get the position
				pos = pygame.mouse.get_pos()
				# Change the x/y screen coordinates to grid coordinates
				column = pos[0] // (WIDTH + MARGIN)
				row = pos[1] // (HEIGHT + MARGIN)
				# Set that location to one
				grid[row][column] = 1
				print("Click ", pos, "Grid coordinates: ", row, column)
		# Set the screen background
		screen.fill(BLACK)
			 
		# Draw the grid

		for row in range(len(grid1)):
			for column in range(len(grid1[0])):
				color = WHITE
				if grid1[row][column] == 1:
					color = GRAY
				if grid1[row][column] == 5:
					color = GREEN
				pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
		print_current(current)
		# FPS
		clock.tick(60)
		# update screen
		pygame.display.flip()
pygame.quit()
