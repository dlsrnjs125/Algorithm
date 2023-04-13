# 20230414
n, m = map(int, input().split(' '))
array = list(map(int, input().split(' ')))

# 0을 기준으로 분류하기 위해서
positive = []
negative = []
result = 0

largest = max(max(array), -min(array))

array.sort()

for i in array:
    if i > 0:
        positive.append(i)
    else:
        negative.append(-i)
# 양수쪽
for i in range(len(positive) - 1, -1, -m):
        result += positive[i]
# 음수쪽         
for i in range(0, len(negative), m):
    result += negative[i]
    
print(result * 2 - largest)