# 20230414
import heapq

n = int(input())
array = []
q = []

# 데드라인을 기준으로 정렬
for i in range(n):
    a , b = map(int, input().split(' '))
    array.append((a, b))
array.sort()

for i in array:
    a = i[0]
    heapq.heappush(q, i[1])
    # 힙 원소개수가 데드라인을 의미하게 된다.
    if a  < len(q):
        heapq.heappop(q)
        
print(sum(q))