# 객체변수 value가 100이상의 값은 가질 수 없도록 제한하는 MaxLimitCalculator 클래스를 만들어보자
class Calculator:
    def __init__(self):
        self.value = 0  #초기를 0으로 세팅함

    def add(self, val):
        self.value += val

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val  #먼저 계산할 방법을 정해주고
        if self.value >= 100:  # 그 다음 조건을 붙여 100이 안넘게끔 제한을 걸어둠
            self.value = 100

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)