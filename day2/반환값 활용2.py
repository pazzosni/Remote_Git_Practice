# 사칙연산 계산기
def cal(a, b, etc):
    if etc == '+':
        return a+b
    elif etc == '-':
        return a-b
    elif etc == '*':
        return a*b
    elif etc == '/':
        return a/b


result = cal(10, 20, '/')
print(result)