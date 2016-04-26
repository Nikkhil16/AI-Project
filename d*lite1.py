import numpy as np
from prettytable import PrettyTable

def m_heuristic(ss):
    x = ss[0]
    y = ss[1]
    h = abs(start[0]-x) + abs(start[1]-y)
    return h

def calculate_key(s):
    return min(g[s[0]][s[1]],rhs[s[0]][s[1]])+m_heuristic(s)+k_old,min(g[s[0]][s[1]],rhs[s[0]][s[1]])

def initialize():
    rhs[goal[0]][goal[1]] = 0
    U.insert(0,[calculate_key(goal),goal])

def find_successors(u):
    successors = []
    x = u[1][0]
    y = u[1][1]
    if x-1 >= 0:
        successors.append([x-1,y])
    if x+1 < len(grid):
        successors.append([x+1,y])
    if y-1 >= 0:
        successors.append([x,y-1])
    if y+1 < len(grid[0]):
        successors.append([x,y+1])
    return successors

def find_predecessors(u):
    predecessors = []
    x = u[0]
    y = u[1]
    if x-1 >= 0:
        predecessors.append([x-1,y])
    if x+1 < len(grid):
        predecessors.append([x+1,y])
    if y-1 >= 0:
        predecessors.append([x,y-1])
    if y+1 < len(grid[0]):
        predecessors.append([x,y+1])
    return predecessors

def update_vertex(u):
    print "vertex to update",u
    if u != goal:
        predecessors = find_predecessors(u)
        values_to_update = []
        for i in range(len(predecessors)):
            values_to_update.append(g[predecessors[i][0]][predecessors[i][1]]+cost[predecessors[i][0]][predecessors[i][1]])
        rhs[u[0]][u[1]] = min(values_to_update)
    #############################################
    c = []
    for j in range(len(U)):
        if U[j][1] == u:
    		c.append(j)
    count = 0
    for k in range(len (c)):
    	U.pop(c[k]-count)
    	count += 1
    ############################################
    if g[u[0]][u[1]] != rhs[u[0]][u[1]]:
        U.insert(0,[calculate_key(u),u])
    print "After update vertex"
    print_G()
    print_RHS()

def compute_shortest_path():
    U.sort()
    while (U[0][0] < calculate_key(start) or rhs[start[0]][start[1]] != g[start[0]][start[1]]):
    #for something in range(2):
        k_old = U[0][0]
        u = U.pop()
        #print "CHECK",u,u[1],start
        if k_old < calculate_key((u[1])):
            U.insert(0,[calculate_key(u[1]),u[1]])
        elif g[u[1][0]][u[1][1]] > rhs[u[1][0]][u[1][1]]:
            #print "equating g to rhs"
            g[u[1][0]][u[1][1]] = rhs[u[1][0]][u[1][1]]
            successors = find_successors(u)
            for i in range(len(successors)):
                if cost[successors[i][0]][successors[i][1]] == 1:
                    update_vertex(successors[i])
        else:
            g[u[1][0]][u[1][1]] = float("inf")
            update_vertex(u[1])
            successors = find_successors(u)
            for i in range(len(successors)):
                if cost[successors[i][0]][successors[i][1]] == 1:
                    update_vertex(successors[i])
        U.sort()
        U.reverse()
        print "After compute shortest"
        print_G()
        print_RHS()

def print_G():
    print "G matrix is : "
    p = PrettyTable()
    for row in g:
        p.add_row(row)
    print p.get_string(header=False)

def print_RHS():
    print "RHS matrix is : "
    p = PrettyTable()
    for row in rhs:
        p.add_row(row)
    print p.get_string(header=False)

def print_current(current):
    print "ROBOT IS CURRENTLY AT: "
    grid1 = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid1[i][j] = grid[i][j]
    grid1[current[0]][current[1]] = 5

    p = PrettyTable()
    for row in grid1:
        p.add_row(row)
    print p.get_string(header=False)

U = []
grid = [[0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0]]


g = [[float("inf") for row in range(len(grid[0]))] for col in range(len(grid))]
rhs = [[float("inf") for row in range(len(grid[0]))] for col in range(len(grid))]
cost = [[1 for row in range(len(grid[0]))] for col in range(len(grid))]
goal = [3,0]
start = [1,5]
km = 0
k_old = 0
last = start
initialize()
compute_shortest_path()
while start != goal:
    predec_range = []
    if g[start[0]][start[1]] == float('inf'):
        print "There is no solution"
        break
    predec = find_predecessors(start)
    for i in range(len(predec)):
        predec_range.append(cost[predec[i][0]][predec[i][1]]+g[predec[i][0]][predec[i][1]])
    a = np.argmin(predec_range)
    next_step = predec[a]
    if grid[next_step[0]][next_step[1]] == 0:
        start = next_step
        current = start
    else:
        km = km + m_heuristic(last)
        last = start
        cost[next_step[0]][next_step[1]] = float("inf")
        neighbours = find_predecessors(next_step)
        for i in range(len(neighbours)):
            update_vertex(neighbours[i])
        compute_shortest_path()

    print_current(current)
