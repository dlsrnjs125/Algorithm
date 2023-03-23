# 20230323
n, m = map(int, input().split())
array = []

for _ in range(n):
    array.append(input())
    
row = [0] * n
column = [0] * m

# x 표시가 있는 행,열
for i in range(n):
    for j in range(m):
        if array[i][j] == "X":
            row[i] = 1
            column[j] = 1

# x표시가 없는 행 갯수 카운트   
row_count = 0
for i in range(n):
    if row[i] == 0:
        row_count += 1
      
# x표시가 없는 열 갯수 카운트
column_count = 0
for j in range(m):
    if column[j] == 0:
        column_count += 1
        
print(max(row_count, column_count))