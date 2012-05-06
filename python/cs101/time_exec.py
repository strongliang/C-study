import time

def time_exec(code):
    start = time.clock()
    result = eval(code)
    run_time = time.clock() - start
    return result, run_time
    
def spin_loop1(times):
    sum = 0
    for i in range(times):
        sum += i
    return sum
        
def spin_loop2(times):
    i = 0
    while i < times:
        i += 1
        
# though it seems to me that a for loop has some extra overhead for managing the list
# the exec time is actually similar to that of a while loop
print time_exec('spin_loop1(1000)')
print time_exec('spin_loop2(1000)')