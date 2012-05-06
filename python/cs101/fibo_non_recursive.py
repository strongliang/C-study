#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci(n):
    fib = [0 for i in range(n+1)]
#    fib = []
#    fib.append(0)
#    fib.append(1)
    fib[0] = 0
    fib[1] = 1
    for i in range(2, n+1):
#        fib.append(fib[i-1] + fib[i-2])
        fib[i] = fib[i-1] + fib[i-2]
    return fib[len(fib)-1]



print fibonacci(36)
#>>> 14930352

print fibonacci(6)