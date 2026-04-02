y = int(input())

# Please write your code here.

def is_year(a):
    if a % 4 != 0:
        return False
    if a % 100 ==0 and a % 400 != 0:
        return False
    return True

if is_year(y):
    print("true")
else:
    print("false")