# 20230421
n = int(input())
# list -> dict (인덱스를 알고 있으면 바로 해당하는 데이터로 접근하기 때문에 메모리 절약)
dp = dict()

def fibo(n):
      if dp.get(n) != None:
            return dp[n]
      if n == 0:
            return 0
      if n == 1 or n == 2:
            return 1
      if n % 2 == 0: # 짝수
            dp[n // 2 + 1] = fibo(n // 2 + 1) % 1000000007
            dp[n // 2 - 1] = fibo(n // 2 - 1) % 1000000007
            return dp[n // 2 + 1] ** 2 - dp[n // 2 - 1] ** 2
      else: # 홀수
            dp[n // 2 + 1] = fibo(n // 2 + 1) % 1000000007
            dp[n // 2] = fibo(n // 2) % 1000000007
            return dp[n // 2 + 1] ** 2 + dp[n // 2] ** 2

print(fibo(n) % 1000000007)

# 메모리 초과(실패)
dp = [0] * (n+1)
dp[1] = 1
dp[2] = 1

def fibo(n):
    if n == 0:
        return dp[0]
    if n == 1 or n == 2:
        return dp[1]
    if n % 2 == 0:
        dp[n//2 + 1] = fibo(n//2 + 1) % 1000000007
        dp[n//2 - 1] = fibo(n//2 - 1) % 1000000007
        return dp[n // 2 + 1] ** 2 - dp[n // 2 - 1] ** 2
    else: # 홀수
        dp[n // 2 + 1] = fibo(n // 2 + 1) % 1000000007
        dp[n // 2] = fibo(n // 2) % 1000000007
        return dp[n // 2 + 1] ** 2 + dp[n // 2] ** 2

print(fibo(n) % 1000000007)