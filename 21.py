import math as m,itertools as t
b=[109,8,2]
w=[[8,4,0],[10,5,0],[25,6,0],[40,7,0],[74,8,0]]
a=[[13,0,1],[31,0,2],[53,0,3],[75,0,4],[102,0,5],[0,0,0]]
r=[[25,1,0],[50,2,0],[100,3,0],[20,0,1],[40,0,2],[80,0,3],[0,0,0],[0,0,0]]
f=lambda p,b:m.ceil(b[0]/max(p[1]-b[2],1))<=m.ceil(p[0]/max(b[1]-p[2],1))
g=lambda:(
    sum(i[0])
    for x
        in t.product(w,a,*zip(*t.combinations(r,2)))
    for i 
        in [list(zip(*x))]
    if f([100,sum(i[1]),sum(i[2])],b)
)
print('parta',min(g()))
