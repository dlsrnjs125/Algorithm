# 20230504
a, b = map(int, input().split())
sum = [0 for x in range(64)]

for i in range(1, 64):
    sum[i] = 2**(i-1) + 2*sum[i-1]
    
def check(num):
    count = 0
    bin_num = bin(num)[2:]
    length = len(bin_num)
    
    for i in range(length):
        if bin_num[i] == '1':
            # pow : num 보다 크지 않으면서 가장 큰 2의 거듭제곱 수
            pow = length - i -1
            # sum[pow] : num 보다 작은 자릿수를 가진 수들의 1을 모두 카운트
            count += sum[pow]
            # 가장 앞자리 1의 개수 추가
            count += (num - 2 ** pow + 1)
            num = num - 2 ** pow
    return count

print(check(b) - check(a-1))