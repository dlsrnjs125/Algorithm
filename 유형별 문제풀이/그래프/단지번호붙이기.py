# 20230420
from collections import deque
n = int(input())
graph = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
count = []

for _ in range(n):
    graph.append(list(map(int, input())))
    
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    cnt = 1
    
    while queue:
        x, y = queue.popleft()
        
        # 현재 위치에서 4방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 위치가 벗어나지 않게(가장 먼저 체크해야한다.)
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0 # 방문한 노드 0으로 초기화
                queue.append((nx, ny))
                cnt += 1
    return cnt

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            count.append(bfs(i, j))
            
count.sort() # 오름차순으로 정렬
print(len(count))
for i in count:
    print(i)