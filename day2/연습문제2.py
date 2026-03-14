#Q9. 다음과 같은 딕셔너리 a가 있다. 다음 중 오류가 발생하는 경우를 고르고, 그 이유를 설명해 보자.
'''a[‘name’] = ‘python’
a[(‘a’,)] = ‘python’
a[[1]] = ‘python’
a[250] = ‘python’
'''
a = dict()
print(type(a))
a['name'] = 'python'
a[('a', )] = 'python'
#a[[1]] = 'python'  #이 부분이 에러
a[250] = 'python'