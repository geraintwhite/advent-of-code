import re
f=open('input/16.txt').read().split('\n')[:-1]
c={'children':lambda x:x==3,'cats':lambda x:x==7,'samoyeds':lambda x:x==2,'pomeranians':lambda x:x==3,'akitas':lambda x:x==0,'vizslas':lambda x:x==0,'goldfish':lambda x:x==5,'trees':lambda x:x==3,'cars':lambda x:x==2,'perfumes':lambda x:x==1}
p=lambda l:re.findall(r'([a-z]+): (\d+)',l)
z=[p(x) for x in f]
g=lambda:[int(re.findall(r'Sue (\d+):',x)[0]) for x in f if all(c[i](int(y)) for i,y in p(x))]
print('parta',g())
c['cats'],c['trees'],c['pomeranians'],c['goldfish']=lambda x:x>7,lambda x:x>3,lambda x:x<3,lambda x:x<5
print('partb',g())
