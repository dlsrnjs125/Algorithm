n = int(input())

# Please write your code here.
def get_num(n):
    tens = n // 10
    ones = n % 10 

    if n%2 ==0 and (tens+ones)%5==0:
        print("Yes")
    else:
        print("No")

get_num(n)