def solution(n):
    answer = 0
    num = 1
    
    for i in range(1, 12):
        num *= i
        
        if n < num:
            answer = i - 1
            break
        
    return answer