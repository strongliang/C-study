#Double Gold Star

#Khayyam Triangle

#The French mathematician, Blaise Pascal, who built a mechanical computer in the
#17th century, studied a pattern of numbers now commonly known in parts of the
#world as Pascal's Triangle (it was also previously studied by many Indian,
#Chinese, and Persian mathematicians, and is known by different names in other
#parts of the world).

#The pattern is shown below:

#                    1
#                   1 1
#                  1 2 1
#                 1 3 3 1
#                1 4 6 4 1
#                   ...

 #0 1 2 3 
 #1 3 3 1

#1 4 6 4 1
#0 1 2 3 4

#Each number is the sum of the number above it to the left and the number above
#it to the right (any missing numbers are counted as 0).

#Define a procedure, triangle(n), that takes a number n as its input, and
#returns a list of the first n rows in the triangle. Each element of the
#returned list should be a list of the numbers at the corresponding row in the
#triangle.

def triangle(n):
    res = []
    if n >= 1:
        res.append([1])
    for i in range(2, n+1): # index is 1 based, +1 max range to accomodate
        above = res[i-2] # index is 1 based, -1 to accommodate
        expand = [0] + above + [0]
        current = []
        for i in range(len(expand)-1):
            current += [expand[i] + expand[i+1]]
        res.append(current)   
    return res 
        




#For example:

#print triangle(0)
#>>> []

#print triangle(1)
#>>> [[1]]

#print triangle(2)
#>> [[1], [1, 1]]

#print triangle(3)
#>>> [[1], [1, 1], [1, 2, 1]]

#print triangle(6)
#>>> [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]

res = triangle(7)
for i in range(len(res)):
    print res[i]