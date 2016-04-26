import numpy
from prettytable import PrettyTable

def initttt():
    print "REACHING HERE?"
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    available = []
    available1 =[[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    count = 0
    possible_children = []
    real_children = []
    return possible_children, real_children, closed, available, available1

def m_heuristic(real_child,goal,count):
    x = real_child[0]
    y = real_child[1]
    h = abs(goal[0]-x) + abs(goal[1]-y)
    real_child = (h,real_child)
    return (real_child)

def print_current(current):
    print "The robot's position is"
    grid1 = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid1[i][j] = grid[i][j]
    grid1[current[1][0]][current[1][1]] = 5

    p = PrettyTable()
    for row in grid1:
        p.add_row(row)
    print p.get_string(header=False)

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

actual_grid =  [[0, 0, 1, 0, 1, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 1, 0]]

grid = [[0 for row in range(len(actual_grid[0]))] for col in range(len(actual_grid))]
closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
available = []
available1 =[[0 for row in range(len(grid[0]))] for col in range(len(grid))]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
count = 0
possible_children = []
real_children = []
current = [count,init]
print_current(current)

while current[1][0] != goal[0] or current[1][1] != goal[1]:
    print "checkit!!", possible_children
    closed[current[1][0]][current[1][1]]=1
    count += 1
    possible_children = psbl_children(current,grid)
    real_children = rl_children(closed,available1,possible_children)
    for i in range(len(real_children)):
        real_children[i] = m_heuristic(real_children[i],goal,count)
    for i in range(len(real_children)):
        available1[possible_children[i][0]][possible_children[i][1]] = 2
        available.append(real_children[i])
    available.sort()
    available.reverse()
    next_step = available.pop()
    print "The next step", next_step
    if actual_grid[next_step[1][0]][next_step[1][1]] == 1:
        print "Need to recalculate path"
        grid[next_step[1][0]][next_step[1][1]] = 1
        possible_children, real_children, closed, available, available1 = initttt()
        print "This has to be reset",  possible_children, real_children, closed, available1
    else:
        current = next_step
        print_current(current)
print("SOLVED")
