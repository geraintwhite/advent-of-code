from itertools import permutations
f=open('input/13.txt').read().split('\n')[:-1]
m={}
for l in f:
    s=l.split()
    a,b,h=s[0],s[-1][:-1],int(s[3])*[-1,1][s[2]=='gain']
    m.setdefault(a,{})[b]=h
g=lambda m:max([sum(m[i[x]][i[x-1]]+m[i[x]][i[(x+1)%len(i)]] for x in range(len(i))) for i in permutations(m)])
print('parta',g(m))
for x in list(m):
    m.setdefault(x,{})['me']=m.setdefault('me',{})[x]=0
print('partb',g(m))
