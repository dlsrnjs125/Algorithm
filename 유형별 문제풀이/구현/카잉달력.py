# 20230421
t = int(input())

def calculate(m, n, x, y):
    a = x # a(정답)를 처음 x 값으로 초기화
    while a <= m * n: # 정답의 범위는 m*n을 넘을 수 없다.
        if (a - x) % m == 0 and (a - y) % n == 0:
            return a
        a += m
    return -1 # 해가 없을 경우

for i in range(t):
    m, n, x, y = map(int, input().split(' '))
    print(calculate(m, n, x, y))