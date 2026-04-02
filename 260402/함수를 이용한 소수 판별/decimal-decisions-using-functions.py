a, b = map(int, input().split())

# Please write your code here.

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

total = 0

for i in range(a, b+1):
    if is_prime(i):
        total += i

print(total)