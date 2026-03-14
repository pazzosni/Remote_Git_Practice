#문자열 바꾸기
#문자열의 split와 join함수를 사용하여 위 문자열을 다음과 같이 고치시오.
'''my_list = 'a:b:c:d'
change1 = my_list.split(':') #split함수 활용 ':'제외
change2 = '#'.join(change1) #join함수 활용 '#' 추가
print(change2)'''
#split 활용
a = 'a:b:c:d'
split_a = a.split(':')
split_a = ('#'.join(split_a))
print(split_a)