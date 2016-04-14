def psbl_children(current,grid):
    possible_children = []
    i = current[1][0][0]
    j = current[1][0][1]
    if current[1][1] == 1:
        #Vertical Left
        if j-1 >= 0 and grid[i-1][j-1] == 0 and grid[i][j-1] == 0 and grid[i+1][j-1] == 0:
            possible_children.append([[i,j-1],1])
        #Vertical Right

        #Vertical Up
        #Vertical Down
        #CW Horizontal
        #CCW Horizontal
    if current[1][1] == 0:
        #Horizontal Right
        #Horizontal Left
        #Horizontal Up
        #Horizontal Down
        #CW Vertical
        #CCW Vertical
    #print possible_children

def rl_children(closed0,closed1,available0,available1,grid):
    real_children = []
    for i in range(len(possible_children)):
        if possible_children[i][1] == 1:
            if closed1[possible_children[i][0][0]][possible_children[i][0][1]] == 0:
                if available1[possible_children[i][0][0]][possible_children[i][0][1]] == 0:
                    real_children.append(possible_children[i])
        if possible_children[i][1] == 0:
            #check with closed0,available0

def m_heuristic(real_child,goal,count):
    x = real_child[0][0]
    y = real_child[0][1]
    orientation = real_child[1]
    h = abs(goal[0][0]-x) + abs(goal[0][1]-y) + abs(goal[1]-orientation)
    real_child = (h+count,real_child)
    return (real_child)

grid = [[0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0]]
closed0 = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
closed1 = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
available = []
available0 =[[0 for row in range(len(grid[0]))] for col in range(len(grid))]
available1 =[[0 for row in range(len(grid[0]))] for col in range(len(grid))]
init = [[1, 0],1]
goal = [[len(grid)-2, len(grid[0])-1],1]
count = 0
current = [count,init]
print "The robot's position is"
print current
#while current[1][0][0] != goal[0][1] or current[1][0][1] != goal[0][1] or current[1][1] != goal[1]:
if current[1][1] == 1:
    closed1[current[1][0][0]][current[1][0][1]] = 1
if current[1][1] == 0:
    closed0[current[1][0][0]][current[1][0][1]] = 1
count += 1
possible_children = psbl_children(current,grid)
real_children = rl_children(closed,available1,possible_children)
for i in range(len(real_children)):
    real_children[i] = m_heuristic(real_children[i],goal,count)
for i in range(len(real_children)):
    if real_children[i][1][1] == 1:
        available1[real_children[i][1][0][0]][real_children[i][1][0][1]] = 2
    if real_children[i][1][1] == 0:
        available0[real_children[i][1][0][0]][real_children[i][1][0][1]] = 2
    available.append(real_children[i])
available.sort()
available.reverse()
current = available.pop()
