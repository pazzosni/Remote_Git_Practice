def order(shot=2, size='Regular', takeout=True):
    print(f'아메리카노', '{size} 사이즈 {shot}샷')
    if takeout:
        print('포장 주문이 완료되었습니다')
    else:
        print('주문이 완료되었습니다')

order(size='Regular')