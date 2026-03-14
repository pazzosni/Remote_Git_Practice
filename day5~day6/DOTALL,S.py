import re
p = re.compile('a,b')
m = p.match('a\nb')
print(m)  #None이 출력됨. \n은 메타문자와 매치되지 않음

#매치되게 하려면,
p = re.compile('a.b', re.DOTALL)  # re.DOTALL을 사용함으로써 줄 바꿈 문자에 상관없이 검색
m = p.match('a\nb')
print(m)