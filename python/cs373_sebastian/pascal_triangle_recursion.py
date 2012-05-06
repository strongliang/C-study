def tri(n):
    if n == 1:
        return [[1]]
    else:
        res = tri(n-1)
        above = res[n-2]
        expand = [0] + above + [0]
        current = []
        for i in range(n):
            current += [expand[i] + expand[i+1]]
        res.append(current)
        return res
        
res = tri(5)

for i in range(len(res)):
    print res[i]
        