# 20230310
n = int(input())

array = [] # tuple 사용

for _ in range(n):
    x, y = map(int, input().split(' '))
    array.append((x, y))
    
array = sorted(array) # 기본라이브러리 사용 -> 오름차순으로 정렬

for i in array:
    print(i[0], i[1])