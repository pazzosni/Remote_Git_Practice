#for 문 활용
person = {'이름': '김민석', '나이': 29, '키':175, '몸무게': 50}
for v in person.values():
    print(v)
for v in person.keys():
    print(v)
for k, v in person.items():
    print(k,v)
#문자열
fruit = 'apple'
for x in fruit:
    print(x)