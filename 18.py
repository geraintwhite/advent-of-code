from functools import reduce
r=range
f=[[x=='#' for x in y] for y in open('input/18.txt').read().split('\n')[:-1]]
t=lambda l,i,d:l[i] if -1<i<len(l) else d
g=lambda b,o=():[[1 if n==3 or (x,y)in o else 0 if n<2 or n>3 else b[y][x]for x in r(len(b[y]))for n in[sum(t(t(b,y+j,[]),x+i,0)for i in r(-1,2)for j in r(-1,2)if not i==j==0)]]for y in r(len(b))]
print('parta',sum(map(sum,reduce(lambda x,_:g(x),r(100),f))))
f[0][0]=f[0][-1]=f[-1][0]=f[-1][-1]=1
print('partb',sum(map(sum,reduce(lambda x,_:g(x,((0,0),(0,99),(99,0),(99,99))),r(100),f))))
