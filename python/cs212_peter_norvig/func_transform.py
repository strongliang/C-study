# ---------------
# User Instructions
#
# Write a function, n_ary(f), that takes a binary function (a function
# that takes 2 inputs) as input and returns an n_ary function. 

def n_ary(f):
    """Given binary function f(x, y), return an n_ary function such
    that f(x, y, z) = f(x, f(y,z)), etc. Also allow f(x) = x."""
    def n_ary_f(x, *args):
        # my code here
#        if not args: return lambda x: x   #wrong, we don't want to return a new function here
        if not args: return x
#        if len(args)==0: return f(x)
#        elif len(args)==1: return f
        else: return f(x, n_ary_f(args[0], *(args[1:])))
        
#        # Peter's
#        return x if not args else f(x, n_ary_f(*args))
    return n_ary_f
    
    
def foo(a, b):
    return a, b
    
foo2 = n_ary(foo)
print foo2(1, 2, 3, 4, 5)
    

    
    
