class BlackBox:
    pass

b1 = BlackBox() # 객체 생성, 객체명 b1
b2 = BlackBox() # 각각 계정이라고 생각하면돔

b1.name = '까망이' #b1은 까망이 것
b2.name = '노랭이' #클래스 객체의 변수에 접근하기 위해서는 점(.)을 사용
#print(name)을 해도 name변수는 지정된게 없기 때문에 출력되지않음
print(b1.name)
print(b2.name)
print(isinstance(b1, BlackBox)) #True출력