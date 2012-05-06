#Reachability

#Single Gold Star

#Define a procedure, reachable(graph, node), that takes as input a graph and a
#starting node, and returns a list of all the nodes in the graph that can be
#reached by following zero or more edges starting from node.  The input graph is
#represented as a Dictionary where each node in the graph is a key in the
#Dictionary, and the value associated with a key is a list of the nodes that the
#key node is connected to.  The nodes in the returned list may appear in any
#order, but should not contain any duplicates.


#def reachable(graph, node):
#    reach = []
#    if node not in graph:
#        return [node]
#
#    open = [node]       
#    closed = []
#    change = True
#    while change == True:
#        change = False
#
#        for e in open:
#            if e in closed:
#                open.remove(e)
#                continue
#            else:
#                reach.append(e)
#                closed.append(e)
#                union(open, graph[e])
#                change = True
#    return reach    
#def union(a, b):
#    for e in b:
#        if e not in a:
#            a.append(e)

def reachable(graph, node):
    reach = []
    open = [node]
    while open:
        e = open.pop(0)
        if e not in graph:
            reach.append(e)
        elif e not in reach:
            reach.append(e)
            open += graph[e]
    return reach    
       

#For example,

graph = {'a': ['m', 'p'], 'b': ['a', 'c'], 'c': ['b', 'd'], 'd': ['a'], 'e': ['a']}
#
print reachable(graph, 'a')
##>>> ['a', 'c', 'd', 'b']
#
#print reachable(graph, 'd')
##>>> ['d', 'a', 'c', 'b']
#
#print reachable(graph, 'e')
##>>> ['e', 'a', 'c', 'd', 'b']

#graph = {'a': ['b'], 'b': ['h'], 'c': ['h'], 'd':[], 'e': ['j'], 'f': ['a','c','e'], 'g': ['a'], 'h': ['g'], 'i': ['h','e'], 'j': ['d']}
print reachable(graph, 'a')
print reachable(graph, 'b')
print reachable(graph, 'c')
print reachable(graph, 'd')
print reachable(graph, 'e')
print reachable(graph, 'f')
print reachable(graph, 'g')
print reachable(graph, 'h')
print reachable(graph, 'i')
print reachable(graph, 'j')

#>>> Output:
#>>> ['a', 'b', 'h', 'g']
#>>> ['b', 'h', 'g', 'a']
#>>> ['c', 'h', 'g', 'a', 'b']
#>>> ['d']
#>>> ['e', 'j', 'd']
#>>> ['f', 'a', 'c', 'e', 'b', 'h', 'j', 'g', 'd']
#>>> ['g', 'a', 'b', 'h']
#>>> ['h', 'g', 'a', 'b']
#>>> ['i', 'h', 'e', 'g', 'j', 'a', 'd', 'b']
#>>> ['j', 'd']


