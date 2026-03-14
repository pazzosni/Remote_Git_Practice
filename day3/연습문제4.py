#filter와 lambda를 사용해서 리스트 [1,-2,3,-5,8,-3]에서 음수를 제거해보자.
'''
my_list = [1,-2,3,-5,8,-3]
def my_list(x):
    return x > 0

print(list(filter(my_list, [1,-2,3,-5,8,-3])))
'''
num = [1,-2,3,-5,8,-3]
res = list(filter(lambda x:x>0, num))  #람다사용
print(res)