# 20230408
from collections import deque
n = int(input())
m = int(input())
adj = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
count = 0

for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

def dfs(now_pos):
    global count
    visited[now_pos] = True
    for next_pos in adj[now_pos]:
        if not visited[next_pos]:
            dfs(next_pos)
    count = visited.count(True) - 1
            
def bfs(now_pos):
    global count
    q = deque([1])
    while q:
        now_pos = q.popleft()
        if not(visited[now_pos]):
            visited[now_pos] = True
            for next_pos in adj[now_pos]:
                if not visited[next_pos]:
                    q.append(next_pos)
    count = visited.count(True) - 1

bfs(1)
print(count)

dfs(1)
print(count)