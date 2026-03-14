# while문을 사용해 1부터 1000까지 자연수 중 3의 배수의 합을 구하라.
result = 0

i = 1
while i <= 1000:
  if i % 3 == 0: #3의 배수로 걸러내는 코드
  	result += i
  i += 1
print(result)

# 더 좋은 코드로 작성 하는 법
for i in range(1, 1001):
    if i % 3 == 0:
        result += i

print(result)