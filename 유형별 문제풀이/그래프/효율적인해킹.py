# 20230410
from collections import deque

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
count = 0

for _ in range(m):
    x, y = map(int, input().split())
    adj[y].append(x)

def bfs(v):
    global count
    count = 0
    visited = [False] * (n + 1)
    q = deque([v])
    visited[v] = True
    while q:
        v = q.popleft()
        for e in adj[v]:
            if not visited[e]:
                q.append(e)
                visited[e] = True
    count = visited.count(True)
    return count

def dfs(v):
    global count
    count = 0
    global visited
    visited[v] = True
    for e in adj[v]:
        if not(visited[e]):
            visited[e] = True
            dfs(e)
    count = visited.count(True)
    return count


result = []
max_value = - 1

# bfs 오름차순으로 출력
for i in range(1, n + 1):
    c = bfs(i)
    if c > max_value:
        result = [i]
        max_value = c
    elif c == max_value:
        result.append(i)
        max_value = c
        
# dfs 오름차순으로 출렭
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    c = dfs(i)
    if c > max_value:
        result = [i]
        max_value = c
    elif c == max_value:
        result.append(i)
        max_value = c

for e in result:
    print(e, end=" ")