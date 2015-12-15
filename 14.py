f=open('input/14.txt').read().split('\n')[:-1]
i=int
def g(x):
    m={}
    for l in f:
        p=l.split()
        n,s,t,r=p[0],i(p[3]),i(p[6]),i(p[-2])
        m[n]=s*t*(x/(t+r))+s*min(t,x%(t+r))
    return m
def b(x):
    p={}
    for i in range(x):
        p={n:p.get(n,0)+[0,1][d==max(a.values())] for a in [g(i+1)] for n,d in a.items()}
    return p
print('parta',max(g(2503).values()))
print('partb',max(b(2503).values()))
