# 20230503
import heapq

n, k = map(int, input().split(' '))
jew = []
bags = []
answer = 0

for _ in range(n):
    heapq.heappush(jew, list(map(int, input().split(' '))))
    
for _ in range(k):
    bags.append(int(input()))
bags.sort() # 가방은 작은 순으로

temp_jew = []

for i in bags:
    while jew and i >= jew[0][0]: # jew가 존재하고 가방이 담을 수 있는 무게가 보석의 무게와 같거나 클 때
        heapq.heappush(temp_jew, -jew[0][1])
        heapq.heappop(jew)

    if temp_jew:
        answer -= heapq.heappop(temp_jew)
print(answer)