import re

def a(s):
    if len(re.findall(r'[aeiou]', s)) < 3:
        return False
    if len(re.findall(r'([a-z])\1', s)) < 1:
        return False
    if len(re.findall(r'ab|cd|pq|xy', s)):
        return False
    return True

def b(s):
    if len(re.findall(r'([a-z]{2}).*\1', s)) < 1:
        return False
    if len(re.findall(r'([a-z])[a-z]\1', s)) < 1:
        return False
    return True

f = open('input/5.txt').read().split('\n')[:-1]

print('parta', len(list(filter(a, f))))
print('partb', len(list(filter(b, f))))
