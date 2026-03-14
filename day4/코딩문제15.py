#0~9의 문자로 된 숫자를 입력받았을 때, 
#이 입력값이 0~9의 모든 숫자를 각각 한 번씩만 사용한 것인지 확인하는 함수를 작성하시오.
#Duplicate Numbers

def check_unique_digits(number_string):
    # 0부터 9까지의 숫자를 모두 포함하는 문자열
    required_digits = set("0123456789")
    