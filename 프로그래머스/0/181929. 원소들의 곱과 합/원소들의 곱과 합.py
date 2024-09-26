def solution(num_list):
    answer = 0
    p = 1
    s = 0
    
    for i in num_list:
        s += i
        p *= i
    
    if s**2 > p:
        answer = 1
    
    return answer