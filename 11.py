import re
a=re.findall
i='hepxcrrq'
o=ord
f=lambda i:not a(r'[iol]',i)and[z for z in (i[x:x+3]for x in range(len(i)-2))if o(z[2])-o(z[1])==o(z[1])-o(z[0])==1] and len(set(a(r'([a-z])\1',i)))>1
def n(i):
    i=list(i)
    for x in range(len(i)-1,-1,-1):
        i[x]=(chr(o(i[x])+1),'a')[i[x]=='z']
        if not i[x]=='a':break
    return ''.join(i)
while not f(i):i=n(i)
print('part a',i)
i=n(i)
while not f(i):i=n(i)
print('part b',i)
