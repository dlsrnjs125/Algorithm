# 20230413
chansges = 1000 - int(input())
count = 0

for i in [500, 100, 50, 10, 5, 1]:
    count += chansges // i
    chansges = chansges % i
    
print(count)