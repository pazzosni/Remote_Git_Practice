f = open('list.txt', 'w', encoding='utf8')
f.write("김xx\n") # 문장 입력하기
f.write("정xx\n") # 문장 입력하기
f.write("허xx\n") # 문장 입력하기
# f라는 함수는 파일이 열려있는 상태이기 때문에 close함수를 써야 파일을 닫을 수 있음
f.close() #파일 닫기