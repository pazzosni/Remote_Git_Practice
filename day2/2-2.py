my_list = '오예스', '몽쉘', '초코파이', '초코파이', '초코파이'
my_set = set(my_list)
my_list = list(my_set)
print(my_list) #순서가 보장이 안됨

#순서를 보장받고 싶으면 : dict.fromkeys
my_list = [1, 2, 3, 3, 3]
my_dic = dict.fromkeys(my_list)
my_list = list(my_dic)
print(my_list)