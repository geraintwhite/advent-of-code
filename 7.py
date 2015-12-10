from operator import *
from functools import reduce
def do(i):
    w={}
    o={'NOT':invert,'AND':and_,'OR':or_,'LSHIFT':lshift,'RSHIFT':rshift}
    f=sorted(i.split('\n')[:-1])[::-1]
    g=lambda v:w[v] if v.isalpha() else int(v)
    while f:
        l=f.pop()
        a,b=l.split(' -> ')
        p,c=reduce(lambda x,y:x[y not in o].append(y) or x,a.split(),([],[]))
        try:w[b]=o[p[0]](*map(g,c)) if len(p) else g(c[0])
        except KeyError:f.insert(0,l)
    return w
inpa=open('input/7.txt').read()
parta=do(inpa)
inpb=inpa.replace('14146 -> b', str(parta['a']) + ' -> b')
print('parta', parta['a'])
print('partb', do(inpb)['a'])
