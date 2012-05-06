from itertools import *


print [[int(str(O)+str(D)+str(D)), int(str(E)+str(V)+str(E)+str(N))] for O,D,E,V,N in permutations(range(10), 5) if int(str(O)+str(D)+str(D))*2==int(str(E)+str(V)+str(E)+str(N))]