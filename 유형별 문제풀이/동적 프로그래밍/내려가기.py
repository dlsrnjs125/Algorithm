# 20230426
n = int(input())
# 처음 숫자를 입력받아 DP의 초기값 설정
tmp = list(map(int, input().split(' ')))
max_dp = tmp
min_dp = tmp

for _ in range(n-1):
    a, b, c = map(int, input().split())
    # 밑에 값들을 입력받을 때마다, DP에 갱신 -> 슬라이딩 윈도우
    max_dp = [a + max(max_dp[0], max_dp[1]), b + max(max_dp), c + max(max_dp[1], max_dp[2])]
    min_dp = [a + min(min_dp[0], min_dp[1]), b + min(min_dp), c + min(min_dp[1], min_dp[2])]
    
print(max(max_dp), min(min_dp))