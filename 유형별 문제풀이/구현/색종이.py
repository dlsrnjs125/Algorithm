# 20230415
n = int(input())

paper = [[0]* 101 for i in range(101)]

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            paper[x+i][y+j] = 1
            
result = 0
for i in paper:
    result += sum(i)
print(result)