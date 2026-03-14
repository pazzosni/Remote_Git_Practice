#구구단 x단 프로그램 만들기
# gugu함수 구현하기
def gugu(x): #x단 구구단 출력
    for i in range(1, 10):
        print(f"{x} x {i} = {x*i}")

x = 9
print(gugu(x))