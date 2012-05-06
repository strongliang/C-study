
# method 1, using library
import itertools
res = []
a = list(itertools.permutations(list('abc')))
for e in a:
    s = ''.join(e)
    res.append(s)
print res

# method 2, using generator
def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                #nb str[0:1] works in both string and list contexts
                yield perm[:i] + str[0:1] + perm[i:]
                
a = list(all_perms('abc'))
print a
    
def perm(str):
    a = list(str)
    if len(str) == 1:
        print str
        return str
    else:
        for i in range(len(a)):
            print a[i],
            b = a[:]
            perm(''.join(b.pop(i)))

perm("ab")
    
            