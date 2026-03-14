#break 문
drama = ['시즌', '시즌2', '시즌3', '시즌4', '시즌5']
for x in drama:
    if x == '시즌4':
        print('재미 없대, 그만 보자')
        break
    print(f'{x}시청')