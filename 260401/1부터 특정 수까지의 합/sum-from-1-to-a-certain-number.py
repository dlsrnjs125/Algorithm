n = int(input())

# Please write your code here.

def print_sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    
    print(sum // 10)

print_sum(n)