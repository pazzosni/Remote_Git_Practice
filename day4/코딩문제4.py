# 다음은 A학급 학생의 점수를 나타내는 리스트이다. 
# 다음 리스트에서 50점 이상 점수의 총합을 구하시오.
'''
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
total = sum(filter(lambda x: x>50, A))
print(total)
'''
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]

result = 0

total = 0
for x in A:
    if x > 50:
        total += x

print(total)