# iterator.py
class MyIterator:
    def __init__(self, data):
        self.data = data #self.data: 반복할 데이터를 저장한다.
        self.position = 0 #self.position: 현재 위치를 추적하는 변수이다(0부터 시작).

    def __iter__(self):#__iter__ 메서드: 이터레이터 객체 자신을 반환한다.
        '''이 메서드가 있어야 파이썬이 해당 객체를 반복 가능한 객체로 인식한다.
for 문, iter() 함수, next() 함수 등에서 사용하려면 반드시 구현해야 한다.
보통 return self로 자기 자신을 반환한다.'''
        return self

    def __next__(self):#__next__ 메서드: 다음 값을 반환하고,
        # 더 이상 값이 없으면 StopIteration 예외를 발생시킨다.
        if self.position >= len(self.data):
            raise StopIteration
        result = self.data[self.position]
        self.position += 1
        return result

if __name__ == "__main__":
    i = MyIterator([1,2,3])
    for item in i:
        print(item)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             