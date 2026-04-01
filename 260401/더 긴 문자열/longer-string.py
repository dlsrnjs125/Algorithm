a, b = list(input().split())

if len(a) > len(b):
    print(a, len(a))
elif len(a) == len(b):
    print("same")
else:
    print(b, len(b))