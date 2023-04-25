# 20230425
n, m = map(int, input().split())
knowList = set(input().split()[1:])
parties = []
count = 0

for _ in range(m):
    parties.append(set(input().split()[1:]))
    
for _ in range(m):
    for party in parties:
        # party에 진실을 아는 사람이 있을 경우
        if party & knowList:
            knowList = knowList.union(party)

for party in parties:
    if party & knowList:
        continue
    count += 1
    
print(count)