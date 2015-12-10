import re

a=lambda l,s:not l if s is None else s
b=lambda l,s:max(l+(2 if s is None else [-1,1][s]),0)

def setrange(g,lights,start,end,state):
    for x in range(start[0],end[0]+1):
        for y in range(start[1],end[1]+1):
            lights[y][x]=g(lights[y][x],state)
    return lights

getcoords=lambda s:[[int(c) for c in p] for p in re.findall(r'(\d+),(\d+)',s)]
f=open('input/6.txt').read().split('\n')[:-1]

def do(g):
    lights=[[0 for x in range(1000)] for y in range(1000)]
    for l in f:
        s,e=getcoords(l)
        lights=setrange(g,lights,s,e,True if l.count('on') else False if l.count('off') else None)
    return lights

print('parta', sum(i.count(1) for i in do(a)))
print('partb', sum(sum(i) for i in do(b)))
