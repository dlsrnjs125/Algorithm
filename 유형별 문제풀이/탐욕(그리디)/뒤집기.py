# 20230413
data = input()

count_0 = 0
count_1 = 0

# 첫번째 데이터 확인
if data[0] == '1':
    count_0 += 1
else:
    count_1 += 1

# 다음 데이터부터 비교
for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        if data[i + 1] == '1':
            count_0 += 1
        else:
            count_1 += 1
            
print(min(count_0, count_1))
