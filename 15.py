import re
from operator import mul
from functools import reduce
f=open('input/15.txt').read().split('\n')[:-1]
m=[list(map(int,re.findall(r'-?\d',l))) for l in f]
a,b=[],[]
for i in range(100):
    for j in range(100):
        for k in range(100):
            n=[i,j,k,100-i-j-k]
            z=reduce(mul,(max(sum(reduce(mul,y)for y in zip(x,n)),0)for x in list(zip(*m))[:-1]))
            a.append(z)
            if sum(reduce(mul,y)for y in list(zip(list(zip(*m))[-1],n)))==500:b.append(z)
print('parta', max(a))
print('partb', max(b))
