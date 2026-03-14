class BlackBox:
    def __init__(self, name, price):
        self.name = name # 멤버 변수
        self.price = price

class TravelBlackBox(BlackBox):
    def __init__(self, name, price, sd):
        super().__init__(name, price) #self를 지정할 필요가 없음!! super():부모 클래스에서 만들어놨던 멤버 변수를 사용하겠다
        self.sd = sd
    
    def set_travel_mode(self, min):
        print(str(min) + "분 동안 여행 모드 ON")

b1 = BlackBox('까망이', 200000)
b2 = TravelBlackBox('하양이', 1000000, 64)
print(b2.name, b2.price, b2.sd)