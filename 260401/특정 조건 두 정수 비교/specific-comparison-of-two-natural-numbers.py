a, b = map(int, input().split())

# 첫 번째 조건: a < b
if a < b:
    print(1, end=' ')
else:
    print(0, end=' ')

# 두 번째 조건: a == b
if a == b:
    print(1)
else:
    print(0)