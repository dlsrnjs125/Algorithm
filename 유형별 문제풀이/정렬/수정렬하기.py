# 20230309
# 선택정렬 알고리즘
n = int(input())
array = list()

for _ in range(n):
    array.append(int(input()))
    
for i in range(n):
    min_index = i
    for j in range(i, n):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]
        
for i in array:
    print(i)
    
# 파이썬 기본 정렬 알고리즘 이용
n = int(input())
array = list()

for _ in range(n):
    array.append(int(input()))
                 
array.sort()

for i in array:
    print(i)