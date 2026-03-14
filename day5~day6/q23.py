import re

'''
아래에 정규표현식을 직접 입력해보세요!
'''

text = "tomato"

p1 = r"(to)ma\1"

m1 = re.search(p1, text)

print("m1 : ", m1.group())