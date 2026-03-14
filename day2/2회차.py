my_list = ['오예스', '몽쉘' , '초코파이'] # 순서가 보장됨
my_list2 = ['오예스', '몽쉘' , '초코파이', '초코파이', '초코파이'] # 중복 가능

print(my_list[1:]) #몽쉘부터 출력
print(my_list2[0:]) #오예스부터 출력
print(len(my_list)) # 갯수가 몇개 인가

#리스트 수정법
my_list[1] = '몽쉘카카오'
print(my_list)

#값을 유하고 싶을시
#인덱스 함수를 사용 -> 변수 지정

#값을 추가하기
my_list.append('두쫀쿠')
print(my_list)

#값 삭제
my_list.remove('초코파이')
print(my_list)
#my_list.append('None') #None자체를 값으로 넣을 수 있음
my_list.remove(my_list[0]) #문법상으로는 문제가 안됨. 
print(my_list)

#다른 리스트 더하기
your_list ='빅파이', '오뜨'
my_list.append(your_list)
print(my_list)

my_list.pop
print(my_list)

#my_list.sort()

#튜플
my_tuple = ('몽쉘', '초코파이', '오예스') #패킹
(a1, b1, c1) = my_tuple #괄호가 없어도 되지만 가독성을 위해서 괄호를 씌우고 '언패킹'했다는 것을 알림
print(a1, b1, c1) #튜플을 사용해서 '언패킹'하게 되면 일반 변수로 사용할 수 있게 됨

# * : asterisk 사용법 -> 매개변수, 가변인자
numbers = (1,2,3,4,5,6,7,8,9,10)
(one, two, *other) = numbers
print(other) # 1,2 를 제외한 나머지 수가 출력이 됨. *를  변수명에 붙여도 되지만 *은 변수명에 포함하지 않기 때문에 빼는게 올바르게 사용하는 문법
print(other[0])

(one, *other, ten) = numbers
print(other)

친구A = {'돈가스', '보쌈', '제육덮밥'}
친구B = {'짬뽕' , '초밥' , '제육덮밥'}
print(친구A.intersection(친구B)) #두 변수의 교집합
print(친구A.union(친구B)) #두 변수의 합집합

person = {
    "이름": "김민석", 
    "나이" : 7, 
    "키":120, 
    "몸무게":23
    }

#print(person[0])#값이 출력되지 않음 key,value로 이루어져 있기 때문
print(person["나이"])
print(person.get("이름"))

#새로운 데이터 추가하기 (열을 추가할 때 많이 사용)
person["최종학력"] = '대학교'
print(person)

#특정 키의 밸류 바꾸기
person["키"] = 130

#여러 키의 밸류를 바꾸기 : update
person.update({"몸무게" : 50 , "최종학력" : '석사'})
print(person)

#특정 키 밸류 삭제하기
person.pop('몸무게')
print(person)

#모든 데이터 삭제 : clear
#어떤 키들이 있는가 : keys
print(person.keys)
#어떤 밸류들이 있는가 : values
print(person.values)
#어떤 키 밸류들이 있는가 : items
print(person.items)