import sys

input = sys.stdin.readline


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union_(a, b):
    a = find(a)
    b = find(b)

    # 이미 부모가 같다면 리턴
    if a == b:
        return

    if rank[a] > rank[b]:
        parent[b] = a
    elif rank[a] < rank[b]:
        parent[a] = b
    else:
        parent[a] = b
        rank[b] += 1


N, M = map(int, input().split())

graph = []
parent = [i for i in range(N + 1)]  # 부모를 저장
rank = [0] * (N + 1)  # 각 노드마다 랭크를 저장
for i in range(M):
    a, b, cost = map(int, input().split())
    graph.append((a, b, cost))

graph.sort(key=lambda x: x[2])  # 마을의 비용을 오름차순으로 정렬
ans = 0  # 연결된 마을 길이의 합
end_v = 0  # 마지막에 연결된 마을 길이를 저장
for i in graph:

    if find(i[0]) != find(i[1]):
        union_(i[0], i[1])
        ans += i[2]  # 마을의 연결 비용들을 계속 더해주고
        end_v = i[2]  # 마지막에 연결된 마을 연결 비용을 저장

print(ans - end_v)  # 마지막에 연결된 연결 비용만 빼준 체 출력