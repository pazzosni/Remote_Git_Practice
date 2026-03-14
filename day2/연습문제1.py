#홍길동의 평균 점수 구하기
# 국어 -80, 영어 -75, 수학-55
국어 = 80
영어 = 75
수학 = 55
평균 = (국어 + 영어 + 수학) / 3
print(평균)

#자연수 13 이 홀수인지 짝수인지 판별하기
a = 13
b = a/2
print(b)
print(a, '를 2로 나눈 값은 소수이므로 ', a , '는 홀수 입니다')

#홍길동의 주민등록번호는 881120-1068234이다. 홍길동의 주민등록번호를 연원일(YYYYMMDD)부분과 그 뒤의 숫자 부분으로 나누어 출력해보자.
홍길동 = (881120-1060234)
yyyymmddd = 881120
other = 1060234
print(yyyymmddd)
print(other)
#num = id[7]
#주민등록번호 뒷자리(Q3의 주민등록번호 사용)의 맨 첫 번째 숫자는 성별을 나타낸다. 성별을 나타내는 숫자를 출력해보자.
#print(other[0])

#다음과 같은 문자열 a:b:c:d:가 있다. 문자열의 replace함수를 이용하여 a#b#c#d로 바꿔보자.
s = 'a:b:c:d:'
new_s = s.replace(':', '#')
print(new_s)

#[1, 3, 5, 4, 2] 리스트를 [5, 4, 3, 2, 1]로 만들어 보자.(Hint : sort() 함수와 reverse() 함수)
c = [1, 3, 5, 4, 2]
c.sort()
print(c)
c.reverse()
print(c)

#[‘Life’, ‘is’, ‘too’, ‘short’] 리스트를 Life is too short 문자열로 만들어 출력해 보자.(Hint : join()함수)
d = ['Life', 'is', 'too', 'short']
print(type(d))
print(' '.join(d)) #리스트 => 문자열

#(1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)를 만들어 출력해 보자.
e = (1, 2, 3)
f = (4,) #1개 요소
print(e + f)
#정석적인 방법 : 형변환
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
my_list.append(4)
my_tuple = tuple(my_list)
print(my_tuple)