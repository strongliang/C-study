def tricky_loop(p):
    while True:
        if len(p) == 0:
            break
        else:
            if p[-1] == 0:
                p.pop() # assume pop is a constant time operation
            else:
                p[-1] = 0
    return 101
    
import time

def time_exec(code):
    start = time.clock()
    result = eval(code)
    run_time = time.clock() - start
    return result, run_time

import random    
p = []
for i in range(10**6):
    p.append(random.random() * 10)    
#print time_exec('tricky_loop(range(10**5))')
#print time_exec('tricky_loop(range(10**6))')
#print time_exec('tricky_loop(range(10**7))')

print time_exec('tricky_loop(p)')