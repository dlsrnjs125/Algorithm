# 20230314
# 재귀 함수 이용
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(int(input())))

# 반복문 이용
n = int(input())

a, b = 0,1 

while n > 0:
    a, b = b, a + b
    n -= 1
    
print(a)