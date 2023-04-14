# 20230415
n = int(input())
row = [0] * n
result = 0

# x행에 놓은 Queen에 대해 검증
def check(x):
    for i in range(x):
        # 위, 대각선 확인
        if row[x] == row[i]:
            return False
        if abs(row[x] - row[i]) == x - i:
            return False
    return True

# x행에 대한 처리
def dfs(x):
    global result
    if x == n:
        result += 1
    else:
        for i in range(n):
            row[x] = i
            if check(x):
                dfs(x + 1)

dfs(0)
print(result)