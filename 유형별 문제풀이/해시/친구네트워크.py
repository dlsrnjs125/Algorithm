# 20230308
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
        return parent[x]
    else:
        return x
    
    
def union(x, y):
    x = find(x)
    y = find(y)
    
    if x != y:
        parent[y] = x
        number[x] += number[y]
    
test_case = int(input())

for _ in range(test_case):
    parent = dict()
    number = dict()
    
    friend_input = int(input())
    for _ in range(friend_input):
        x, y = input().split(' ')
        
        # 입력값 초기화
        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1
            
        union(x, y)
        print(number[find(x)])