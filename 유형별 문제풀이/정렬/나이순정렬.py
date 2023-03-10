# 20230310
n = int(input())

array = [] # tuple 사용

for _ in range(n):
    input_date = input().split(' ')
    array.append((int(input_date[0]), input_date[1]))
    
array = sorted(array, key=lambda x: x[0]) # 나이를 기준으로 정렬

for i in array:
    print(i[0], i[1])