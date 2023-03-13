# 20230313
import sys
n = int(sys.stdin.readline())
array = [0] * 10001 # 배열의 크기는 데이터의 범위를 포함할 수 있도록 설정

for i in range(n):
    data = int(sys.stdin.readline())
    array[data] += 1

for i in range(10001):
    if array[i] != 0:
        for j in range(array[i]): # 배열에 들어있는 숫자만큼 반복해서 출력
            print(i)