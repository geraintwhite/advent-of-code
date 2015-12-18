from itertools import *
f=list(map(int,open('input/17.txt').read().split('\n')[:-1]))
g=[x for x in (sum(1 for c in combinations(f,i) if sum(c)==150) for i in range(len(f))) if x]
print('parta',sum(g))
print('partb',g[0])
