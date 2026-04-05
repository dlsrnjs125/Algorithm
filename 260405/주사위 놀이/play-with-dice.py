n = list(map(int, input().split()))
d = dict()

for i in range(1, 7):
    d[i] = n.count(i)

for key, value in d.items():
    print(f"{key} - {value}")
    