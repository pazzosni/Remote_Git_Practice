num = int(input('몇명이신가요?')) # int로 감싸주지않으면 문자열로 출력이되어 정수로 인식을 못함
print(type(num))

if num > 4:
    print('죄송하지만 저희는 4명까지만 예약이 가능합니다.')