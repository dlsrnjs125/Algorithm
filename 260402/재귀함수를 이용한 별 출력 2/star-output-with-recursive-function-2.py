n = int(input())

# Please write your code here.
def star(n):
    if n == 0:
        return
    print("* " * n)
    star(n-1)
    if n != 0:
        print("* " * n)

star(n)