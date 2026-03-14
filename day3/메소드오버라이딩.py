class AdvancedTravelBlackBox(TravelBlackBox):
    def set_travel_mode(self, min):
        print(str(min) + "분 동안 여행 모드 ON")
        self.make() # 추억용 여행 영상 제작
        self.send() # 메일 발송
        