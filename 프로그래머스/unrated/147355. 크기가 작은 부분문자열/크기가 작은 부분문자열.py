def solution(t, p):
    answer = 0
    n = len(p)
    
    for i in range(len(t) - n + 1):
        if p >= t[i:i+n]:
            answer += 1
    
    return answer