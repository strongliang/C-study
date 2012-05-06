def fac(n):
    if n == 1 or n == 0:
        return 1
    else:
        res = fac(n-1)
        print res
        return res * (n)
        
        
print fac(5)
        