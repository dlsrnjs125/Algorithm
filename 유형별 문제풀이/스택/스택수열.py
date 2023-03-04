# 2023_03_03
n = int(input())

count = 1
stack = []
result = []

for i in range(1, n+1):
    data = int(input())
    while count <= data:
        stack.append(count)
        count += 1
        result.append('+')
    if stack [-1]== data: # 스택 최상위값과 비교
        stack.pop()
        result.append('-')
    else:
        print('NO')
        exit(0)

print('\n'.join(result))