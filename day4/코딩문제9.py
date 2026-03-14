#sample.txt 파일의 숫자 값을 모두 읽어 총합과 평균 값을 구한 후 평균 값을 
#result.txt 파일에 쓰는 프로그램을 작성하시오.
# sample.txt : 70 60 55 75 95 90 80 80 85 100
''' 파일 쓰기
with open('sample.txt', 'w' , encoding='utf8') as f:
    f.write('70\n')
    f.write('60\n')
    f.write('55\n')
    f.write('75\n')
    f.write('95\n')
    f.write('90\n')
    f.write('80\n')
    f.write('80\n')
    f.write('85\n')
    f.write('100\n')

'''
# with.open('./day4/sample.txt', 'r', encoding='utf8') as f: #파일 읽기 with를 사용함으로써 자동 닫기
f = open('./day4/sample.txt', 'r', encoding='utf8')
num = [] #새로운 리스트 생성
    
for line in f:
    num.append(int(line)) #int화시켜 계산이 가능한 리스트로 변경
print(num)
f.close

aver = sum(num)/10

f = open('./day4/result.txt', 'w', encoding='utf8') #값을 구한 리스트를 새로운 파일에 추가
f.write(str(aver)) #읽으려면 문자열이여야 하기 때문에 str로 변경
f.close

f = open('./day4/result.txt', 'r', encoding='utf8') #값을 구한 리스트 파일을 읽기
print(f.read())
f.close