def solution(a, b):
    answer = 0
    v1 = str(a) + str(b)
    v2 = 2 * a * b
    
    if int(v1) >= v2:
        answer = int(v1)
    else:
        answer = v2
    
    return answer