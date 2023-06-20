def solution(a, b):
    answer = 0
    
    for i in enumerate(b):
        answer += i[1] * a[i[0]]
    return answer