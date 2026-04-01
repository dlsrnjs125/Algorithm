n = input()
a = list(map(int, input().split()))

for i in range(len(a)):
    print(a[i]**2, end=" ")