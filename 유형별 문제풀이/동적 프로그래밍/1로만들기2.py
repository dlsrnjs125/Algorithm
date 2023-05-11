# 20230511
import sys
n = int(sys.stdin.readline())

mem = [0] * (n+1) # 메모이제이션
path = ['' for _ in range(n+1)] # 최단 경로
path[1] = '1'

for idx in range(2, n+1):
    mem[idx] = mem[idx - 1] + 1
    prev = idx - 1
    if idx %  3 == 0 and mem[idx//3]+1 < mem[idx]:
        mem[idx] = mem[idx//3] + 1
        prev = idx // 3
    if idx %  2 == 0 and mem[idx//2]+1 < mem[idx]:
        mem[idx] = mem[idx//2] + 1
        prev = idx // 2
    path[idx] = str(idx) + ' ' + path[prev]

print(mem[n])
print(path[n])