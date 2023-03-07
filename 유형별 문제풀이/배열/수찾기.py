# 20230307
n = int(input())
n_data = set(map(int, input().split()))
m = int(input())
m_data = list(map(int, input().split()))

for i in m_data:
    if i not in n_data:
        print('0')
    else:
        print('1')