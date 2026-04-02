n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def is_same(a, b):
    for i in range(n):
        if a[i] not in b:
            return False
    return True

if is_same(a, b):
    print("Yes")
else:
    print("No")