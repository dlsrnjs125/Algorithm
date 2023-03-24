# 20230324
import sys

n, c = map(int, sys.stdin.readline().split())
house = sorted([int(sys.stdin.readline()) for _ in range(n)])

def binary_search(array, start, end, target):
    global n
    
    while start <= end:
        mid = (start+end) // 2
        standard = 0
        cnt = 1
        for i in range(n):
            if house[i] - house[standard] >= mid:
                cnt += 1
                standard = i
        if cnt < target:
            end = mid-1
        else:
            start = mid+1
    return (start+end)//2
        
def solution(house, c):
    mingap = 1
    maxgap = house[-1] - house[0]
    answer = binary_search(house, mingap, maxgap, c)
    return answer

print(solution(house, c))