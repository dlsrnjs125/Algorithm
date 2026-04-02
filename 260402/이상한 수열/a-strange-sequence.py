n = int(input())

# Please write your code here.
def strange(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return strange(n//3) + strange(n-1)

print(strange(n))