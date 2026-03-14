#glob모듈을 사용해서 C:\doit 디렉터리의 파일 중 확장자가 .py인 파일만 출력하는 프로그램을 만들어보자.
import glob

res = glob.glob('C:\lsc\*.py')

print(res)

print(len(res))