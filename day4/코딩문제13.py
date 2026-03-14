#DashInsert 함수는 숫자로 구성된 문자열을 입력받은 뒤 문자열 안에서 홀수가 연속되면 두 수 사이에 - 를 추가하고, 
#짝수가 연속되며 * 를 추가하는 기능을 갖고 있다. DashInsert 함수를 완성하시오.
number = input('입력 :')
nums = list(map(int,number)) #숫자 문자열 -> 숫자 리스트
result = []

for i, num in enumerate(nums):
    result.append(str(num)) #num = 4
    if i < len(nums) -1: #현재 요소가 다음 요소를 가질 때
        if(num %2 ==1) & (nums[i+1] %2==1): #현재 요소와 다음요소
            result.append('-')
        elif (num%2==0) & (nums[i+1] %2==0):
            result.append('*')

print("".join(result))