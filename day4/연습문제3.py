#게시판 페이징하기

'''함수 이름은? get_total_page
입력받는 값은? 게시물의 총 개수(m), 한 페이지에 보여 줄 게시물 수(n)
출력하는 값은? 총 페이지 수'''

def get_total_page(m, n):
    if m % n == 0:
        return m // n
    return m // n+1

print(get_total_page(5, 10)) # 1
print(get_total_page(15, 10)) # 2
print(get_total_page(25, 10)) # 3
print(get_total_page(30, 10)) # 3