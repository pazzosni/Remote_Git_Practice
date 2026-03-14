#다음과 같이 실행할 때 입력값을 모두 더해서 출력하는 스크립트(C:\doit\myargv.py)를 작성해보자.
'''
C:\cd doit #현재 폴더를 doit폴더로 이동
C:\doit> python myargv.py 1 2 3 4 5 6 7 8 9 10 #python : 파이썬 실행. myargv.py : 실행할 파이썬 파일. 1~10 : 프로그램에 전달하는 입력값.
55
'''
import sys #명령행 인자

args = sys.argv[1:]  # 명령줄에서 프로그램 실행할 때 전달된 인자(값)들을 가져오는 코드

result = 0
for a in args:
    result += int(a)

print(result)