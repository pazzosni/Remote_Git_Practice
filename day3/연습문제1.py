class Calculator:  #부모 
  def __init__(self):
    self.value = 0
  def add(self, val):
    self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
       self.value -= val
    def transfer(self, val):
       self.value += val

cal = UpgradeCalculator()
cal.add(10) #value 0 => 10
cal.minus(7)
cal.transfer(5)

print(cal.value) #10에서 7을 뺀 3을 출력