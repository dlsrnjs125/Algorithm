# 20230406
from collections import deque

def dfs(v):
    print(v, end=' ')
    visited[v] = True # 방문한 원소 방문처리
    for e in adj[v]:
        if not(visited[e]):
            dfs(e)

def bfs(v):
    q = deque([v]) # bfs 사용시 필요
    while q:
        v = q.popleft()
        if not(visited[v]):
            visited[v] = True
            print(v, end=' ')
            for e in adj[v]:
                if not visited[e]:
                    q.append(e)

n, m, v = map(int, input().split())
# 연결리스트 이용
adj = [[] for _ in range(n + 1)]

for _ in range(m): 
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

# 연결리스트 정렬 시켜줌으로서 가장 낮은 번호부터
for e in adj:
    e.sort()

visited = [False] * (n + 1)
dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)