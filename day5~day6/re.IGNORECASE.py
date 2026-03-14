import re
p = re.compile('[a-z]+', re.I) #대소문자 구별없이 매치를 수행할 때
m = p.match('python')
m2 = p.match('Python')
m3 = p.match('PYTHON')
print(m)
print(m2)
print(m3)