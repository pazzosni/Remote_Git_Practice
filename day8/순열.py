from itertools import permutations, combinations, product
res = (list(permutations([1,2,3,4,5,6], 3)))
print(res)
print(len(res))

c_res = (list(combinations([1,2,3,4,5,6], 3)))
print(c_res)
print(len(c_res))

pro_res = list(product([1,2,3,4,5,6], repeat = 3))
print(pro_res)
print(len(pro_res))