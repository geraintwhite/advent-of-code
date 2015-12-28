import math as m,itertools as i
b=[109,8,2]
w=[[8,4,0],[10,5,0],[25,6,0],[40,7,0],[74,8,0]]
a=[[13,0,1],[31,0,2],[53,0,3],[75,0,4],[102,0,5],[0,0,0]]
r=[[25,1,0],[50,2,0],[100,3,0],[20,0,1],[40,0,2],[80,0,3],[0,0,0],[0,0,0]]
g=lambda a,b:m.ceil(b[0]/max(a[1]-b[2],1))<=m.ceil(a[0]/max(b[1]-a[2],1))
f=lambda c:[
    sum(s[0])
    for t
        in i.product(w,a,r,r)
    for s
        in [list(zip(*t))]
    if c(g([100,sum(s[1]),sum(s[2])],b)) and not t[-2]==t[-1]
]
print('parta',min(f(lambda x:x)))
print('partb',max(f(lambda x:not x)))
