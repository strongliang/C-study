#THREE GOLD STARS

#Sudoku [http://en.wikipedia.org/wiki/Sudoku]
#is a logic puzzle where a game
#is defined by a partially filled
#9 x 9 square of digits where each square
#contains one of the digits 1,2,3,4,5,6,7,8,9.
#For this question we will generalize
#and simplify the game.


#Define a procedure, check_sudoku,
#that takes as input a square list
#of lists representing an n x n
#sudoku puzzle solution and returns
#True if the input is a valid
#sudoku square and returns False
#otherwise.

#A valid sudoku square satisfies these
#two properties:

#   1. Each column of the square contains
#       each of the numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the numbers from 1 to n exactly once.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]
            
#check if a line (row or col) is correct
def check_line(line):
    print line
    for i in range(len(line)):
        if i+1 not in line:
            return False
    return True
        
def check_sudoku(solution):
    dim = len(solution) #square, so only use 1d to store
    for i in range(dim):
        if not check_line(solution[i]):
            return False
        if not check_line([col[i] for col in solution]):
            return False
    return True
    
print check_sudoku(correct)
print check_sudoku(incorrect)    
    
