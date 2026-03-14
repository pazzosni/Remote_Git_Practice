import re

p1 = "apple"
p2 = "banana"

m1 = re.findall(p1, "I like apple and banana")
m2 = re.findall(p2, "I like apple and banana")

print("m1 : ", m1)
print("m2 : ", m2)


### 아래 p3에 직접 정규표현식을 입력해보세요!

p3 ="apple|banana"     #apple 또는 banana가 포함되면 매치

m3 = re.findall(p3, "I like apple and banana")

print("m3 : ", m3)