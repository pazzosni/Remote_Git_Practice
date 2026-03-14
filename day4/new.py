import sys

op = sys.argv[1] # 0번은 파이썬파일
if op == '-a':
    memo = sys.argv[2]
    with open('memo.txt', 'a') as f:
        f.write(memo)

elif op == '-v':
    with open('memo.txt', 'r') as f:
        print(f.read())