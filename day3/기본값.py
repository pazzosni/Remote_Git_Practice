def get_price(is_vip=False): # True : 단골 손님, False : 일반손님
    if is_vip == True:
        return 10000 #단골 손님
    else:
        return 15000 #일반 손님
    
price1 = get_price(True) #단골 손님
price2 = get_price(False) # 일반 손님
price3 = get_price(False) # 일반 손님
price4 = get_price(False) # 일반 손님