import math,itertools
t,s,r=itertools.takewhile,math.sqrt,range
i=34000000
a=lambda n:list(t(lambda x:10*sum(i+x//i for i in r(1,int(s(x))+1)if x%i==0)<n,r(n)))
b=lambda n:list(t(lambda x:11*sum(i*(x//i<=50)+x//i*(i<=50)for i in r(1,int(s(x))+1)if x%i==0)<n,r(n)))
print('parta',len(a(i)))
print('partb',len(b(i)))
