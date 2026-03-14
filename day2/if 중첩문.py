#if 중첩문
yellow_card = 1
foul = False  #True : 파울을 1번 저질렀을때 , False : 파울을 저지르지 않았을때
if foul: #foul == True
    yellow_card += 1
    if yellow_card == 2:
        print('경고 누적 퇴장')
    else:
        print('휴..조심해야지')
else:
    print('주의')

