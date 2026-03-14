count = 0

for i in range(ord('가'), ord('힣') + 1):
    print(chr(i), end='')
    count += 1

print()
print(count)