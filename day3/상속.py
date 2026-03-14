class BlackBox: #기본 블랙박스 -부모 클래스
    def __init__(self, name, price):
        self.name = name
        self.price = price

class TravelBlackBox(BlackBox): #여행 모드 지원 블랙박스 -자식 클래스
    def set_travel_mode(self, min):
        print(str(min) + "분 동안 여행 모드 ON")

b1 = BlackBox('까망이', 200000)
b2 = TravelBlackBox('하양이', 100000)

b2.set_travel_mode(10)