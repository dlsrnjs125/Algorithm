a, b = map(int, input().split())

# Please write your code here.
def in_369(n):
    s = str(n)
    if '3' in s or '6' in s or '9' in s:
        return True

def is_3(n):
    if n%3==0:
        return True

cnt = 0
for i in range(a, b+1):
    if in_369(i) or is_3(i):
        cnt+=1

print(cnt)
