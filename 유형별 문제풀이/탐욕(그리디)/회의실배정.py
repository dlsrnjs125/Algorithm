# 20230419
import sys
n = int(sys.stdin.readline())
count= 1

time = [[0] * 2 for _ in range(n)]

for i in range(n):
    start, end = map(int, sys.stdin.readline().split(' '))
    time[i][0] = start
    time[i][1] = end

# 끝 시간 -> 시작 시간 순으로 정렬 -> 순서 중요
time.sort(key = lambda x : (x[1], x[0]))

end_time = time[0][1] # 정렬한 time에서 첫 회의 설정
for i in range(1, n):
    if time[i][0] >= end_time:
        count += 1
        end_time = time[i][1]
print(count)