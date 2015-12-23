import math
i=34000000
#i=100000
def a(n,x=1):
    while 10*sum(i+x//i for i in range(1,int(math.sqrt(x))+1) if x%i==0)<n:
        x+=1
    return x
def b(n,x=1):
    while 11*sum((i if x//i<=50 else 0)+(x//i if i<=50 else 0) for i in range(1,int(math.sqrt(x))+1) if x%i==0)<n:
        x+=1
    return x
print('parta',a(i))
print('partb',b(i))
