# 3과 5의 배수를 모두 더하기
# 10 미만의 자연수에서 3과 5의 배수를 구하면 3, 5, 6, 9이다. 이들의 총합은 23이다. 
# 1,000 미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하라.
'''총합을 구해야하니 sum을 활용. 두 수의 배수를 구해야 하니 math.lcm을 사용해야함'''
'''
import math
num = math.lcm(3, 5)  #3, 5의 배수지정
total = sum(i for i in range(num, 1000, num)) # 최소공배수부터 1000까지 lcm간격으로 반복
print(total) #오답
'''
#정답
result = 0

for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        result += i

print(result)