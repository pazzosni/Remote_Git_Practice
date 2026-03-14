#a 리스트에서 중복 숫자를 제거해 보자.
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
my_dic = dict.fromkeys(a) #딕셔너리의 특징을 사용하여 중복을 없앰
print(my_dic)
a = list(my_dic)
print(a)