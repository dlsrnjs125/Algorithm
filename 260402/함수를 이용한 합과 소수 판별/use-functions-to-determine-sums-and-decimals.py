a, b = map(int, input().split())
# Please write your code here.
# 소수 판별
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
# 자릿수 합이 짝수 판별
def is_even_num(x):
    a = str(x)
    sum = 0
    for i in range(len(a)):
        sum += int(a[i])
    if sum % 2 == 0:
        return True
    else:
        return False

cnt = 0
for i in range(a, b+1):
    if is_prime(i) and is_even_num(i):
        cnt += 1
    else:
        continue

print(cnt)