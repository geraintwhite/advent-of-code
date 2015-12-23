import re,itertools,functools
r=functools.reduce
m='CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF'
f=[l.split(' => ')for l in open('input/19.txt').read().split('\n')[:-1]]
a=lambda t:set(t[:x.start()]+z+t[x.end():]for y,z in f for x in re.finditer(y,t))
b=lambda t:r(lambda p,_:p if p[-1]=='e'else p[:-1]+r(lambda l,v:l+[l[-1].replace(v[1],v[0],1)] if v[1] in l[-1] else l,f,[p[-1]]),range(len(re.findall(r'[A-Z][a-z]?',m))),[t])
print('parta',len(a(m)))
print('partb',len(b(m))-1)
