class BlackBox: #기본 블랙박스 -부모 클래스
    def __init__(self, name, price, ad):
        self.name = name
        self.price = price

class VideoMaker: #비디오 만드는 클래스 -부모 클래스
    def make(self):
        print("추억용 여행 영상 제작")

class MailSender: #메일 보내는 클래스 -부모 클래스
    def send(self):
        print('메일 발송')

class TravelBlackBox(BlackBox, VideoMaker, MailSender):
    def __init__(self, name, price, sd): # 자식 클래스에서도 init을 호출해줘야 함
        super().__init__(name, price)
        self.sd = sd

    def set_travel_mode(self, min):
        print(str(min) + "분 동안 여행 모드 ON")
        self.make()
        self.send()
              
b2 = TravelBlackBox("하양이", 100000, 64)
b2.make()
b2.send()