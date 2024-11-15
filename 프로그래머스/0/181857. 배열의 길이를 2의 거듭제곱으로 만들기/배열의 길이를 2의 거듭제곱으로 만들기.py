def solution(arr):
    answer = []
    cnt = 0
    length = len(arr)
    
    while (length > 1):
        length = length / 2
        cnt += 1
    
    answer = arr + ([0] * (2**cnt - len(arr)))
    
    return answer