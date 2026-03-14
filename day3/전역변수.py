message = '나는야 전역 변수'

print(message) # 전역 변수 출력

def no_secret():
    global message
    message = '나는 진짜전역변수임'
    print(message) #'나는야 전역 변수' 출력
    print(message) #'나는 지역변수임' 출력
no_secret()
print(message) #'나는야 전역 변수' 출력