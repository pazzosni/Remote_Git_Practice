#간단한 메모장 만들기

'''원하는 메모를 파일에 저장하고 추가 및 조회가 가능한 간단한 메모장을 만들어 보자.

python memo.py -a “Life is too short”'''
#영어로만 된 파이썬 파일 만들어서 거기서 실행할 것
import sys

op = sys.argv[1] # 0번은 파이썬파일
if op == '-a':
    memo = sys.argv[2]
    with open('memo.txt', 'a') as f:
        f.write(memo)

elif op == '-v':
    with open('memo.txt', 'r') as f:
        print(f.read())