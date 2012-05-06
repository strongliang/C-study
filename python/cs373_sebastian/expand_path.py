# ----------
# User Instructions:
#
# Modify the the search function so that it returns
# a shortest path as follows:
# 
# [['>', 'v', ' ', ' ', ' ', ' '],
#  [' ', '>', '>', '>', '>', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', '*']]
#
# Where '>', '<', '^', and 'v' refer to right, left, 
# up, and down motions. NOTE: the 'v' should be 
# lowercase.
#
# Your function should be able to do this for any
# provided grid, not just the sample grid below.
# ----------


# Sample Test case
grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

# ----------------------------------------
# modify code below
# ----------------------------------------

#def print_path(goal, list, expand):
#    if not list:
#        return
#    else:
#        for e in list:
#            if e[:2] == goal:
#        expand[goal[0]][goal[1]] = 
    
def search():
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1
    
    expand = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    expand[goal[0]][goal[1]] = '*'
    seq = 0

    x = init[0]
    y = init[1]
    g = 0


#    open = [[g, x, y, hist]]
    open = [[g, x, y]]

    found = False  # flag that is set when search is complet
    resign = False # flag set if we can't find expand

    while not found and not resign:
        if len(open) == 0:
            resign = True
            return 'fail'
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]
            g = next[0]
#            h = next[3]
#            print [g, x, y, h]
            
            if x == goal[0] and y == goal[1]:
                found = True
#                print_path(goal, hist, expand)
#                print [seq, x, y, h]
#                for e in h:
#                    if e:
#                        expand[e[0]][e[1]] = e[2]
                
            else:
#                h.append([])
                
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
#                            h[len(h)-1] = [x, y, delta_name[i]]
#                            open.append([g2, x2, y2, h])
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1
    for i in range(len(expand)):
        print expand[i]
    return # make sure you return the shortest path.


search()
