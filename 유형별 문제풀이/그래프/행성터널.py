# 20230517
import sys
input = sys.stdin.readline

n = int(input())
xlist, ylist, zlist = [], [], []
parents = [i for i in range(n+1)]
edges = []
cnt, ans = n-1, 0

# 좌표를 x, y, z 별로 저장하고 정렬
for i in range(n):
    x, y, z = map(int, input().split())
    xlist.append((x, i))
    ylist.append((y, i))
    zlist.append((z, i))
xlist.sort()
ylist.sort()
zlist.sort()

def union(x, y):
    x = find(x)
    y = find(y)
    parents[y] = x
    
def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

# 인접한 행성들끼리 간선 구성
for curList in xlist, ylist, zlist:
    for i in range(1, n):
        w1, a = curList[i-1]
        w2, b = curList[i]
        edges.append((abs(w1 - w2), a, b))
edges.sort(reverse=True)

# 크루스칼 진행
while cnt:
    w, a, b = edges.pop()
    if find(a) == find(b):
        continue
    union(a, b)
    cnt -= 1
    ans += w
print(ans)