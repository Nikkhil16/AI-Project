import numpy
from prettytable import PrettyTable

##############################################
###########   DEFINE FUNCTIONS   ############
def psbl_children(current,grid):
    possible_children = []
    i = current[1][0][0]
    j = current[1][0][1]
    # From Vertical
    if current[1][1] == 1:
        #Vertical Left
        if j-1 >= 0 and grid[i-1][j-1] == 0 and grid[i][j-1] == 0 and grid[i+1][j-1] == 0:
            possible_children.append([[i,j-1],1])
        #Vertical Right
        if j+1 < len(grid[0]) and grid[i+1][j+1] == 0 and grid[i][j+1] == 0 and grid[i-1][j+1] == 0:
            possible_children.append([[i,j+1],1])
        #Vertical Up
        if i-2 >= 0 and grid[i-2][j] == 0:
            possible_children.append([[i-1,j],1])
        #Vertical Down
        if i+2 < len(grid) and grid[i+2][j] == 0:
            possible_children.append([[i+1,j],1])
        #CW Horizontal and #CCW Horizontal
        if j-1 >= 0 and j+1 < len(grid[0]) and ((grid[i-1][j+1] == 0 and grid[i+1][j-1] == 0 and grid[i][j+1] == 0 and grid[i][j-1] == 0) or (grid[i-1][j-1] == 0 and grid[i+1][j+1] == 0 and grid[i][j-1] == 0 and grid[i][j+1] == 0)):
            possible_children.append([[i,j],0])
        
    # From Horizontal
    if current[1][1] == 0:
        #Horizontal Right
        if j+2 < len(grid[0]) and grid[i][j+2] == 0:
            possible_children.append([[i,j+1],0])
        #Horizontal Left
        if j-2 >= 0 and grid[i][j-2] == 0:
            possible_children.append([[i,j-1],0])
        #Horizontal Up
        if i-1 >= 0 and grid[i-1][j-1] == 0 and grid[i-1][j] == 0 and grid[i-1][j+1] == 0:
            possible_children.append([[i-1,j],0])
        #Horizontal Down
        if i+1 < len(grid) and grid[i+1][j-1] == 0 and grid[i+1][j] == 0 and grid[i+1][j+1] == 0:
            possible_children.append([[i+1,j],0])
        #CW Vertical and #CCW Vertical
        if i-1 >= 0 and i+1 < len(grid) and ((grid[i-1][j-1] == 0 and grid[i-1][j] == 0 and grid[i+1][j+1] == 0 and grid[i+1][j] == 0) or (grid[i+1][j-1] == 0 and grid[i+1][j] == 0 and grid[i-1][j] == 0 and grid[i-1][j+1] == 0)):
            possible_children.append([[i,j],1])
    #print possible_children
    return possible_children

def rl_children(closed0,closed1,available0,available1,possible_children):
    real_children = []
    for i in range(len(possible_children)):
        if possible_children[i][1] == 1:
            if closed1[possible_children[i][0][0]][possible_children[i][0][1]] == 0:
                if available1[possible_children[i][0][0]][possible_children[i][0][1]] == 0:
                    real_children.append(possible_children[i])
        if possible_children[i][1] == 0:
            if closed0[possible_children[i][0][0]][possible_children[i][0][1]] == 0:
                if available0[possible_children[i][0][0]][possible_children[i][0][1]] == 0:
                    real_children.append(possible_children[i])
    #print "real_children"
    #print real_children
    return real_children

def m_heuristic(real_children,goal):
    x = real_children[0][0]
    y = real_children[0][1]
    orientation = real_children[1]
    h = abs(goal[0][0]-x) + abs(goal[0][1]-y) + abs(goal[1]-orientation)
    real_child = (h,real_children)
    return (real_child)

def print_current(current):
    grid1 = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid1[i][j] = grid[i][j]
    if current[1][1] == 1:            
        grid1[current[1][0][0]-1][current[1][0][1]] = 5
        grid1[current[1][0][0]][current[1][0][1]] = 5
        grid1[current[1][0][0]+1][current[1][0][1]] = 5
    if current[1][1] == 0:            
        grid1[current[1][0][0]][current[1][0][1]-1] = 5
        grid1[current[1][0][0]][current[1][0][1]] = 5
        grid1[current[1][0][0]][current[1][0][1]+1] = 5
 
    p = PrettyTable()
    p.set_field_names(["A", "B", "C", "D",'E','F','G'])
    print grid1
    for row in grid1:
        p.add_row(row)
    print p.get_string(header=False)
##############################################
###############   MAIN LOOP   ################
if __name__ == "__main__":
    grid = [[0, 0, 1, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0]]
    #horizontal - closed list
    closed0 = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    #vertical - closed list
    closed1 = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    available = []
    available0 =[[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    available1 =[[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    #initial robot location and orientation
    init = [[1, 0],1]
    #goal state for the robot
    goal = [[len(grid)-2, len(grid[0])-1],1]
    count = 0
    #current robot location and orientation
    current = [count,init]
    print "The robot's position is"
    print_current(current)
    while current[1][0][0] != goal[0][0] or current[1][0][1] != goal[0][1] or current[1][1] != goal[1]:
        if current[1][1] == 1:
            closed1[current[1][0][0]][current[1][0][1]] = 1
        if current[1][1] == 0:
            closed0[current[1][0][0]][current[1][0][1]] = 1
        count += 1
        possible_children = psbl_children(current,grid)
        real_children = rl_children(closed0,closed1,available0,available1,possible_children)
        for i in range(len(real_children)):
            real_children[i] = m_heuristic(real_children[i],goal)
        for i in range(len(real_children)):
            if real_children[i][1][1] == 1:
                available1[real_children[i][1][0][0]][real_children[i][1][0][1]] = 2
            if real_children[i][1][1] == 0:
                available0[real_children[i][1][0][0]][real_children[i][1][0][1]] = 2
            available.append(real_children[i])
        #print available
        available.sort()
        available.reverse()
        current = available.pop()
        print "The robot's position is"
        print_current(current)
    print("SOLVED")

####################################################
