# 20230420
from collections import deque # bfs 사용시 필오
N, M = map(int, input().split(' '))

graph = []

for _ in range(N):
    graph.append(list(map(int, input())))

def bfs(x, y):
    # 이동할 4가지 방향(상하좌우)
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        
        # 현재 위치에서 4방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 위치가 벗어나지 않게(가장 먼저 체크해야한다.)
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            # 벽을 만났을 때
            if graph[nx][ny] == 0:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                
    return graph[N-1][M-1]

print(bfs(0,0))                