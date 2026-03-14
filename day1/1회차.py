print(1)
print(3.14)
print('hello world')
print("안녕하세요")
print('1004') # 문자, 숫자가 아님
# 분리안 자료형
print(True)
print(False)


env1 = 10000
env2 = 20000
env3 = '파이팅'
env4 = 'Lamborghini Aventador'
env5 = "logitech G Hub"
env6 = 5
env7 = 4
env8 = env6 + env7

print(env8)
print(env1)
print(env2)
print(env3)
print(env4)

print(2<5 and 3<9 and 12<30)

# bool 함수
# print(3>5)  -> False
# print(bool(None)) -> False
# print(bool('Flase')) -> True

'''여러줄 주석
테스트입니다
테스트실행중입니다'''

#index 개념
lang = 'PYTHON'
print(lang[-2])

#슬라이싱 개념
print(lang[:]) 
# 인덱싱 0번부터 4번까지(5는 5미만이라는 뜻) 
# 공백으로 남길시 끝까지 라는 뜻
# 처음을 공백으로 남기면 처음부터 라는 뜻

a = '7'
b = '제곱'
print(b + a) # 변수 두 개가 둘다 문자이기에 가능한 출력

c = a + b #c라는 변수 생성
print(c + '입니다')

b += '입니다' # b에다가 입니다를 추가함(더해서 누적하라는 뜻) ->좋은 코드임
print(b)

num = 5
num += 2 # 7
num -= 3 # 4
num *= 2 # 8
num /= 4 # 2.0
print(num)

s = '안녕하세요'
print(len(s)) # len = 값의 길이를 나타내는 함수

# 여러 줄 변수 사용하기
a = '''
안녕하세요.
반갑습니다.
hi
bye
'''
print(a)
print(len(a))

letter = ' how are you?'
print(letter.capitalize())
print(letter.upper())
print(letter.split())
print(letter.count('how are'))

s = '..이스트 소 프 트...'
print(s.startswith('이')) # 이로 시작을 하는가 = True
print(s.startswith('나')) # 나로 시작을 하는가 = False
print(s.endswith('소프트')) # 소프트로 끝나는가 = True 
print(s.strip('.')) # . 만 지우기
print(s.strip(' ')) #앞뒤 공백만 제거
print(s.lstrip('.')) # 왼쪽기준
print(s.rstrip('.')) # 오른쪽기준
print(s.replace('이스트', '웨스트')) #좌측거를 우측걸로 바꿔줘

# 글자위치를 찾는 함수 s.find
print(s.find('이'))
# 다른 문자들 사이에 가운데로 = s.center

# 띄어쓰기 하는 방법
java = '자바'
python = '파이썬'

print(java, python) #,를 붙이면 '한 칸'이 무조건 띄워짐

#다른 문장에 삽입하기
print("개발 언어에는" + " " + python + "," + java + "등이 있어요") # 문법상 오류는 없으나 지저분함
print('개발 언어에는 {}, {} 등이 있어요' .format(python, java)) # .format 기법 = 위의 코드보다 수정도 쉽고 훨씬 깔끔함
print(f'개발언어에는 {python}과 {java}가 있어요') # f-string 기법 = 가장 심플하고 직관적임

#탈출문자
# 친구가 "파이썬 배우기 쉬워?" 하고 물었다.
print('친구가 "파이썬 배우기 쉬워?" 라고 물었다.')

# 나는 속으로 '엄청 어려운데...' 라고 생각했다
print("나는 속으로 '엄청 어려운데...' 라고 생각했다.") # ''를 붙일 시 에러가 발생함
# 이런 현상 때문에 탈출문자를 써야함 \(역슬래시) = 큰 따옴표는 \" , 작은 따옴표는 \'
print("나는 속으로 \'나만 당할순없지' 라는 생각에 \"엄청 쉽지\"라고 했다.")
#역슬래시를 출력하는 법
print("나는 속으로 \'나만 당할순없지' 라는 생각에 \"엄청 쉽지\"라고 했다.\\") #\\를 두개 작성하면 1개가 출력됨
print('C: \\Users\\nadocoding')#경로를 표현하고 싶을때
print(r'C:\Users\nadocoding')#raw string 문법이라고 하며 그대로 출력해달라는 의미
# 줄 바꾸는 법 \n
print("꿀꽈배기는\n너무\n맛있어요")
# '''로도 사용할 수 있음
print('''꿀 꽈배기는
너무
맛있어요''')