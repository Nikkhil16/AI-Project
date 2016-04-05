import numpy
from prettytable import PrettyTable

##############################################
###########   DEFINE FUNCTIONS   ############
'''
def sense(current,grid):
    zz = []
    zz.append(grid[current[1][0] + 1][current[1][1]])

    p = PrettyTable()
    for row in zz:
        p.add_row(row)
    print p.get_string(header=False)
'''
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

    p = PrettyTable()
    for row in grid1:
        p.add_row(row)
    print p.get_string(header=False)
##############################################
###############   MAIN LOOP   ################
if __name__ == "__main__":
    grid = [[0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
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

####################################################
