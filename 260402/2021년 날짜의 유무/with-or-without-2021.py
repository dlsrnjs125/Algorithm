m, d = map(int, input().split())

# Please write your code here.
def is_month_day(m,d):
    if m <= 12:
        if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
            if d <= 31:
                return True
            else:
                return False
        elif m == 2:
            if d <= 28:
                return True
            else:
                return False
        else:
            if d <= 30:
                return True
            else:
                return False
    else:
        return False

if is_month_day(m, d):
    print("Yes")
else:
    print("No")