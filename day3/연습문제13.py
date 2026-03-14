#random 모듈을 이용해서 로또번호(1~45사이의 숫자 6개)를 생성해보자. (중복 숫자 안 됨)
import random

num = random.sample(range(1, 46), 6) #숫자 범위 지정, 중에서 6개만 출력
print(num)  #sample자체에도 중복을 차단하는 기능이 있음
res = sorted(num) #중복차단
print(res)