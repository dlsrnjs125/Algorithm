# 20230418
n, m = map(int, input().split(' '))
a = [] # 듣지 못하는 사람
b = [] # 보지 못하는 사람
result = []

for i in range(n):
    a.append(input())
    
for i in range(m):
    b.append(input())
    
result = list(set(a) & set(b)) # set으로 '&' 연산자를 통해 교집합
result.sort()

print(len(result))
print(' '.join(result), end=' ')