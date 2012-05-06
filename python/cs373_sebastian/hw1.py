colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']
      

motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7
p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT

#init
row = len(colors)
col = len(colors[0])

p = [[1./(row*col) for c in range(col)] for r in range(row)]
show(p)



def sense(p, Z):
    q = [[0 for c in range(col)] for r in range(row)]
    for i in range(row):
        for j in range(col):
            hit = (Z == colors[i][j])
            q[i][j] = p[i][j] * (hit * sensor_right + (1-hit) * (1-sensor_right))
    
    s = sum(sum(w) for w in q)
    for i in range(row):
        for j in range(col):
            q[i][j] = q[i][j] / s
    return q


def move(p, U):
    q = [[0 for c in range(col)] for r in range(row)]
    for i in range(row):
        for j in range(col):
            s = p_move * p[(i-U[0])%row][(j-U[1])%col]
            s += (1-p_move) * p[i][j]
            q[i][j] = s
    return q

for i in range(len(measurements)):
#    print motions[i], measurements[i]
#    print 'before: '
#    show(p)
    p = move(p, motions[i])
    p = sense(p, measurements[i])
#    print 'after: '
#    show(p)


#Your probability array must be printed 
#with the following code.

show(p)


# -*- coding: cp1252 -*-
#Displays the matrixs p and colors given in the Homework 1.4
#
#   How to use it :
#
#   Just replace the line:
#                   show(p)
#   by those ones:
#                   #show(p)
#                   import AfficheHistogram
#                   fenetre = AfficheHistogram.AfficheHistogramme ( p, colors )
#                   fenetre.mainloop()
#
#Have fun :)

