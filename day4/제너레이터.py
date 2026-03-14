'''def mygen():
     yield 'a'
     yield 'b'
     yield 'c'
 
g = mygen()'''

#제네레이터 표현식
# generator.py
def mygen(): #mygen 함수는 1부터 1,000까지 각각의 숫자를 제곱한 값을 순서대로 반환하는 제너레이터
    for i in range(1, 1000):
        result = i * i
        yield result

gen = mygen()

print(next(gen))
print(next(gen))
print(next(gen))