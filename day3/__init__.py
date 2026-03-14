'''class BlackBox:
    pass

b1 = BlackBox()
b1.name = '까망이'

b2 = BlackBox()
'''
#print(b2.name) #에러가 뜸

class BlackBox:
    def __init__(self, name, price):
        self.name = name #멤버변수
        self.price = price


b1 = BlackBox('까망이', 200000) # 객체 생성, 객체명b1 b1=self
b2 = BlackBox('하양이', 100000)

print(b1.name, b2.name)