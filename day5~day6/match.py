#match : 문자열의 처음부터 정규식과 매치되는지 조사한다. 
#즉, 패턴이 문자열의 시작 위치(인덱스 0)에서 바로 매치되어야 한다.

# 다음과 같은 패턴이 있다고 할때,
import re
p = re.compile('[a-z]+')


m = p.match('python')
print(m)
if m:
    print('Match found: ', m.group())
else:
    print('No match')