import glob

path = r'C:\KMS\day4\*.py'
# .txt, .jpg, .png 갯수확인할때 많이씀

cnt = glob.glob(path)
print(cnt, len(cnt))