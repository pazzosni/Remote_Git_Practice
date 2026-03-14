import re

'''
아래에 정규표현식을 직접 입력해보세요!
'''

p1 = "short$"
p2 = "short$"

m1 = re.findall(p1, "Life is short")
m2 = re.findall(p2, "Life is short, art is long")

print("m1 : ", m1)
print("m2 :" , m2)