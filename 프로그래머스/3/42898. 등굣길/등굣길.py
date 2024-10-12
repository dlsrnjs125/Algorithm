def solution(m, n, puddles):
    dp = [[0]* (m+1) for i in range(n+1)] # dp 초기화
    dp[1][1] = 1 # 집 시작 위치
    
    for i, j in puddles:
        dp[j][i] = -1 # 웅덩이
        
    for i in range(1, n+1):
        for j in range(1, m+1):
            if dp[i][j] == -1: # 웅덩이
                dp[i][j] = 0
                continue
            dp[i][j] += (dp[i-1][j] + dp[i][j-1]) % 1000000007
    
    print(dp)
    return (dp[n][m])