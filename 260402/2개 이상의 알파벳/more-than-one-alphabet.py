a = input()

# Please write your code here.
def has_2_more(a):
    if len(set(a)) >= 2:
        return True
    else:
        return False

if has_2_more(a):
    print("Yes")
else:
    print("No")