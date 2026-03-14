class Myclass():
    def __init__(self):
        self.__variable = 10
        self.abc = 20

    def func(self):
        print('>>>', self.__variable)

obj = Myclass()
obj.func()
print(obj.abc)
print(obj.__variable) 
'''하위 클래스 충돌을 피하기 위해 이름을 다시 쓰도록 알리고 
맹글링(Magling) 기능을 사용해서 변수 이름 변경
내부에서만 접근 가능
외부에서는 '_클래스_이름'을 통해서 사용 가능(메소드 오버라이딩 방지)'''