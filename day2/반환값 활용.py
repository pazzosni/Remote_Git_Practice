def get_price(is_vip): #True : 단골 손님, False : 일반 손님
    if is_vip == True:
        return 10000 #단골 손님
    else:
        return 15000 #일반 손님
    
price = get_price(True)
print(f'커트 가격은 {price} 원입니다')# 10000