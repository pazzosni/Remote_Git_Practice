#map과 lambda를 사용해서 [1,2,3,4] 리스트의 각 요솟값에 3이 곱해진 리스트 [3,6,9,12]를 만들어보자.
my_list = [1,2,3,4]
def two_times(x):
    return x*2

print(list(map(two_times, my_list))) #lambda를 사용하지 않음
print(list(map(lambda x: x*2, my_list))) #lambda를 사용함