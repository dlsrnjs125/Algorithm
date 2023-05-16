# 20230516
text = input()
n = len(text)
dp = [0 for _ in range(n)]

table = [[False for _ in range(n)] for _ in range(n)]

for i in range(n):
    table[i][i] = True
    
for i in range(n-1):
    if text[i] == text[i+1]:
        table[i][i+1] = True
    
## 대각선 방향으로 채움
for a in range(n-2):
    for i in range(n-2-a):
        j = i + a + 2
        if text[i] == text[j] and table[i + 1][j-1]:
            table[i][j] = True
            
## dp
dp[0] = 1
for i in range(1, n):
    min_val = dp[i-1] + 1
    for j in range(i):
        if table[j][i]:
            min_val = min(min_val, dp[j-1] + 1)
    dp[i] = min_val
    
print(dp[-1])