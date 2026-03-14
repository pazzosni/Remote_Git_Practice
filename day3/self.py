class BlackBox:
    def __init__(self, name, champion,  price):
        self.name = name
        self.champion = champion
        self.price = price
    
    def set_travel_mode(self, sec):
        print(f'{self.name}의 {self.champion} {sec}초 동안 궁사용 가능')

b1 = BlackBox("추현식","파이크", 200000)
b2 = BlackBox("하양이","가렌", 100000)
b1.set_travel_mode(40) #결과  추현식의 파이크 40초 동안 궁사용 가능
b2.set_travel_mode(10) #결과 : 하양이 10분동안 여행모드 on

#self를 안쓰면 b1껀지 b2껀지 알 수가 없기 때문에 self를 꼭 써줘야함