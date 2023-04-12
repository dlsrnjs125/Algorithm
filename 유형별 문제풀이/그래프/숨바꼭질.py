# 20230407
from collections import deque

MAX = 100001
n, k = map(int, input().split())
array = [0] * MAX

def bfs():
    q = deque([n])
    while q:
        now_pos = q.popleft()
        if now_pos == k:
            return array[now_pos]
        for next_pos in (now_pos - 1, now_pos + 1, now_pos * 2):
            if 0 <= next_pos < MAX and not array[next_pos]: # not을 쓰는 이유 -> 똑같은 곳 방문을 하지 않기 위해서
                array[next_pos] = array[now_pos] + 1 # 최소 시간 구하기
                q.append(next_pos)

print(bfs())