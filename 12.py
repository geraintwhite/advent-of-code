import json
i=isinstance
a=lambda o:sum(map(a,o))if i(o,list)else sum(map(a,o.values()))if i(o,dict)else o if i(o,int)else 0
b=lambda o:sum(map(b,o))if i(o,list)else sum(map(b,o.values()))if i(o,dict)and 'red' not in o.values() else o if i(o,int)else 0
with open('input/12.txt') as f:
    j=json.load(f)
    print('parta', a(j))
    print('partb', b(j))
