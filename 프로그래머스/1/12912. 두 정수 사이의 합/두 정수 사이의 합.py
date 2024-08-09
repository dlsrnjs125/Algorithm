def solution(a, b):
    answer = 0
    min, max = 0, 0
    
    if a < b:
        min = a
        max = b
    else:
        min = b
        max = a
    
    for i in range(min, max+1):
        answer += i
    
    return answer