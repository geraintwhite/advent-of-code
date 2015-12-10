from functools import reduce
from itertools import groupby
i='3113322113'
f=lambda i:''.join(str(len(list(g)))+k for k,g in groupby(i))
print('parta', len(reduce(lambda x,_:f(x),range(40),i)))
print('partb', len(reduce(lambda x,_:f(x),range(50),i)))
