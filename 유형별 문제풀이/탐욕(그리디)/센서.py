# 20230413
import sys

n = int(input())
k= int(input())

array = list(map(int, input().split(' ')))
array.sort()
distance = []

# k >= n 일 때 예외처리
if k >= n:
    print(0)
    sys.exit()

# 각 센서의 거리를 게산 -> 내림차순 정렬    
for i in range(1, n):
    distance.append(array[i] - array[i -1])
distance.sort(reverse=True)

# 거리가 긴 것부터 제거
for i in range(k-1):
    distance[i] = 0
print(sum(distance))