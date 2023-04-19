# 20230419
n = int(input())
s = [int(input()) for _ in range(n)]
dp = [0] * n

# 만약 계단이 2개일 경우
if len(s) <= 2:
    print(sum(s))
# 계단이 3개 이상일 경우
else:
    dp[0] = s[0]
    dp[1] = s[0] + s[1]
    # 3번째 계단부터 dp 점화식 이용
    for i in range(2, n):
        dp[i] = max(dp[i-2]+s[i], dp[i-3]+s[i-1]+s[i])
    print(dp[-1])