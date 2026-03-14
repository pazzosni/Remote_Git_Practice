#첫 번째 항의 값이 0이고 두 번째 항의 값이 1일 때, 이후에 이어지는 항은 
# 이전의 두항을 더한 값으로 이루어지는 수열을 피보나치 수열이라고 한다.
'''
0, 1, 1, 2, 3, 5, 8, 13 …

입력을 정수 n으로 받았을 때, n이하까지의 피보나치 수열을 
출력하는 함수를 작성해 보자.
'''
'''n = input('정수를 입력하세요.')
n = int(n) #받은 값을 정수로 환
print(type(n))

A = [0, 1] #초기 값 설정
for i in range(2, n):
    A.append(A[i-1] + A[i-2]) #이전의 두항을 찾는법

print(A)'''

######################
fib_list = [0,1]
def rec_fibo(n, i=0):
    next_num = fib_list[i] + fib_list[i+1]
    if next_num <= int(n):
        rec_fibo(n, i+1)

num = input('정수르 입력하세요')
num = int(num)
rec_fibo(num)
print(fib_list)