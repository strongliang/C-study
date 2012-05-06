#Same Structure

#Define a procedure, same_structure, that takes two inputs. It should output
#True if the lists contain the same elements in the same structure, and False
#otherwise. Two values, p and q have the same structure if:

#    Neither p or q is a list.

#    Both p and q are lists, they have the same number of elements, and each
#    element of p has the same structure as the corresponding element of q.


#For this procedure, you can use the is_list(p) procedure from Homework 6:

def is_list(p):
    return isinstance(p, list)


def same_structure(a,b):
    if not is_list(a) and not is_list(b): # neither is list
        return True
    elif (is_list(a) and not is_list(b)) or \
         (is_list(b) and not is_list(a)): # one list, one not
        return False
    else:                                 # both are lists
        if len(a) != len(b):
            return False
        else:
            for i in range(len(a)):
                if not same_structure(a[i], b[i]):
                    return False
            return True
            
        



#Here are some examples:

print same_structure(3, 7) == True
#>>> True

print same_structure([1, 0, 1], [2, 1, 2]) == True
#>>> True

print same_structure([1, [0], 1], [2, 5, 3]) == False
#>>> False

print same_structure([1, [2, [3, [4, 5]]]], ['a', ['b', ['c', ['d', 'e']]]]) == True
#>>> True

print same_structure([1, [2, [3, [4, 5]]]], ['a', ['b', ['c', ['de']]]]) == False
#>>> False