#abc.txt 파일의 내용을 역순으로 바꾸어 저장하기
#파일을 불러올 수 있는가 - 읽기모드
#파일을 수정할 수 있는가 - 쓰기모드

'''f = open('./day4/abc.txt', 'r', encoding='utf8')
for lines in f:
    print(lines, end='')
f.close()'''

f = open('./day4/abc.txt', 'r', encoding='utf8')
lines = f.readlines() #f.readlines() : 파일의 모든 줄을 한번에 읽어서 리스트로 만들어주는 함수
for lines in reversed(lines):
    print(lines, end='')
f.close()