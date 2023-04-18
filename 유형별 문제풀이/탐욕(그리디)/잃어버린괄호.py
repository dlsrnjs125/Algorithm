# 20230418
n = input().split('-')
result = 0 # 결과를 저장
num = [] # '-'로 나눈 항들의 합을 저장

for i in n:
    sum = 0
    tmp = i.split('+')
    # 각 항들의 합을 num에 저장
    for j in tmp:
        sum += int(j)
    num.append(sum)
    
result = num[0] # 첫 항에서서 나머지 값을 빼주기 위해서

for i in range(1, len(num)):
    result -= num[i]
print(result)