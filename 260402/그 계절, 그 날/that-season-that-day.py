y, m, d = map(int, input().split())

# Please write your code here.
# 윤년
def is_year(y):
    if y % 4 != 0:
        return False
    if y % 100 ==0 and y % 400 != 0:
        return False
    return True

# 월, 일이 존재하는지 검사
def is_month_day(y, m , d):
    if m <= 12:
        if m == 4 or m == 6 or m == 9 or m == 11:
            if d <= 30:
                return True
            else:
                return False
        elif m == 2:
            if is_year(y): # 윤년 검사
                if d <= 29:
                    return True
            else:
                if d <= 28:
                    return True
        else:
            if d <= 31:
                return True
            else:
                return False
    else:
        return False

# 어떤 계절 검사
def is_weather(m):
    if 3 <= m <= 5:
        print("Spring")
    elif 6 <= m <= 8:
        print("Summer")
    elif 9 <= m <= 11:
        print("Fall")
    else:
        print("Winter")
            