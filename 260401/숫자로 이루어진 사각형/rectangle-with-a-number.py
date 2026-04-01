n = int(input())

# Please write your code here.

def print_rect(n):
    cnt = 0
    for _ in range(n):
        for i in range(n):
            cnt = (cnt + 1) % 10
            if cnt == 0:
                cnt += 1
            print(cnt, end = ' ')
        print()

print_rect(n)