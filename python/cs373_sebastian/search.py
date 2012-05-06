# ----------
# User Instructions:
# 
# Define a function, search() that takes no input
# and returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1] # Make sure that the goal definition stays in the function.

delta = [[-1, 0 ], # go up
        [ 0, -1], # go left
        [ 1, 0 ], # go down
        [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1




def expand(cell, closed):
    new_list = []
    y_max = len(grid)
    x_max = len(grid[0])
    
    for d in delta:
        new_x = cell[2] + d[1]
        new_y = cell[1] + d[0]
        if (new_x<0 or new_x>x_max-1 or new_y<0 or new_y>y_max-1):
            continue
        if ([new_y, new_x] in closed):
            continue
        if (grid[new_y][new_x] == 1):
            continue
        
        new_list.append([cell[0]+cost, new_y, new_x]) 
        closed.append([new_y, new_x])
            
    return new_list
 
def pick_min(open):
    min_g = min([row[0] for row in open])
    for e in open:
        if e[0] == min_g:
            return e
        
def search():
    closed = []
    open = [[0] + init]
    
    while open:
        # find cell c with lowest g
        cell = pick_min(open)

        if cell[1:] == goal:
            print 'reached goal at:', cell
            return cell
        else:
            closed.append(cell[1:])
            open.remove(cell)
            open += expand(cell, closed)
                    
    print 'fail'

search()
