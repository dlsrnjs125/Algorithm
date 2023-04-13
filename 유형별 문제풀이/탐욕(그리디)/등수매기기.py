# 20230412
n = int(input())
array = []
result = 0

for _ in range(n):
    array.append(int(input()))

# 오름차순으로 정렬    
array.sort()

for i in range(1, len(array) + 1):
    result += abs(i - array[i - 1]) # 불만도 합 계산
    
print(result)