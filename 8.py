import re
f=open('input/8.txt').read().split('\n')[:-1]
parta=sum(sum(map(len,re.findall(r'\\(x[a-f0-9]{2}|\\|")',r)))+2 for r in f)
partb=sum(r.count('\\')+r.count('"')+2 for r in f)
print('parta', parta)
print('partb', partb)
