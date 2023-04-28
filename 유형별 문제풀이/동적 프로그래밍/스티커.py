# 20230428
test = int(input())

for i in range(test):
    s = []
    n = int(input())
    
    for j in range(2):
        s.append(list(map(int, input().split(' '))))
        
    for k in range(1, n):
        # 두번째 값까지는 대각선 값 더해주기
        if k  == 1:
            s[0][k] += s[1][k-1]
            s[1][k] += s[0][k-1]
        # 세번째 값부터 max(대각선, 대각선 왼쪽)
        else:
            s[0][k] += max(s[1][k-1], s[1][k-2])
            s[1][k] += max(s[0][k-1], s[0][k-2])
    print(max(s[0][n-1], s[1][n-1]))