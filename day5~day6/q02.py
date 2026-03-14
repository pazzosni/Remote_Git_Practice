#정규식 객체
import re

text = "abcdefg"

pattern = re.compile("e") # 문자열 패턴을 컴파일하여 정규식 객체를 반환

print("정규식 객체의 자료형 : ", type(pattern))

print("정규식 객체 사용하는 경우 : ", pattern.findall(text)) #["e"]

print("객체를 사용하지 않는 경우 : ", re.findall("e", text)) #["e"]