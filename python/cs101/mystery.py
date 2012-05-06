from math import *
import random

def mystery(p):
    i = 0
    count = 0
    while True:
        count += 1
        if i >= len(p):
            break
        if p[i] % 2:
            i = i + 2
        else:
            i = i + 1
    print count
    return i

p = [int(100.*random.random()) for e in range(10**7)]
mystery(p)
#print p

