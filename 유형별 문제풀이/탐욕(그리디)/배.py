# 20230413
import sys

n = int(input())
crains = list(map(int, input().split(' ')))
m = int(input())
boxes = list(map(int, input().split(' ')))

# 모든 박스를 못 옮기는 경우 -1 출력
if max(crains) < max(boxes):
    print(-1)
    sys.exit()

result = 0
count = 0
point = [0] * n # 크레인이 현재 옮겨야 하는 박스의 번호
visited = [False] * m # 박스를 옮겼는지 확인

# 내림차순 정렬(최소 시간을 구하기 위해)
crains.sort(reverse=True)
boxes.sort(reverse=True)

while True:
    if count == len(boxes):
        break
    for i in range(n):
        # 박스마다 크레인에 옮길 수 있는지 판단
        while point[i] < len(boxes):
            if not visited[point[i]] and crains[i] >= boxes[point[i]]:
                visited[point[i]] = True
                point[i] += 1
                count += 1
                break
            point[i] += 1
    result += 1
    
print(result)