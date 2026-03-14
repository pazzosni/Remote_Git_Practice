def visit(today, *customers): #customer1, 2 등으로 하면 변할때마다 수정해야하기때문에 *을 붙임으로써 몇개가 오든 대응 가능
    print(today) #날짜 출력
    for customer in customers:
        print(customer)
visit("2022년 6월 10일", "나장발") # 1명 방문
visit("2022년 6월 10일", "나장발", "나수염") # 2명 방문
visit("2022년 6월 10일", "나장발", "나수염", "나김리") # 3명 방문