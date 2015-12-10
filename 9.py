from itertools import permutations
f=open('input/9.txt').read().split('\n')[:-1]
m={}
for l in f:
    p,d=l.split(' = ')
    a,b=p.split(' to ')
    m.setdefault(a,{})[b]=int(d)
    m.setdefault(b,{})[a]=int(d)
t=[sum(m[i[x-1]][i[x]] for x in range(1,len(i))) for i in permutations(m)]
print('parta', min(t))
print('partb', max(t))
